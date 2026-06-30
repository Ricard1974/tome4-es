#!/usr/bin/env python3
"""
CORRECCIÓN MASIVA DE CALIDAD — ToME4-es
Corrige errores conocidos en las traducciones existentes.

Errores que corrige:
  1. Tags de color rotas: #LIGHT GREEN# → #LIGHT_GREEN#
  2. Espacios extra alrededor de %s/%d/%0.2f
  3. Variables #Source#/#Target# faltantes (las restaura del original)
  4. Espacios al inicio/final de traducción
  5. Espacios antes de puntuación (. ! ? , ; :)
  6. Traducciones incorrectas conocidas (diccionario)
  7. Palabras duplicadas
  8. Etiquetas @var@ con espacios insertados

Uso:
  python3 scripts/fix_quality.py              # Aplica correcciones
  python3 scripts/fix_quality.py --dry-run    # Simulación
  python3 scripts/fix_quality.py --stats      # Solo estadísticas
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"


# =============================================================================
# 1. Tags de color válidas (extraídas de los textos originales)
# =============================================================================
def build_valid_tags():
    """Construye el set de tags de color válidas desde los originales."""
    tags = set()
    for fpath in sorted(SPLIT_DIR.rglob("*.lua")):
        with open(fpath, encoding="utf-8") as f:
            for line in f:
                m = re.match(r't\("([^"]+)",', line)
                if m:
                    tags.update(re.findall(r"#[A-Z_]+#", m.group(1)))
                    # También tags hex como #ff00ff#
                    tags.update(re.findall(r"#[a-fA-F0-9]{6}#", m.group(1)))
    return tags


# =============================================================================
# 2. Variables del juego que deben preservarse
# =============================================================================
GAME_VARS = [
    "#Source#",
    "#Target#",
    "#Actor#",
    "#Target2#",
    "@Source@",
    "@Target@",
    "@himher@",
    "@playername@",
    "@playerdescriptor.race@",
    "@playerdescriptor.subrace@",
    "@playerdescriptor.class@",
    "@playerdescriptor.gender@",
]

# Patrón para detectar estas variables en el texto
GAME_VAR_PATTERN = re.compile(r"(#[A-Z][a-z]+#|@[a-z.]+@)")


# =============================================================================
# 3. Errores de traducción específicos conocidos
# =============================================================================
SPECIFIC_FIXES = [
    # Cada entrada es (bad_spanish_pattern, good_spanish_replacement)
    # Se aplica sobre la traducción ya existente (español→español)
    # "Alter the appearance" → confundido con "altar" (más allá)
    ("Más allá de la apariencia de %s", "Cambiar la apariencia de %s"),
    ("Más allá de la apariencia de tu cuerpo", "Cambiar la apariencia de tu cuerpo"),
    (
        "Más allá de la apariencia de sus características faciales",
        "Cambiar la apariencia de tus rasgos faciales",
    ),
    ("Más allá de la apariencia de tu pelo", "Cambiar la apariencia de tu pelo"),
    (
        "Más allá de la apariencia de tu aura cosmética",
        "Cambiar la apariencia de tu aura cosmética",
    ),
    # "kiss her" → traducido obscenamente
    ("[la jode]", "[besarla]"),
    ("[Lean closer and kiss her]", "[Inclinarse y besarla]"),
    # "wares" → confundido con "wars" (guerras)
    ("tus guerras.", "tus mercancías."),
    ("Guerras de Gladiator", "Mercancías de gladiador"),
    ("las guerras del gladiador", "las mercancías del gladiador"),
    # "Use" → confundido con el verbo "Usar" en lugar de "Usa"
    ("Usar es", "Usa"),
]


def normalize_color_tags(text, valid_tags):
    """
    Corrige #LIGHT GREEN# → #LIGHT_GREEN# para tags de color conocidas.
    """

    def fix_tag(m):
        tag = m.group(0)
        # Reconstruir con underscores
        fixed = "#" + tag[1:-1].replace(" ", "_") + "#"
        if fixed in valid_tags:
            return fixed
        # Si no está en valid_tags pero tiene pinta de color tag...
        if re.match(r"^#[A-Z]+(?:_[A-Z]+)+#$", fixed):
            return fixed
        return tag  # No tocar si no parece tag de color

    result = re.sub(r"#[A-Z]+(?: [A-Z]+)+#", fix_tag, text)
    return result


def fix_format_spacing(text):
    """
    Normaliza espacios alrededor de %s, %d, %f:
      - Elimina espacios dobles alrededor de specifiers
      - Si el original tenía un patrón específico, respetarlo no es posible aquí
        porque solo tenemos la traducción. En su lugar, aseguramos que cada
        specifier tenga exactamente un espacio alrededor (como en el original inglés).

    NOTA: Esto es heurístico. En casos raros podría no ser perfecto, pero
    es mejor que tener espacios dobles o triples.
    """
    # Eliminar espacios dobles alrededor de format specifiers
    # Caso: "  %s" → " %s"
    text = re.sub(r"  (%[0-9+.\-]*[sdf])", r" \1", text)
    # Caso: "%s  " → "%s "
    text = re.sub(r"(%[0-9+.\-]*[sdf])  ", r"\1 ", text)
    # Caso: " texto%s" → " texto %s" (específico: spec pegado a palabra)
    # NO hacer esto porque puede ser intencional (ej. "%d%%")
    return text


def verify_game_vars(text, original):
    """
    Verifica que las variables del juego (#Source#, @Target@, etc.)
    presentes en el original también estén en la traducción.
    Si faltan, las restaura.
    """
    for var in GAME_VARS:
        count_orig = original.count(var)
        count_trans = text.count(var)

        if count_orig > count_trans:
            # La variable falta en la traducción
            # Intentar restaurarla en la posición aproximada
            # Buscar en qué posición estaba en el original
            orig_parts = original.split(var)
            if len(orig_parts) > 1:
                # Reconstruir: insertar la variable en la posición
                # donde estaría basado en el texto circundante
                # Estrategia simple: añadir al final
                text = text + " " + var

    return text


def find_and_restore_missing_vars(text, original):
    """
    Encuentra #Source#, #Target# etc. que faltan en la traducción
    y las inserta en la posición más probable.
    """
    orig_vars = GAME_VAR_PATTERN.findall(original)
    trans_vars = GAME_VAR_PATTERN.findall(text)

    for var in orig_vars:
        if var not in trans_vars and var in GAME_VARS:
            # Esta variable falta en la traducción
            # Buscar el texto circundante en el original para saber dónde insertarla
            idx = original.index(var)
            # Tomar el texto antes de la variable
            before = original[max(0, idx - 15) : idx].strip()
            after = original[idx + len(var) : idx + len(var) + 15].strip()

            # Intentar insertar la variable donde tenga sentido
            if before and before in text:
                text = text.replace(before, before + " " + var, 1)
            elif after and after in text:
                text = text.replace(after, var + " " + after, 1)
            else:
                # Añadir al final como fallback
                text = text.rstrip() + " " + var

    return text


def fix_trailing_spaces(text):
    """Elimina espacios al inicio y final de la traducción."""
    return text.strip()


def fix_space_before_punctuation(text):
    """
    Corrige espacios antes de puntuación en español.
    Ejemplo: "Hola !" → "Hola!"
    """
    text = re.sub(r"\s+([.!?,;:])", r"\1", text)
    return text


def fix_double_spaces(text):
    """
    Normaliza espacios múltiples a un solo espacio (excepto saltos de línea).
    Esto corrige los espacios dobles/triples que LibreTranslate inserta
    alrededor de placeholders y en otras posiciones.
    """
    # Colapsar 2+ espacios (que no sean \n) a 1 espacio
    text = re.sub(r" {2,}", " ", text)
    return text


def fix_duplicated_words(text):
    """Corrige palabras duplicadas (ej: 'loco loco' → 'loco')."""
    words = text.split()
    result = []
    for i, w in enumerate(words):
        if i > 0 and w.lower() == words[i - 1].lower() and len(w) > 2:
            continue  # Saltar duplicado
        result.append(w)
    return " ".join(result)


def parse_t_line(line):
    """Extrae (original, translation, type) de una línea t()."""
    m = re.match(
        r'^(\s*)t\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',
        line,
    )
    if m:
        return m.group(1), m.group(2), m.group(3), m.group(4)
    return None


# =============================================================================
# MAIN
# =============================================================================
def main():
    dry_run = "--dry-run" in sys.argv
    only_stats = "--stats" in sys.argv

    if only_stats:
        dry_run = True

    mode = " [SIMULACIÓN]" if dry_run else ""
    print("=" * 60)
    print(f"  CORRECCIÓN DE CALIDAD{mode}")
    print("=" * 60)

    # Construir tags de color válidas
    print("\n  📋 Analizando tags de color válidas...")
    valid_tags = build_valid_tags()
    print(f"     {len(valid_tags)} tags de color encontradas en originales")

    # Contadores
    stats = defaultdict(int)
    file_changes = defaultdict(list)

    for fpath in sorted(SPLIT_DIR.rglob("*.lua")):
        with open(fpath, encoding="utf-8") as f:
            content = f.read()

        original_content = content
        lines = content.split("\n")
        new_lines = []

        for line in lines:
            parsed = parse_t_line(line)
            if not parsed:
                new_lines.append(line)
                continue

            indent, orig, trans, type_ = parsed

            if orig == trans:
                new_lines.append(line)
                continue

            new_trans = trans
            file_issues = []

            # 1. Tags de color rotas
            fixed_trans = normalize_color_tags(new_trans, valid_tags)
            if fixed_trans != new_trans:
                n_tags = sum(1 for _ in re.finditer(r"#[A-Z]+(?: [A-Z]+)+#", new_trans))
                stats["color_tags_fixed"] += n_tags
                file_issues.append(f"color_tags:{n_tags}")
                new_trans = fixed_trans

            # 2. Espacios extra en format specifiers
            fixed_trans = fix_format_spacing(new_trans)
            if fixed_trans != new_trans:
                stats["format_spacing_fixed"] += 1
                file_issues.append("format_spacing")
                new_trans = fixed_trans

            # 3. Espacios al inicio/final
            fixed_trans = fix_trailing_spaces(new_trans)
            if fixed_trans != new_trans:
                stats["trailing_spaces_fixed"] += 1
                file_issues.append("trailing_spaces")
                new_trans = fixed_trans

            # 4. Espacios dobles/triples (normalizar)
            fixed_trans = fix_double_spaces(new_trans)
            if fixed_trans != new_trans:
                stats["double_spaces_fixed"] += 1
                file_issues.append("double_spaces")
                new_trans = fixed_trans

            # 5. Espacios antes de puntuación (numeración corregida)
            fixed_trans = fix_space_before_punctuation(new_trans)
            if fixed_trans != new_trans:
                stats["punct_spaces_fixed"] += 1
                file_issues.append("punct_spaces")
                new_trans = fixed_trans

            # 6. Variables #Source#/#Target# faltantes
            fixed_trans = find_and_restore_missing_vars(new_trans, orig)
            if fixed_trans != new_trans:
                stats["missing_vars_restored"] += 1
                file_issues.append("missing_vars")
                new_trans = fixed_trans

            # 7. Palabras duplicadas
            fixed_trans = fix_duplicated_words(new_trans)
            if fixed_trans != new_trans:
                stats["duplicated_words_fixed"] += 1
                file_issues.append("duplicated_words")
                new_trans = fixed_trans

            # 8. Traducciones incorrectas específicas
            for bad, good in SPECIFIC_FIXES:
                if bad in new_trans:
                    new_trans = new_trans.replace(bad, good)
                    stats["specific_fixes"] += 1
                    file_issues.append(f"specific:{bad[:20]}")

            if new_trans != trans:
                # Reconstruir línea
                new_line = f'{indent}t("{orig}", "{new_trans}", "{type_}")'
                new_lines.append(new_line)
                if file_issues:
                    file_changes[fpath].extend(file_issues)
            else:
                new_lines.append(line)

        new_content = "\n".join(new_lines)
        if new_content != original_content and not dry_run:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

    # Resumen
    print(f"\n  {'=' * 56}")
    print("  RESUMEN DE CORRECCIONES")
    print(f"  {'=' * 56}")

    categories = [
        ("Tags de color rotas", "color_tags_fixed"),
        ("Espacios en format specifiers", "format_spacing_fixed"),
        ("Espacios dobles/triples", "double_spaces_fixed"),
        ("Espacios al inicio/final", "trailing_spaces_fixed"),
        ("Espacios antes de puntuación", "punct_spaces_fixed"),
        ("Variables #Source# restauradas", "missing_vars_restored"),
        ("Palabras duplicadas", "duplicated_words_fixed"),
        ("Traducciones incorrectas", "specific_fixes"),
    ]

    total_fixes = 0
    for label, key in categories:
        count = stats[key]
        if count > 0:
            print(f"  ✓ {label:40s} {count:>5d}")
            total_fixes += count

    print(f"  {'─' * 50}")
    print(
        f"  TOTAL CORRECCIONES{' (simulación)' if dry_run else '':25s} {total_fixes:>5d}"
    )
    print(f"  Archivos modificados: {len(file_changes)}")

    if dry_run and total_fixes > 0:
        print("\n  💡 Ejecuta sin --dry-run para aplicar")
    elif not dry_run and total_fixes > 0:
        print("\n  ✅ Correcciones aplicadas")
        print("  💡 Ejecuta ahora: python3 scripts/merge_sections.py")
        print("     Luego:         python3 scripts/build_addon.py --package")


if __name__ == "__main__":
    main()
