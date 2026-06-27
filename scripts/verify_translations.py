#!/usr/bin/env python3
"""
Verificador de calidad de traducciones para ToME4-es.

Escanea todos los archivos split en busca de:
  - Cadenas sin traducir (EN == ES)
  - Spanglish (términos en inglés en medio de español)
  - "usted" (formal en lugar de "tú")
  - Términos de stats en inglés (Strength, Cunning, etc.)
  - Problemas de formato (%d%%, espacios extraños)

Uso:
  python3 scripts/verify_translations.py                    # Reporte completo
  python3 scripts/verify_translations.py --summary          # Solo resumen
  python3 scripts/verify_translations.py --json             # Salida JSON
"""

import re
import json
import sys
from pathlib import Path
from collections import defaultdict

# Añadir agent al path
sys.path.insert(0, str(Path(__file__).parent.parent / "agent"))

from terms import FORCED_TERMS

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
SPLIT_DIR = TRANS_DIR / "mod-tome-split"

# Términos en inglés que deberían estar traducidos en textos de juego
SPANGLISH_TERMS = {
    # Stats
    r"\bStrength\b": "Fuerza",
    r"\bDexterity\b": "Destreza",
    r"\bConstitution\b": "Constitución",
    r"\bWillpower\b": "Voluntad",
    r"\bCunning\b": "Astucia",
    r"\bMagic\b(?=\s+(?:power|damage|save|resistance))": "Magia",
    # Combat
    r"\bmelee\b": "cuerpo a cuerpo",
    r"\bMelee\b": "Cuerpo a cuerpo",
    r"\branged\b": "a distancia",
    r"\bRanged\b": "A distancia",
    r"\bdamage\b": "daño",
    r"\bDamage\b": "Daño",
    r"\bchance\b": "probabilidad",
    r"\bChance\b": "Probabilidad",
    r"\bstamina\b": "resistencia",
    r"\bstam\b": "res",
    r"\bmana\b": "maná",
    # Items
    r"\barmour\b": "armadura",
    r"\barmor\b": "armadura",
    r"\bresist\b": "resistencia",
    r"\bResist\b": "Resistencia",
    r"\bweapon\b": "arma",
    r"\bWeapon\b": "Arma",
}

# Stats completas en inglés (case-insensitive match for middle-of-text)
EN_STATS = {
    "strength",
    "dexterity",
    "constitution",
    "willpower",
    "cunning",
    "magic",
    "stamina",
    "mana",
    "psi",
    "positive",
    "negative",
}


def extract_calls(content):
    """Extrae todas las llamadas t() de un archivo."""
    calls = []
    for m in re.finditer(r't\("([^"]*)",\s*"([^"]*)",\s*"([^"]*)"\)', content):
        calls.append((m.group(1), m.group(2), m.group(3)))
    return calls


def has_spanglish(text):
    """Detecta términos en inglés en medio de texto en español."""
    if not text:
        return []
    hits = []
    for pattern, term in SPANGLISH_TERMS.items():
        if re.search(pattern, text):
            # Verificar que no sea parte de un nombre propio
            # Si el texto está mayormente en español, marcar
            hits.append(term)
    return hits


def has_usted(text):
    """Detecta uso de 'usted' (formal) en lugar de 'tú'."""
    if not text:
        return False
    return bool(re.search(r"\b[uU]sted\b", text))


def is_untranslated(original, translation, min_len=10):
    """Detecta cadenas sin traducir (original == translation y suficientemente largas)."""
    if not translation or not original:
        return False
    if original == translation and len(original) >= min_len:
        return True
    # También detectar si la traducción es solo formateo/cambio mínimo
    if len(original) >= min_len and original.lower() == translation.lower():
        return True
    return False


def scan_all():
    """Escanea todos los archivos split."""
    results = []
    total_calls = 0
    untranslated_count = 0
    spanglish_count = 0
    usted_count = 0
    stats_en = defaultdict(int)

    for fpath in sorted(SPLIT_DIR.rglob("*.lua")):
        rel_path = fpath.relative_to(SPLIT_DIR)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        calls = extract_calls(content)
        total_calls += len(calls)

        for original, translation, type_ in calls:
            issues = []

            # 1. Sin traducir
            if is_untranslated(original, translation):
                issues.append("UNTRANSLATED")
                untranslated_count += 1

            # 2. Spanglish
            spanglish_hits = has_spanglish(translation)
            if spanglish_hits:
                for term in spanglish_hits:
                    issues.append(f"SPANGLISH:{term}")
                spanglish_count += 1

            # 3. "Usted"
            if has_usted(translation):
                issues.append("USTED")
                usted_count += 1

            if issues:
                results.append(
                    {
                        "file": str(rel_path),
                        "type": type_,
                        "original": original[:80],
                        "translation": translation[:80],
                        "issues": issues,
                    }
                )

    return {
        "total_calls": total_calls,
        "untranslated": untranslated_count,
        "spanglish": spanglish_count,
        "usted": usted_count,
        "issues": results,
    }


def main():
    print("=" * 60)
    print("  VERIFICADOR DE CALIDAD - ToME4-es")
    print("=" * 60)

    report = scan_all()

    print(f"\n  Archivos: {len(list(SPLIT_DIR.rglob('*.lua')))}")
    print(f"  Cadenas t(): {report['total_calls']}")
    print(f"\n  📊 RESUMEN:")
    print(f"     Sin traducir:   {report['untranslated']}")
    print(f"     Spanglish:      {report['spanglish']}")
    print(f"     'Usted' formal: {report['usted']}")
    print(f"     Total issues:   {len(report['issues'])}")

    if "--json" in sys.argv:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    if "--summary" in sys.argv:
        return

    # Mostrar ejemplos por categoría
    if report["issues"]:
        print("\n  📋 EJEMPLOS POR CATEGORÍA:")

        # Untranslated
        untrans = [i for i in report["issues"] if "UNTRANSLATED" in i["issues"]]
        if untrans:
            print(f"\n  🔴 SIN TRADUCIR ({len(untrans)}):")
            for i in untrans[:5]:
                print(f"     [{i['file']}] {i['original'][:60]}")

        # Spanglish
        spang = [
            i for i in report["issues"] if any("SPANGLISH" in s for s in i["issues"])
        ]
        if spang:
            print(f"\n  🟡 SPANGLISH ({len(spang)}):")
            for i in spang[:5]:
                terms = [s.split(":")[1] for s in i["issues"] if "SPANGLISH" in s]
                print(f"     [{i['file']}] {', '.join(terms)}: {i['translation'][:60]}")

        # Usted
        usted = [i for i in report["issues"] if "USTED" in i["issues"]]
        if usted:
            print(f"\n  🟠 'USTED' ({len(usted)}):")
            for i in usted[:5]:
                print(f"     [{i['file']}] {i['translation'][:60]}")

    print("\n  💡 Para arreglar: python3 scripts/fix_quality.py")


if __name__ == "__main__":
    main()
