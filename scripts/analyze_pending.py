#!/usr/bin/env python3
"""
Extrae el vocabulario único de las cadenas sin traducir
para ayudar a completar el diccionario.
"""

import re
from pathlib import Path
from collections import Counter

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"


def get_untranslated_words():
    """Extrae todas las palabras de cadenas sin traducir."""
    words = Counter()
    all_texts = []

    for fpath in sorted(TRANS_DIR.glob("*.lua")):
        if fpath.name in (
            "_t_append.lua",
            "_not_merged.lua",
            "i18n.log",
            "copy_files.py",
        ):
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r't\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', line)
                if m and m.group(1) == m.group(2):
                    text = m.group(1)
                    all_texts.append(text)
                    # Extraer palabras (solo alfabéticas, >=3 letras)
                    for w in re.findall(r"[A-Za-z]{3,}", text):
                        words[w.lower()] += 1

    return words, all_texts


def main():
    words, texts = get_untranslated_words()

    print(f"Total textos sin traducir: {len(texts)}")
    print(f"Palabras únicas: {len(words)}")
    print()

    # Palabras más comunes que NO están en el diccionario base
    # (cargar palabras del diccionario existente)
    known_words = {
        # Artículos y preposiciones (ya tratados)
        "the",
        "a",
        "an",
        "of",
        "in",
        "on",
        "at",
        "to",
        "for",
        "with",
        "without",
        "by",
        "from",
        "as",
        "or",
        "and",
        "but",
        "if",
        "your",
        "you",
        "all",
        "some",
        "any",
        "no",
        "this",
        "that",
        # Verbos comunes ya en EN_ES
        "attack",
        "attacks",
        "hit",
        "hits",
        "strike",
        "strikes",
        "burn",
        "burns",
        "burning",
        "heal",
        "heals",
        "healing",
        "gain",
        "gains",
        "lose",
        "loses",
        "lost",
        "increase",
        "increases",
        "decrease",
        "decreases",
        "reduce",
        "reduces",
        "remove",
        "removes",
        "apply",
        "applies",
        "grant",
        "grants",
        "summon",
        "summons",
        "summoned",
        # Sustantivos comunes ya en EN_ES
        "damage",
        "power",
        "strength",
        "skill",
        "talent",
        "spell",
        "magic",
        "effect",
        "shield",
        "speed",
        "level",
        "range",
        "radius",
        "duration",
        "cooldown",
        # Ya traducidos en PHRASES
        "human",
        "elf",
        "dwarf",
        "orc",
        "skeleton",
        "halfling",
        "warrior",
        "mage",
        "rogue",
        "archer",
        "paladin",
    }

    print("=== PALABRAS FRECUENTES NO CUBIERTAS ===")
    for word, count in words.most_common(100):
        if word not in known_words and count >= 3:
            print(f"  {word}: {count}")

    print()
    print("=== TEXTOS CORTOS (<=40 chars) SIN TRADUCIR ===")
    short_texts = [t for t in texts if len(t) <= 40]
    for t in sorted(set(short_texts))[:30]:
        print(f'  "{t}"')


if __name__ == "__main__":
    main()
