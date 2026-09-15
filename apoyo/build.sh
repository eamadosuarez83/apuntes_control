#!/usr/bin/env bash
# Compila los apuntes.
#
#   apoyo/build.sh            genera las figuras y un PDF por clase
#   apoyo/build.sh libro      genera además el libro único con todas las clases
#
# Los PDFs quedan en build/, en la raíz del proyecto.
#
# Requiere: pandoc, texlive-xetex, lmodern, graphviz, python3 + schemdraw
#   sudo apt install pandoc texlive-xetex lmodern graphviz
#   pip install schemdraw matplotlib
set -e
export LC_ALL=C.UTF-8   # pandoc necesita locale UTF-8 para los titulos con acentos

APOYO="$(cd "$(dirname "$0")" && pwd)"
RAIZ="$(dirname "$APOYO")"
SALIDA="$RAIZ/build"
mkdir -p "$SALIDA"

# ------------------------------------------------------------------- figuras
# Cada script emite .svg (para leer el Markdown) y .pdf (vectorial, para
# XeLaTeX, que no incrusta SVG).
cd "$APOYO/figuras"
for py in *.py; do python3 "$py"; done
for f in *.dot; do dot -Tsvg "$f" -o "${f%.dot}.svg"; done

# -------------------------------------------------------------------- clases
# Se trabaja desde apuntes/ para que las rutas de imagen resuelvan.
cd "$RAIZ/apuntes"
PREPARADOS=()
for md in [0-9][0-9]-*.md; do
  # rutas de imagen a PDF; el H1 se quita porque el titulo va en el metadata
  sed 's|\(figuras/[A-Za-z0-9_-]*\)\.svg|\1.pdf|g' "$md" \
    | awk '!(hecho==0 && /^# /){print} /^# /{hecho=1}' > ".build-$md"
  PREPARADOS+=(".build-$md")

  TITULO=$(grep -m1 '^# ' "$md" | sed 's/^# //')
  pandoc ".build-$md" --metadata-file="$APOYO/metadata.yaml" \
    -M title="$TITULO" \
    -o "$SALIDA/${md%.md}.pdf" --pdf-engine=xelatex \
    --toc --toc-depth=2 --shift-heading-level-by=-1
done

# --------------------------------------------------------------------- libro
if [ "$1" = "libro" ]; then
  # aqui los H1 de cada archivo se vuelven capitulos
  LIBRO=()
  for md in [0-9][0-9]-*.md; do
    sed 's|\(figuras/[A-Za-z0-9_-]*\)\.svg|\1.pdf|g' "$md" > ".libro-$md"
    LIBRO+=(".libro-$md")
  done
  pandoc "${LIBRO[@]}" --metadata-file="$APOYO/metadata-libro.yaml" \
    -o "$SALIDA/libro-completo.pdf" --pdf-engine=xelatex \
    --toc --toc-depth=2 --top-level-division=chapter
  rm -f "${LIBRO[@]}"
  echo "Libro: build/libro-completo.pdf"
fi

rm -f "${PREPARADOS[@]}"
echo "PDFs por clase en build/"
