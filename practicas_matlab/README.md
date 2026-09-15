# Prácticas de MATLAB — original y equivalente en Python

Código de la materia (`salvar/control_digital/` en Nextcloud), tal cual
se usó en clase en 2018. Cada `.m`/`.slx` original queda junto a su
traducción a Python (mismo nombre base, extensión `.py`), para poder
comparar línea a línea.

Esto es distinto de los capítulos de `apuntes/`: allá el código Python ya
está narrado dentro de la explicación del tema (con la crítica de qué
está bien, qué está mal y por qué) y **no se toca**. Acá es la traducción
directa del script tal como está, sin comentario pedagógico — una
referencia de "esto en MATLAB es esto mismo en Python".

| Original | Python | Qué hace | Aparece también en |
|---|---|---|---|
| `clase1.m` | `clase1.py` | $G=s/[(s+2)(s^2+s+8)]$, polos/ceros/ganancia DC | cap. 02 |
| `clase2.m` | `clase2.py` | PID $K=386$, $T_i=900$, $T_d=1000$ sobre una planta de 3er orden | cap. 05 |
| `clase3` (sin extensión) | `clase3a.py` | `ilaplace` de $1/[s(s^2+4)]$ | cap. 02 |
| `clase3.m` | `clase3b.py` | `ilaplace` de $1/[s(s^2-s+4)]$ | cap. 02 |
| `clase4.slx` | `clase4.py` | Simulink: Step/Random + Relay + planta $1/(s+1)$ | cap. 05 (figura ilustrativa, no esta reconstrucción exacta) |

## Sobre `clase4.slx`

Es un diagrama de Simulink, sin código de texto. Los parámetros de
`clase4.py` **no son una interpretación** — se decodificaron leyendo el
XML interno del `.slx` (es un zip; `simulink/blockdiagram.xml` tiene cada
bloque y cada conexión con sus parámetros). Ahí se descubrió algo que no
era evidente solo mirando los tipos de bloque:

- La planta es literalmente `tf(1,[1 1])`, o sea $1/(s+1)$.
- El segundo puerto del bloque `Sum` **no está cableado** — no hay lazo
  cerrado ni realimentación: es un modelo abierto para visualizar cómo el
  *Relay* condiciona una señal antes de la planta.
- El `Relay` usa los valores por defecto de Simulink (umbral de
  encendido = apagado = 1), y con el escalón por defecto (que se queda
  parado exactamente en 1) eso produce *chattering* — el relé conmuta en
  cada paso de simulación porque la entrada nunca cruza el umbral, solo
  lo toca. Con la rama de ruido (`Random Number`) sí conmuta con
  normalidad. Ver el docstring de `clase4.py` para el detalle completo.

Este hallazgo es más preciso que el que se usó para la figura del
capítulo 05 (`clase4_onoff_ruido.svg`, un lazo cerrado con ruido en la
medida e histéresis, hecho como ilustración general del concepto antes de
poder leer el `.slx` en detalle). Esa figura y su texto se dejan como
están — la corrección queda documentada acá y en `notas/NOTAS-DESARROLLO.md`.

## Requisitos

Las traducciones usan `control`, `sympy`, `numpy` y `matplotlib` — mismo
venv que el resto del repo (`~/.venvs/apuntes_control`).
