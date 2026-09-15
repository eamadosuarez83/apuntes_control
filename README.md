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
pip install schemdraw matplotlib control
```

(`control` — python-control, el equivalente del Control System Toolbox de
MATLAB — hace falta desde los capítulos 12 y 13. Si el sistema bloquea
`pip install` directo por PEP 668, usar un venv:
`python3 -m venv .venv && .venv/bin/pip install schemdraw matplotlib control`,
y correr `build.sh`/los scripts de `apoyo/figuras/` con ese Python.)

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
| `12-tecnicas-clasicas-de-diseno.md` | Lugar de las raíces, Nyquist, compensadores adelanto/atraso | — (complemento, no sale del cuaderno) |
| `13-complementos-digitales.md` | PID discreto, *dead-beat*, antialiasing, cuantización | — (complemento, no sale del cuaderno) |
| `14-modelado-de-sistemas-fisicos.md` | De la física a $G(s)$: analogías entre dominios, motor DC, linealización | — (complemento, no sale del cuaderno) |
| `15-instrumentacion-electronica.md` | Sensores, acondicionamiento, ADC, PWM, drivers, elección de $T$ | — (complemento, no sale del cuaderno) |
| `16-proyecto-integrador-motor.md` | Proyecto completo: identificar, diseñar PI, programar y verificar | — (complemento, no sale del cuaderno) |

**El escaneo del cuaderno terminó** en la página 57 (páginas 1–57
transcritas por completo). Los capítulos 12 y 13 son contenido
complementario agregado a partir de una evaluación del curso — cubren
temas del temario (transformación bilineal, retenedores, PID discreto,
etc.) y de control clásico en general que no llegaron a aparecer en el
cuaderno; ver `notas/NOTAS-DESARROLLO.md` para el detalle de qué se agregó
y por qué.

## Criterio

Se transcribe lo que dice el cuaderno. Los errores detectados no se corrigen en
el texto de las clases: quedan registrados en
[`notas/NOTAS-DESARROLLO.md`](notas/NOTAS-DESARROLLO.md), junto con las dudas
de lectura del manuscrito y los vacíos de contenido a cubrir más adelante.

## PDFs incluidos

La carpeta `pdf/` trae los PDFs ya compilados (un capítulo por archivo más
`libro-completo.pdf`) para poder leerlos sin instalar nada. Se regeneran con
`apoyo/build.sh`, que los escribe en `build/`.
