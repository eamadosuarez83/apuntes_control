# Apuntes de Sistemas de Control Digital

Transcripción a Markdown de un cuaderno manuscrito del curso de *Sistemas de
Control Digital*, con los diagramas rehechos por script y compilación a PDF.

## Estructura

```
apuntes/        una clase por archivo, numeradas en orden de lectura
apoyo/          todo lo que no es contenido de clase
  figuras/      scripts que generan las figuras, y las figuras generadas
  build.sh      compila los PDFs
  metadata.yaml, metadata-libro.yaml
notas/          bitácora del proyecto: dudas de lectura, errores, vacíos
build/          PDFs compilados (no versionado)
```

## Compilar

```bash
./apoyo/build.sh          # un PDF por clase, en build/
./apoyo/build.sh libro    # además el libro completo: build/libro-completo.pdf
```

Dependencias:

```bash
sudo apt install pandoc texlive-xetex lmodern graphviz
pip install schemdraw matplotlib
```

Nota: XeLaTeX no incrusta SVG, así que cada script de `apoyo/figuras/` genera
las dos versiones — `.svg` para leer el Markdown en GitHub o en un visor, y
`.pdf` vectorial para el LaTeX. `build.sh` sustituye las rutas al vuelo.

## Contenido

| Archivo | Tema | Páginas del cuaderno |
|---|---|---|
| `01-fundamentos-control.md` | Temario, conceptos, lazo abierto y cerrado | 1–5 |
| `02-laplace-y-respuesta-temporal.md` | Laplace, estabilidad, fracciones parciales | 6–15 |
| `03-modelado-ganancias-y-frecuencia.md` | Circuito RC, ganancias, Bode, muestreo | 16–20, 25, 26 |
| `04-transformada-z-y-mapeo.md` | Transformada Z, mapeo de polos y ceros | 23, 24, 27–30 |
| `05-pid-y-control-on-off.md` | Lazo cerrado, PID, on-off con histéresis | 21, 22 |
| `06-respuesta-transitoria-en-z.md` | Polo dominante, tiempos característicos | 31, 32, 35, 36 |
| `07-simplificacion-e-identificacion.md` | Simplificar modelos, identificación | 37–41, 56, 57 |
| `08-practica-motor.md` | Práctica del motor, divisor de tensión | 33, 34 |
| `09-error-estacionario-y-estabilidad.md` | Error en estado estable, margen, Routh | 42–47 |
| `10-pares-de-transformada-z.md` | Pares de transformada Z desde la serie | 48, 49 |
| `11-discretizacion-con-distintos-T.md` | Mapeo s→z con varios periodos de muestreo | 50–55 |

**El escaneo sigue en curso**: faltan las páginas 58 en adelante. Dentro de lo
ya transcrito siguen sin aparecer la transformación bilineal, los retenedores
en detalle y el desarrollo del criterio de Routh.

## Criterio

Se transcribe lo que dice el cuaderno. Los errores detectados no se corrigen en
el texto de las clases: quedan registrados en
[`notas/NOTAS-DESARROLLO.md`](notas/NOTAS-DESARROLLO.md), junto con las dudas
de lectura del manuscrito y los vacíos de contenido a cubrir más adelante.

## PDFs incluidos

La carpeta `pdf/` trae los PDFs ya compilados (un capítulo por archivo más
`libro-completo.pdf`) para poder leerlos sin instalar nada. Se regeneran con
`apoyo/build.sh`, que los escribe en `build/`.
