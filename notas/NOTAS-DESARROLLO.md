# Notas sobre el desarrollo del libro

Bitácora de cómo se está armando esta transcripción. Nada de esto entra en el
contenido de clase; va aparte a propósito.

## Origen del material

- Cuaderno manuscrito de *Sistemas de Control Digital*, curso tomado hace unos 6 años.
- Lotes transcritos:
  - páginas 1–5 → `01-fundamentos-control.md`
  - páginas 6–15 → `02-laplace-y-respuesta-temporal.md`
  - páginas 16–20, 25, 26 → `03-modelado-ganancias-y-frecuencia.md`
  - páginas 23, 24, 27–30 → `04-transformada-z-y-mapeo.md`
  - páginas 21, 22 → `05-pid-y-control-on-off.md`
  - páginas 31, 32, 35, 36 → `06-respuesta-transitoria-en-z.md`
  - páginas 37–41 → `07-simplificacion-e-identificacion.md`
  - páginas 33, 34 → `08-practica-motor.md`
  - páginas 42–47 → `09-error-estacionario-y-estabilidad.md`
  - páginas 48, 49 → `10-pares-de-transformada-z.md`
  - páginas 50–55 → `11-discretizacion-con-distintos-T.md`
  - páginas 56, 57 → sección añadida a `07-simplificacion-e-identificacion.md`

  A partir de este lote los archivos ya no siguen el orden del cuaderno: el
  manuscrito intercala Bode y muestreo entre las páginas de transformada Z, y
  aquí se agrupan por tema.
- Criterio: se transcribe el contenido técnico. Lo administrativo queda aquí abajo
  como registro, no en el cuerpo del libro.

### Datos administrativos del cuaderno (archivo)

| Dato | Valor en el cuaderno |
|---|---|
| Docente | Cristian Gutiérrez |
| Plataforma | Edmodo, código de clase `gc2af5` |
| 1.er parcial | 11 de septiembre |
| 2.º parcial | 23 de octubre |
| 3.er parcial | 27 de noviembre |

Notas: la tercera letra del código de Edmodo es ambigua en el original, y de todos
modos Edmodo cerró en 2022. El correo institucional queda por verificar.

## Herramientas para los diagramas de bloques

Probadas dos, elegida **schemdraw**:

| Herramienta | Veredicto |
|---|---|
| **schemdraw** (Python) | Elegida. El módulo `dsp` trae sumador con cruz y signos ±, nodos de derivación, y el posicionamiento es explícito — que es justo lo que pide un diagrama de bloques. Script versionable, salida SVG/PNG/PDF. |
| **Graphviz** | Sirve, queda guardado en `diagramas/*.dot` como alternativa. Pelea: el lazo de realimentación necesita `constraint=false`, el sumador es un círculo vacío sin símbolo, y con `splines=ortho` se pierden las etiquetas de arista (hay que usar `xlabel`). |
| **TikZ** | Opción si algún día se compila todo como documento LaTeX nativo. Es el estándar en los libros de control, pero más lento de escribir. |
| **Mermaid** | Solo si se necesita que renderice directo en GitHub/Obsidian sin compilar nada. Queda pobre para control. |

## Cadena de compilación

Markdown → `pandoc` → XeLaTeX → PDF, con `build.sh`.

Detalle que obliga a generar los diagramas dos veces: **XeLaTeX no incrusta SVG**.
Por eso `build.sh` corre `bloques_schemdraw.py` con salida `.svg` (para leer el
Markdown en cualquier visor) y otra vez con salida `.pdf` (vectorial, para el
LaTeX), y luego sustituye las rutas `_sd.svg` → `_sd.pdf` en una copia temporal
del Markdown.

Dependencias en Debian/Ubuntu:

```bash
sudo apt install pandoc texlive-xetex lmodern graphviz
pip install schemdraw
```

Los metadatos del PDF (título, idioma, márgenes, numeración) viven en
`metadata.yaml`, fuera del contenido, para que los archivos de apuntes queden
limpios.

## Convenciones

- Un archivo por lote de páginas: `NN-tema.md`, numerado en orden del cuaderno.
- Los diagramas siempre en `diagramas/`, generados por script — nunca imágenes
  sueltas sin fuente. Cada script emite `.svg` y `.pdf` por su cuenta, y
  `build.sh` corre todos los `.py` que encuentre.
- Los mapas de polos van en `planos_s.py` (matplotlib); los diagramas de bloques
  en `bloques_schemdraw.py`; los circuitos en `circuito_rc.py` (schemdraw con
  `elements`); las figuras de la parte discreta (mapeo s→z, aliasing, on-off)
  en `discretos.py`.
- Cuando una figura del cuaderno es un trazo cualitativo (la respuesta on-off,
  por ejemplo), se reproduce con una simulación mínima y se avisa en el pie que
  los valores son ilustrativos.
- Matemáticas en LaTeX entre `$` / `$$`; cadenas de despeje en un solo bloque
  `aligned` (varios `$$` seguidos se desbordan de la página).
- Lo que no se lee bien en el manuscrito se transcribe con la mejor lectura y se
  marca en *cursiva* como duda, en lugar de inventar.
- Lo que el cuaderno anota mal o incompleto se corrige, pero se deja constancia
  aquí si el cambio es de fondo.
- Los datos personales que aparezcan en el cuaderno (la pág. 33 trae un nombre
  y un teléfono anotados al pie) no se transcriben.

## Dudas de lectura

Lo que no se distingue bien en el manuscrito. Mejor lectura adoptada, marcada
para revisar contra el cuaderno físico.

| Ubicación | Duda |
|---|---|
| pág. 1 | código de Edmodo: tercera letra ambigua (`gc2af5`) |
| pág. 1 | correo del docente, sin verificar |
| pág. 8 | tras `y(t) = (1/a)e^{at} − 1/a` dice "tiene cero en *a* y otro en 0"; por el desarrollo son **polos**, no ceros — probable lapsus |
| pág. 11 | el término independiente del resultado se lee `1/4` o `(1/4)t`; se transcribió `1/4`, que es lo coherente con la entrada escalón |
| pág. 6 | el exponente del caso oscilatorio se lee `±jα`; podría ser `±jω` |
| pág. 17 | la etiqueta de la curva ideal/real se lee *"zona muestra"*; por el contexto (Δy/Δx y saturación) podría ser "zona lineal" o "zona muerta" |
| pág. 18 | la última línea se lee "la parte **derivativa** reduce el error en estado estable"; ver el punto 13 de abajo |
| pág. 19 | el límite se escribe con `4(s+2)` cuando la planta es `4(3s+2)`; en $s\to0$ da lo mismo (8), así que no cambia el resultado |
| pág. 30 | el valor de $K$ se lee `5.)637×10⁻³`; el cálculo con los números de la misma hoja da $5.65\times10^{-3}$ |
| pág. 36 | $\zeta$ se lee `0.735`; el cálculo da `0.235` — probablemente un 2 leído como 7 |
| pág. 36 | $K_{st}$ se lee `15.33`; el cálculo da `13.33` |
| pág. 33 | las dos últimas columnas de la tabla de resistencias (1.2 / 1.5 y 20 k / 25 k) no tienen encabezado |
| pág. 33 | $T$ del "caso último" quedó escrito como `T = 0.` sin completar |
| pág. 45 | el margen se lee `MG = -6 dB`; podría ser `-5 dB`. En la gráfica de al lado se marca 6 dB |
| pág. 46 | junto a $E_{ss}=1/K_v=0.5$ hay una anotación entre paréntesis ilegible, tipo *"(no pot actual)"* |
| pág. 52 | el exponente del retardo se lee `z^-4` o `z^-4.4`; con $T=0.1$ y 4.4 s debería ser $z^{-44}$ |
| pág. 54 | sobre $s_1$ hay anotado `44.375 → 1.3` con una flecha, sin contexto |

## Vacíos y errores detectados

Material para la fase de evaluación de contenido. Se transcribió lo que dice el
cuaderno; las correcciones van aquí, no en el texto.

### Lote de páginas 1–15

**Errores de fondo**

1. *Pág. 10:* "parte real del polo → respuesta natural, parte imaginaria →
   respuesta forzada". Está mal planteado. La parte real fija la envolvente
   (decaimiento o crecimiento) y la imaginaria la frecuencia de oscilación;
   ambas pertenecen a la respuesta natural. La respuesta forzada la aportan los
   polos de la **entrada** — en estos ejercicios, el término $1/4$ que viene del
   escalón.
2. *Pág. 14 (tarea):* el $y(t)$ final pierde el factor $1/4$ de los dos términos
   oscilatorios y el $1/\sqrt{15}$ del seno. Debería ser
   $y(t) = \tfrac14\left[1 - e^{t/2}\cos\tfrac{\sqrt{15}}{2}t - \tfrac{1}{\sqrt{15}}e^{t/2}\operatorname{sen}\tfrac{\sqrt{15}}{2}t\right]$.
3. *Pág. 12:* inconsistencia de signo — el denominador se escribe $s^2+s+4$ en
   una línea del planteamiento y $s^2-s+4$ en todo el resto. El desarrollo
   corresponde a $s^2-s+4$.
4. *Pág. 6:* la tabla de estabilidad dice "estable si $\operatorname{Re}\{s\}<0$".
   La condición es sobre **los polos**, no sobre la variable $s$.
5. *Pág. 6:* la sintaxis de Matlab anotada está incompleta: `feedback` necesita
   las funciones de la planta y de la realimentación, no un solo par
   `num/den`.

**Vacíos de contenido**

6. El caso $s = \pm j\alpha$ se llama "oscilatorio" sin decir que es el límite de
   estabilidad (estabilidad marginal), y solo vale para polos **simples** en el
   eje imaginario.
7. El ejercicio $1/(s-a)$ nunca discute el signo de $a$, aunque la gráfica
   dibujada es la del caso inestable $a>0$.
8. El ejercicio 2 (polo en $-a$) queda a medias: se plantean las ecuaciones de
   coeficientes y no se resuelve.
9. Solo hay 3 pares de transformadas en la tabla. Falta el par del escalón, la
   rampa, el impulso, y los teoremas de valor inicial y final.
10. Se enuncian la función de transferencia de lazo abierto y la de trayectoria
    directa, pero no se deduce la de **lazo cerrado** $Y/R = G/(1+GA)$ para ese
    diagrama, que es la que realmente se usa después.
11. El segundo ejercicio ($1/(s(s^2+4))$) da oscilación sostenida y no se
    comenta la relación con los polos en $\pm j2$.
12. Nada conecta todavía este material con el título del curso: todo va en el
    dominio $s$ continuo. La parte discreta (muestreo, transformada Z) aún no
    aparece.

### Lote de páginas 16–30

**Errores de fondo**

13. *Pág. 18:* "la parte derivativa reduce el error en estado estable". Es la
    acción **integral** la que elimina el error en estado estable; la
    derivativa actúa sobre la velocidad de cambio del error y mejora el
    amortiguamiento, no el error estacionario.
14. *Pág. 30:* $K$ anotado como $5.1637\times10^{-3}$. Con los valores de esa
    misma página, $1 = 4K/[(0.2693)(0.0839)]$ da
    $K = 5.65\times10^{-3}$. Hay una diferencia del 9 %: o el dígito está mal
    leído, o hay error aritmético. Se transcribió $5.6\times10^{-3}$.
15. *Pág. 23:* la forma factorizada escribe $M$ ceros pero los numera
    $z_1 \ldots z_n$, y $N$ polos numerados $p_1 \ldots p_n$. Los subíndices
    deberían ser $z_1 \ldots z_M$ y $p_1 \ldots p_N$.
16. *Págs. 17–18:* se llama "ejercicio de la clase 1" a dos plantas distintas:
    para $K_{st}$ el denominador es $(s+2)(s^2+s+8)$ y para $K_v$ es
    $s(s^2+s+8)$. Tiene sentido (la de $K_v$ necesita integrador), pero el
    cuaderno no lo dice y parece la misma planta.
17. *Pág. 20:* se escribe "↓70 % → 3 dB" sin el signo menos, que sí aparece en
    las otras dos apariciones de la misma regla.

**Vacíos de contenido**

18. La regla $\omega_s = 20\,\omega_{-3dB}$ (equivalente a $T = \pi/(10\omega)$)
    aparece encuadrada pero sin justificación. Es una regla práctica de
    ingeniería: muestrear 10 veces por encima del mínimo de Nyquist. Conviene
    explicar de dónde sale y contrastarla con el criterio $\omega_s \ge 2\omega_{BW}$
    de la pág. 25, que es el teórico.
19. El criterio de Nyquist se enuncia con $f_N$ y $f_{BW}$ sin definir $f_N$
    (¿frecuencia de muestreo o frecuencia de Nyquist?). En la desigualdad final
    $f_N \ge 2f_{BW}$ se está usando como frecuencia de muestreo.
20. No hay fórmulas para las especificaciones temporales: se definen settling
    time, rise time y sobrepaso en palabras, pero nunca se ligan a $\zeta$ y
    $\omega_n$ ($t_s \approx 4/\zeta\omega_n$, $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$).
21. Del PID solo está la forma paralela ideal. Faltan la sintonización (que es
    el tema de la Unidad 3), la discretización del PID y el problema del
    *windup* del integrador.
22. El control on-off se dibuja pero no se cuantifica: falta la relación entre
    el ancho de histéresis $\Delta$, la frecuencia de conmutación y el desgaste
    del actuador.
23. Del ejemplo muestreado ($T = 1$, ZOH, planta con retardo de 1.25 s) se da
    el resultado en $z$ ya factorizado, sin el desarrollo. Tampoco se comenta
    que el retardo no es múltiplo entero del periodo de muestreo, que es
    justamente lo que produce el cero en $z = -1.755$ (fuera del círculo).
24. La transformación bilineal, que está en el temario de la Unidad 1, todavía
    no aparece en ninguna página.
25. Los diagramas de Bode se leen "de la gráfica de MATLAB" en tres ejercicios.
    Para el libro conviene generar esos Bode con Python y marcar en ellos el
    punto $-3$ dB, en vez de depender de una gráfica que no está.

### Lote de páginas 31–41

**Errores de fondo**

26. *Pág. 36:* $\zeta = \pi/\omega_n$. La fórmula es
    $\zeta = \sigma/\omega_n$. Con $\sigma = 0.5602$ y
    $\omega_n = \sqrt{\sigma^2+\omega_d^2} = 2.382$ da $\zeta = 0.235$,
    que además coincide con leer el valor anotado como `0.235`.
27. *Pág. 36:* $K_{st} = 15.33$ para $G(z) = (z-0.2)/[(z-0.7)(z^2-1.6z+0.8)]$.
    Evaluando en $z=1$: $0.8/(0.3 \times 0.2) = 13.33$.
28. *Págs. 31–32:* de $z = 0.8 \pm 0.4j$ sale $\sigma = 0.5579$ y
    $\omega_d = 2.318$, y así lo escribe la primera línea
    ($-0.55785 \pm j2.315$). Dos renglones después pasa a usar
    $\sigma = 0.5602$, sin explicar el cambio. Todos los tiempos posteriores
    ($t_s$, $\beta$, $t_r$) están calculados con $0.5602$.
29. *Pág. 40:* el despeje de $\zeta$ deja la propia $\zeta$ dentro del
    radical ($\zeta = \sqrt{1 - (\zeta\pi/\ln 0.625)^2}$), lo cual es
    circular como está escrito. El valor final ($0.1479$) sí es el correcto:
    despejando bien, $\zeta^2 = 1/[1 + (\pi/\ln 0.625)^2]$.
30. *Pág. 40:* $\omega_n = \pi/(2.2\sqrt{1-0.1479})$. Dentro del radical
    debería ir $\zeta^2 = 0.0219$, no $\zeta$. El resultado anotado ($1.443$)
    corresponde al cálculo correcto, así que es solo un error de escritura.
31. *Pág. 40:* "como no tiene retardo, $e^{-T_ds} = 0$". Con $T_d = 0$ el
    término vale **1**, no 0; el efecto es que desaparece del modelo.
32. *Pág. 41:* el numerador del modelo identificado. Siendo
    $K\,\omega_n^2 = 0.4 \times 2.0736 = 0.829$, el numerador debería ser
    $0.829$ y no $0.56$ (que sale de $0.4 \times 1.4$). Con $0.56$ el modelo
    no reproduce $y_{ss} = 0.8$ ante el escalón de amplitud 2: da $0.54$.
    La figura del capítulo 7 está generada con el numerador correcto y sí
    reproduce el pico de $1.3$ y el estable de $0.8$ del ensayo.

**Vacíos de contenido**

33. El criterio del polo dominante ("multiplico por 5 la parte real") se usa
    sin justificar. Es la regla práctica de que un polo 5 veces más lejos
    contribuye un transitorio que se extingue 5 veces más rápido.
34. Las fórmulas de $t_p$, $t_s$, $t_r$ y $M_p$ aparecen aquí por primera vez,
    pero en la pág. 18 ya se habían definido esas mismas especificaciones solo
    en palabras. Al unificar el libro conviene juntarlas.
35. $t_s = 4/\sigma$ corresponde al criterio del 2 %, coherente con la
    definición de la pág. 18, pero el cuaderno no lo dice.
36. La afirmación "los ceros no influyen" es cierta solo para la
    **estabilidad**. Los ejemplos de la misma página muestran que sí influyen
    fuertemente en el transitorio: mover el cero de $0.2$ a $0.7$ lleva el
    sobrepico del 47 % al 80 %, y llevarlo a $1.1$ (fuera del círculo,
    sistema de fase no mínima) invierte el signo de la respuesta.
37. La identificación se hace con un solo ensayo al escalón y sin validación;
    falta contrastar el modelo contra los datos y hablar de ruido.
38. La página de la práctica del motor no dice cómo se mide la velocidad con
    el encoder (conteo de pulsos por ventana de tiempo, resolución) ni qué
    periodo de muestreo usar en esa medida.

### Lote de páginas 42–57

**Errores de fondo**

39. *Pág. 49:* el par del coseno queda con un factor 2 de más. Al escribir
    $\cos\omega t = (e^{j\omega t} + e^{-j\omega t})/2$ el $\tfrac12$ se
    pierde al sumar las dos series. El resultado correcto es
    $(z^2 - z\cos\omega)/(z^2 - 2z\cos\omega + 1)$, la mitad de lo anotado.
40. *Pág. 49:* se mezclan $\omega$ y $\omega n$ en los exponentes de la misma
    cadena. Debería ser $\omega T$ (o $\omega$ normalizada) de forma
    consistente en todas las líneas.
41. *Pág. 50:* al armar $G(z)$ solo aparece el binomio del par complejo; el
    polo real $z_1 = 0.00717$ desaparece del denominador sin explicación.
    Además "$4K = 1 \Rightarrow K = 0.2445$" no cuadra literalmente ($1/4 =
    0.25$): el 0.2445 sale de dividir por el denominador evaluado en $z=1$
    ($0.978$), que es lo correcto, pero la línea escrita se salta ese paso.
42. *Pág. 52:* de $s = -0.1282 \pm 0.3174j$ el binomio es
    $s^2 + 0.2564s + 0.1178$. El cuaderno lo escribe con signo menos en el
    término lineal, aunque el enunciado de arriba sí lo tiene positivo.
43. *Pág. 55:* el denominador usa $(z - 1.3)$, pero el polo calculado tres
    líneas antes es $z_1 = 0.77$. $1.3 = 1/0.77$, así que parece una
    inversión accidental. Con $(z-1.3)$ la evaluación en $z = 1$ da $-0.3$ y
    entonces "$1 = 4K/1$" no se sostiene: la ganancia saldría negativa.
44. *Pág. 55:* el binomio del par complejo se escribe con
    $380\times10^{-6}$ en el desarrollo y con $360\times10^{-6}$ en el
    resultado final encuadrado. De $0.00173 - 0.00135 = 0.00038$ el valor es
    $380\times10^{-6}$.
45. *Pág. 57:* el modelo identificado queda como
    $2.07/(s^2 + 0.3685s + 2.07)$, que tiene ganancia estática 1. Con
    $K_{st} = 0.9$ el numerador debería ser $K\,\omega_n^2 = 1.865$. Es el
    mismo error del primer ejemplo de identificación (punto 32), esta vez en
    la otra dirección: allí se usó $K\,\omega_n$, aquí solo $\omega_n^2$.

**Vacíos de contenido**

46. La tabla de Routh se plantea (filas, columnas, $n+1$ filas) pero **nunca
    se dan las fórmulas de los coeficientes** $b_i$ y $c_i$, ni se resuelve un
    ejemplo, ni se enuncia la conclusión del criterio (número de cambios de
    signo en la primera columna = número de polos en el semiplano derecho).
47. El margen de ganancia se define y se da $K_{max} = 10^{MG/20}$, pero no
    aparece el **margen de fase**, que es su pareja natural y suele pesar más
    en el diseño.
48. No se explica por qué el criterio de Routh, que es del plano $s$, se
    aplicaría a un sistema discreto. Falta la transformación bilineal (que
    sigue sin aparecer en el cuaderno) o el criterio de Jury, que es el
    equivalente directo en $z$.
49. En las tablas de $K_p$ y $K_v$ se usa $r$ como número de integradores sin
    decir que es el "tipo" del sistema, y no aparece la tercera constante,
    $K_a$ (error de aceleración, entrada parábola).
50. Los casos de las págs. 50–55 no dicen de qué sistema salen los polos
    $-49.375$ y $-37.81 \pm 52.27j$, ni qué se está diseñando. Al unificar el
    libro habrá que reconstruir el enunciado o marcarlos como ejercicios de
    mapeo sueltos.
51. Del retardo de 4.4 s solo queda planteada la propiedad de traslación.
    Falta cerrar cómo se incorpora $z^{-d}$ al modelo y qué pasa cuando el
    retardo no es múltiplo entero de $T$.

## Corrección de errores aritméticos (fase de evaluación de contenido)

A diferencia del resto de este documento (que solo *registra* errores sin
tocar el texto de las clases, ver "Criterio" en el README), en esta pasada
sí se corrigieron directo en los `.md` los errores aritméticos ya
identificados arriba — a pedido explícito, para poder estudiar de este
material con confianza en los números. Cada corrección queda marcada con un
comentario HTML `<!-- Nota fig. NOTAS-DESARROLLO.md #N: ... -->` en el punto
exacto del archivo (invisible en el PDF, visible en el `.md` fuente), para
poder rastrear qué se tocó y por qué sin tener que volver a este archivo.

| # | Archivo | Qué se corrigió |
|---|---|---|
| 14 | `04-transformada-z-y-mapeo.md` | $K=5.6\times10^{-3}\to 5.65\times10^{-3}$, con el despeje explícito |
| 26 | `06-respuesta-transitoria-en-z.md` | $\zeta=\pi/\omega_n=0.735\to\zeta=\sigma/\omega_n=0.234$ (fórmula y valor) |
| 27 | `06-respuesta-transitoria-en-z.md` | $K_{st}=15.33\to13.33$ (variante del ejercicio, polo en 0.7) |
| — | `06-respuesta-transitoria-en-z.md` | Efecto en cascada de #28 (σ=0.5602→0.5579): recalculados $M_p$, $y_p$, $t_s$, $\beta$, el criterio ×5 y $\omega_n$ |
| 32 | `07-simplificacion-e-identificacion.md` | Numerador del primer modelo identificado: $0.56\to K\omega_n^2=0.829$ |
| 45 | `07-simplificacion-e-identificacion.md` | Mismo error al revés en el segundo ejemplo: $2.07\to K\omega_n^2=1.865$ |
| 39 | `10-pares-de-transformada-z.md` | Par del coseno: se perdía el factor $\tfrac12$ al sumar las series — resultado quedaba el doble. Reescrita la derivación completa con el $\tfrac12$ explícito, y unificada la notación a $\omega T$ (#40) |
| 43 | `11-discretizacion-con-distintos-T.md` | Caso 4: $(z-1.3)\to(z-0.77)$ (el polo ya calculado, `1.3` parece $1/0.77$ invertido por accidente) — recalculada $K$ en consecuencia ($0.25\to0.0575$) |
| 44 | `11-discretizacion-con-distintos-T.md` | Mismo caso: unificado $380\times10^{-6}$ (el que da el propio desarrollo) en vez de $360\times10^{-6}$ que aparecía solo en el resultado encuadrado |

**No se tocó** el punto #41 (pág. 50, $K=0.2445$): ahí el valor final ya es
correcto, solo le falta un paso intermedio en el desarrollo — no es un
error, es un vacío menor, se deja para una revisión de redacción aparte.

## Vacíos de contenido completados

Se agregó teoría + ejercicio resuelto para los temas del propio temario
(cap. 1) que nunca llegaron a aparecer en el cuaderno transcrito:

| Tema | Vacío original | Dónde quedó | Qué se agregó |
|---|---|---|---|
| Retenedor de orden cero (ZOH) | Se usaba la fórmula $(1-e^{-Ts})/s$ sin derivarla | `04-transformada-z-y-mapeo.md` | Derivación desde el pulso rectangular, respuesta en frecuencia (sinc, retardo de fase $T/2$), ejercicio de discretización con ZOH |
| Retenedor de orden uno (FOH) | #24, nunca aparecía | `04-transformada-z-y-mapeo.md` | $G_{h1}(s)$, comparación con ZOH y por qué casi no se usa en la práctica |
| Transformación bilineal | #24, #48, nunca aparecía pese a estar en el temario de Unidad 1 | `04-transformada-z-y-mapeo.md` | Derivación desde la regla trapezoidal, propiedad de preservar estabilidad, *frequency warping*, ejercicio comparando contra el mapeo exacto ($z=e^{Ts}$) sobre la misma planta del ejercicio de ZOH |
| Sintonización del PID | #21, objetivo declarado de la Unidad 3, nunca aparecía | `05-pid-y-control-on-off.md` | Ziegler-Nichols (curva de reacción y ganancia última), con tablas y un ejemplo numérico cada uno, más el problema del *windup* y anti-windup por *clamping* |
| Margen de fase | #47, nunca aparecía | `09-error-estacionario-y-estabilidad.md` | Definición, comparación con MG, ejemplo sobre el mismo sistema ilustrativo de la figura de MG (mismo $K$, los dos márgenes dan negativo — se verifica que concuerdan), rangos típicos de diseño |
| Criterio de Jury | #46, #48, Routh se aplicaba a sistemas discretos sin justificar por qué | `09-error-estacionario-y-estabilidad.md` | Por qué Routh solo no alcanza, los dos caminos válidos (bilineal+Routh vs. Jury directo), tabla general, caso particular $n=2$ con ejemplo (reutilizando el denominador $z^2-1.6z+0.8$ ya usado en otro capítulo) |

La figura `margen_ganancia.svg`/`.py` (`apoyo/figuras/frecuencia.py`) se
extendió para marcar **ambos** márgenes sobre el mismo diagrama de Bode
— se reutiliza una sola figura entre las dos secciones en vez de duplicar
el gráfico.

## Correcciones pedidas en `pendiente.txt` (2026-09-15)

El usuario dejó un archivo `pendiente.txt` en la raíz del proyecto con
feedback puntual de lectura. Se resolvió todo lo pedido ahí:

1. **Capítulo 1 muy resumido** — se agregaron definiciones (sistema,
   referencia, error, perturbación, sensor/transductor, actuador) y se
   profundizaron las que ya estaban, cada una con ejemplo concreto. Se
   agregó también un ejemplo de modelo matemático (masa-amortiguador) que
   ahora se reutiliza como hilo conductor en el capítulo 2.
2. **Capítulo 2, definir polo/cero con ejemplos y mostrar ecuaciones
   diferenciales** — se agregó una sección "Por qué hace falta esto" que
   parte de la ecuación diferencial del capítulo 1 y llega a la función de
   transferencia, y se amplió "Polos y ceros" con la interpretación física
   (frecuencias naturales / peso de cada modo) y dos ejemplos.
3. **Figura 1.2 (línea que llega a H por arriba)** — corregido en
   `bloques_schemdraw.py`: las dos funciones con bloque de realimentación
   (`lazo_realimentado`, `lazo_laplace`) ahora bajan en el aire y entran
   horizontal al bloque (H o A), no verticalmente. Aplicado también a
   `lazo_laplace_sd` (bloque `A(s)`), que tenía el mismo problema aunque no
   se mencionó explícitamente.
4. **Explicar mejor la tabla de estabilidad de 2.1.2** — agregada la
   deducción completa desde $e^{s_i t}=e^{\sigma t}(\cos\omega t + j\,\mathrm{sen}\,\omega t)$,
   mostrando por qué la parte real es la que decide estable/inestable/marginal,
   y por qué un polo o cero en el origen equivale a integrar/derivar.
5. **Desarrollar el ejemplo de MATLAB de 2.1.4** — se explica qué hace
   `feedback` (automatiza el $F=G/(1+GH)$ del capítulo 1), por qué existe
   (evitar álgebra de polinomios a mano), y se agregó un ejemplo numérico
   completo armando el lazo, chequeando estabilidad con `roots()` y
   graficando con `step()`.

No se tocó el resto de los capítulos ni el `.zip` de la raíz de
`proyectos/` (es el resultado de la digitalización original, base de todo
este trabajo — no es un archivo de esta carpeta para editar).

## Capítulos 12-13: complementos a partir de una evaluación del curso (2026-09-15)

Se le pidió a Claude una evaluación honesta del curso completo (qué le
falta, qué falta profundizar, con foco en el repaso de control análogo) y
después que la desarrollara — con **Python en vez de MATLAB** para todo
lo nuevo (librería [`control`](https://pypi.org/project/control/),
instalada en `~/.venvs/apuntes_control`).

Dos capítulos nuevos, no ligados a ninguna página del cuaderno:

- **`12-tecnicas-clasicas-de-diseno.md`** — lugar de las raíces (con
  ejercicio de diseño: elegir $K$ para $\zeta$ objetivo), criterio de
  Nyquist (verificado sobre el mismo sistema ilustrativo ya usado en
  margen de ganancia/fase — coincide: también da inestable), y diseño de
  compensador de adelanto paso a paso (de $MF=8.9°$ a $MF=41°$ sobre
  $G(s)=20/[s(s+1)(s+5)]$).
- **`13-complementos-digitales.md`** — PID discreto (ecuación en
  diferencias, forma posicional e incremental, simulación completa del
  lazo), control *dead-beat* (diseño completo sobre $G(z)=0.5/(z-0.5)$,
  llega exacto a la referencia en 1 muestra), y las dos limitaciones
  físicas del muestreo que Nyquist no cubre (antialiasing, cuantización
  con la fórmula $\text{SNR}\approx 6.02n+1.76\,\text{dB}$).

Nuevos scripts de figuras: `apoyo/figuras/diseno.py` (lugar de raíces,
Nyquist, Bode antes/después del compensador) y
`apoyo/figuras/digital_complementos.py` (PID discreto, dead-beat,
cuantización) — ambos usan `control`, no solo `matplotlib`.

Todos los ejemplos numéricos se verificaron corriendo el código antes de
escribirlos en el texto (no se transcribieron cuentas a mano) — en
particular el compensador de adelanto necesitó tres iteraciones para
encontrar un $\phi_{max}$ de diseño que diera un resultado honesto (no se
fuerza a que "cierre perfecto", se documenta que el margen real quedó por
debajo del objetivo y por qué).

**Pendiente para quien continúe**: el `README.md` y el índice de
`pendiente.txt` no mencionaban estos capítulos — ya actualizado el primero
(tabla de contenido + dependencia de `control`), pero si aparece feedback
nuevo sobre 12-13 en un `pendiente.txt` futuro, tratarlos como cualquier
otro capítulo.

## Capítulos 14-16: del papel al hardware (segunda revisión)

Pedido textual: *"piensa en un estudiante que quiere aprender sistemas de
control y desea entender de qué trata y cómo usarla para por medio de
electrónica conocer los sistemas ya sea mecánico, químico, eléctrico y
poder medir sus entradas y salidas y poder moldear su comportamiento (...)
complementa temas, propón ejercicios nuevos, da el porqué"*.

### El diagnóstico

Leyendo el curso completo con esa pregunta en la mano, el hueco no era de
teoría — era que **todo el material parte de una $G(s)$ ya dada**. El
único modelado presente es el circuito RC del capítulo 3, y la
instrumentación no aparece en ningún lado: el controlador "mide $y$" y
"aplica $u$" como si esas dos flechas fueran gratis. Un estudiante podía
terminar el curso sabiendo diseñar un PID y sin poder controlar nada real,
porque le faltaban los dos extremos de la cadena.

### Lo que se agregó

| Capítulo | Qué cubre | Por qué faltaba |
|---|---|---|
| 14 — Modelado de sistemas físicos | método de 4 pasos, los 4 dominios (eléctrico/térmico/fluidos/mecánico) reducidos a la misma $K/(\tau s+1)$, motor DC completo con la fem como lazo interno, linealización en el punto de operación | sin esto no hay forma de conseguir la $G(s)$ del sistema propio |
| 15 — Cadena de instrumentación | sensores por variable, 4-20 mA, resolución del encoder, acondicionamiento y bits útiles del ADC, filtro EMA y su costo en margen de fase, PWM como DAC, saturación y zona muerta del driver, criterio real para elegir $T$ | el lazo físico controla planta **más** electrónica, y eso cambia la estabilidad |
| 16 — Proyecto integrador | identificación experimental por `curve_fit`, elección justificada de $T$, diseño del PI por cancelación de polo, el `for` que corre en el micro, verificación con cuantización y saturación puestas | cierra el ciclo completo una sola vez, de punta a punta |

Se agregaron **15 ejercicios nuevos** (5 por capítulo) con sus respuestas
desarrolladas, todos numéricos y del tipo "elegí un componente y
justificá con un número", que es la habilidad que el curso no ejercitaba.

### La tabla de analogías entre dominios

El aporte conceptual más rentable del capítulo 14: los cuatro dominios
comparten estructura (algo que acumula + algo que disipa $\Rightarrow$
$\tau = RC$). Aprender a modelar uno alcanza para los cuatro, y la
intuición del capacitor cargándose sirve igual para un horno. Es la
respuesta directa a *"mecánico, químico, eléctrico"* del pedido.

### El hallazgo pedagógico del capítulo 16

Al simular el lazo completo con la cuantización del encoder puesta, el
error final se estanca en $\approx 0.25$ rad/s. Buscando por qué, resultó
ser **medio paso de cuantización del encoder** ($0.628/2 = 0.314$). No fue
un resultado buscado — salió de la simulación — y se convirtió en la
conclusión del capítulo: *la precisión de un lazo está acotada por la de
su sensor, no por lo bueno que sea el controlador*. Es el argumento que
justifica haber escrito los capítulos 14 y 15.

### Figuras nuevas

`motor_dc_sd` y `cadena_instrumentacion_sd` (schemdraw, en
`bloques_schemdraw.py`) más cinco de matplotlib en un archivo nuevo,
`apoyo/figuras/practica.py`: `linealizacion`, `pwm`, `filtro_ema`,
`identificacion_motor`, `proyecto_lazo`.

Dos problemas durante el armado, por si reaparecen:

- Las funciones nuevas quedaron **después** del bloque
  `if __name__ == '__main__'` de `bloques_schemdraw.py` y daban `NameError`
  al invocarse. El bloque main tiene que quedar siempre al final del
  archivo.
- El lazo de realimentación de `cadena_instrumentacion` no cerraba
  visualmente (la flecha subía a la nada). Se resolvió ruteando explícito:
  izquierda desde el acondicionador, arriba hasta la altura de la planta
  (`.toy(P.W)`), y recién ahí la flecha a la derecha (`.tox(P.W)`).

### Verificación numérica

Como en los capítulos 12-13, **ningún número se escribió sin correrlo
antes**. Los valores que quedaron fijados como constantes del hilo
conductor:

| Magnitud | Valor | De dónde sale |
|---|---|---|
| $K$ del motor | 22.07 (rad/s)/V | $K_t/(R_ab+K_tK_e)$ con la hoja de datos del cap. 14 |
| $\tau$ del motor | 14.71 ms | $R_aJ/(R_ab+K_tK_e)$ |
| $T$ de muestreo | 5 ms | compromiso entre $\tau/10$ y la resolución del encoder |
| Resolución del encoder | 0.628 rad/s | $2\pi/(4\cdot500\cdot0.005)$ |
| PI | $K_p=0.0294$, $K_i=2.0$ | cancelación de polo, $K_p=K_i\tau$ |
| Resultado del lazo | $t_s=75$ ms, 0 % sobrepaso, $u_{max}=7.43$ V | simulación con cuantización y saturación |
| Identificación | recupera $K$ con 0.0 % y $\tau$ con 1.1 % de error | `curve_fit` sobre el ensayo simulado con ruido |

La diferencia entre el $t_s$ teórico (91 ms, $4\tau_{lc}$) y el simulado
(75 ms) se dejó explícita en el texto en vez de maquillarla: entra a la
banda del 2 % antes de lo que predice la fórmula asintótica.

## Pendientes

- Transcribir las páginas siguientes (falta de la Unidad 1: retenedores de orden
  cero y uno en detalle, transformación bilineal; y toda la Unidad 2).
  *(Actualización: retenedores y bilineal ya se completaron como contenido
  complementario, ver sección de arriba — pero siguen sin transcribirse del
  cuaderno físico, si en algún momento aparecen esas páginas hay que
  cotejar contra lo que se agregó acá.)*
- Decidir si al final se arma un PDF único con todos los lotes o uno por archivo.
  *(Resuelto: se arma `libro-completo.pdf` con `apoyo/build.sh libro`, y se
  mantienen también los PDFs individuales por clase en `pdf/`.)*

- **Prácticas de MATLAB de la clase** (pendiente, sesión futura). Los `.m`
  aparecieron en Nextcloud el 15-09-2026, en
  `~/Nextcloud/salvar/control_digital/` (no en una carpeta "sistemas de
  control" — de ahí que la primera búsqueda no diera nada). Contenido
  inventariado más abajo. Plan:
  1. leer qué hace cada `.m` y asignarlo a un capítulo según la tabla de
     abajo;
  2. escribir el equivalente en Python con `control`;
  3. **correrlo y comparar** contra el resultado esperado del `.m`;
  4. insertarlo como sección de práctica del capítulo.

  **Decisión del autor: en los apuntes va solo la traducción a Python**,
  no el código MATLAB original a dos columnas. El repo es material de
  aprendizaje con herramientas libres, y duplicar cada ejemplo en dos
  lenguajes duplica también la superficie de errores y el mantenimiento.
  Los `.m` originales, si se quieren conservar, van fuera de `apuntes/`.

  | Lo que hace el `.m` | Capítulo destino |
  |---|---|
  | `tf`, `zpk`, `pzmap`, `step`, `impulse` continuos | 02 |
  | `bode`, `margin` sobre planta continua | 03 |
  | `c2d`, `d2c`, `zgrid`, mapeo s→z | 04 y 11 |
  | PID, Ziegler-Nichols, on-off | 05 |
  | polo dominante, $t_s$/$t_p$/$M_p$ en z | 06 |
  | ajuste de respuesta al escalón, reducción de orden | 07 |
  | práctica del motor, divisor de tensión | 08 |
  | `dcgain`, error estacionario, Routh, Jury | 09 |
  | `rlocus`, `nyquist`, `sisotool`, adelanto/atraso | 12 |
  | PID en diferencias, dead-beat, cuantización | 13 |
  | modelado de motor/tanque/horno, linealización | 14 |
  | lectura de ADC/encoder, filtrado, PWM | 15 |
  | simulación de lazo completo con saturación | 16 |

### Procesado: el informe del motor (capítulo 08)

De la carpeta `control_digital/` se procesó primero `informe_control/`, el
informe IEEE *"Identificación y discretización de modelo de un motor DC"*
(E. Amado Suárez, W. Serrano, M. Gómez — UTS Bucaramanga, oct-2018), que
resultó ser la versión desarrollada de la práctica ya transcrita en el
capítulo 08. Por eso se agregó ahí y no como capítulo nuevo: el cuaderno
tenía el divisor de tensión sin explicar para qué, y el informe lo cierra.

**Decisión de alcance**: la subcarpeta `matlab varios/` quedó **fuera** —
son `.m` de otras materias (robótica 3DOF, convolución de imágenes en
Octave, GUIs, rectificador con tiristores). Solo se toma lo que está en la
raíz de `control_digital/`. El único borderline es `filtro.m`
(`c2d(10(s+2)/s, 0.004, 'tustin')`), que sí es control y podría ir al
capítulo 11 o 13 si en algún momento se quiere.

**Lo verificado corriendo el código** (ninguna cuenta se copió del
informe sin comprobarla):

| Cantidad | Informe | Verificado | Estado |
|---|---|---|---|
| Ganancia de DC | 3345.89 | 3345.89 | coincide |
| Polos en $z$ ($T=1$ s) | $z^2-1.671458z+0.77383$ | $z^2-1.671456z+0.773832$ | coincide |
| Cero en $z$ | 0.9043 | 0.904295 | coincide |
| Ganancia $k_d$ | **1797.06** | **1789.56** | **error del 0.42 % en el informe** |

El $k_d$ se recalculó de dos maneras (con los polos exactos y con los
valores redondeados que el propio informe imprime) y las dos dan 1789.5,
así que el error es del informe, no del redondeo. Se documentó como
corrección explícita en el capítulo, junto con otras dos: el pie de figura
dice "respuesta al impulso" cuando la gráfica es al escalón, y las RPM
están fuera de escala (70 000 RPM medidos, ~29 000 implícitos en la
ganancia — casi seguro que falta dividir por el número de ranuras del
disco del sensor óptico).

**El hallazgo pedagógico**: el modelo tiene $\zeta=0.3745$, que por la
fórmula del capítulo 6 predice 28 % de sobrepaso, pero la respuesta real
sobrepasa **174 %**. La causa es el cero en $s=-0.1006$, que está a
$0.29\,\omega_n$ — más cerca del origen que los polos. Quitando el cero y
manteniendo la ganancia de DC, el sobrepaso vuelve a 28 % exacto. Quedó
como advertencia de que $M_p(\zeta)$ solo vale para segundo orden sin
ceros.

**Diferencia entre herramientas que vale la pena recordar**: en la
correspondencia de polos y ceros, el `c2d(...,'matched')` de MATLAB agrega
$(z+1)^{n-m}$ y `ct.sample_system(...,method='matched')` de
`python-control` agrega $(z+1)^{n-m-1}$. Misma ganancia de DC, polos
idénticos, numeradores distintos: MATLAB deja grado relativo 0 y Python
grado relativo 1. Ninguna es incorrecta, pero al traducir un `.m` hay que
saberlo o los números no cuadran.

Figuras nuevas en `apoyo/figuras/informe_motor.py`:
`informe_motor_respuesta` (escalón continuo vs discreto, reproduce la
figura del informe) e `informe_motor_mapeo` (los polos y el cero llevados
de $s$ a $z$).

**Tropezón de compilación, por tercera vez**: `\,\%` dentro de modo
matemático rompe XeLaTeX con babel español ("Incompatible glue units"),
porque babel ya espacia el `%`. Se corrigió con
`sed -i 's/\\,\\%/\\%/g' apuntes/*.md`. **Conviene no volver a escribir
`\,\%` nunca**. En la misma pasada se cambiaron los `~` sueltos delante de
un número (`~8.8 V`) por "unos 8.8 V", porque en LaTeX el `~` es un
espacio duro y no se ve.

### Procesado: los scripts de clase (capítulos 02 y 05)

Traducidos los cuatro archivos que quedaban en la raíz de
`control_digital/`. Solo va la versión Python, según lo decidido.

| Original | Qué era | Dónde quedó |
|---|---|---|
| `clase1.m` | $G=s/[(s+2)(s^2+s+8)]$ + `ltiview` | cap. 02 — el cero en el origen |
| `clase3` y `clase3.m` | `ilaplace` de $1/[s(s^2+4)]$ y $1/[s(s^2-s+4)]$ | cap. 02 — verificación con `sympy` |
| `clase2.m` | PID con $K=386$, $T_i=900$, $T_d=1000$ | cap. 05 — crítica de la sintonía |
| `clase4.slx` | Simulink: `Relay` + `Random Number` + `Manual Switch` | cap. 05 — on-off con ruido |

**Los dos `clase3` ya estaban en el cuaderno.** Son los ejercicios "Tarea —
polos en el semiplano derecho" y "Segundo ejercicio — polos sobre el eje
imaginario", resueltos a mano por fracciones parciales; los `.m` eran la
comprobación en MATLAB. Así que el aporte no es contenido nuevo sino la
verificación con `sympy` y una figura que pone los dos casos juntos: los
scripts difieren en **un solo signo** ($s^2+4$ contra $s^2-s+4$) y eso
separa la oscilación sostenida de la divergente. Se agregó `sympy` al venv.

**`clase1.m` sí era contenido nuevo** y resultó el más didáctico de los
cuatro: un cero en el origen anula la ganancia de DC ($G(0)=0$), así que
la respuesta al escalón sube a 0.09, oscila y **vuelve a cero** aunque los
polos sean perfectamente estables. Sirve para decir algo que el curso no
decía: una planta con cero en el origen no se puede llevar a una
referencia constante distinta de cero por realimentación unitaria.

**`clase2.m` fue el hallazgo.** Las ganancias parecían de tanteo y lo son,
pero lo interesante es *cómo* se demuestra. Verificado corriendo el código:

| | valor |
|---|---|
| Polos de lazo cerrado | $-386\,000$ y $-0.000507\pm0.000924j$ |
| Estable | sí, y con error estacionario cero |
| $t_s$ al 2 % | nunca sale de la banda |
| $t_s$ al 0.5 % | **2053 s = 34 min** |
| $t_s$ al 0.1 % | 5301 s = 1.5 h |
| $K_d = K\,T_d$ | **386 000** |
| $\lvert U/N\rvert$ a 100 rad/s | 9990 |

O sea: el lazo *es* estable y en una simulación de seis segundos se ve
impecable. Lo que está mal es que los polos están separados por nueve
órdenes de magnitud. Se documentó con dos paneles —los primeros 6 s y la
cola lenta en minutos— porque el contraste entre "parece perfecto" y
"tarda media hora" es justamente la lección.

Se agregó una sintonía diseñada por ubicación de polos ($K_p=22$,
$K_i=59$, $K_d=7.5$, o $K=22$, $T_i=0.373$, $T_d=0.341$) que da
$M_p=10.9\,\%$ y $t_s=1.43$ s, y de paso la **derivada filtrada**
($T_ds \to T_ds/(1+T_ds/N)$, $N=10$), que baja el pico de $\lvert U/N\rvert$
de 75 000 a 242 a cambio de 7 puntos de sobrepaso. Ese tema no estaba en
ningún lado del curso y es cómo se implementa un PID de verdad.

**Rendimiento inesperado de Routh**: con control proporcional sobre esta
planta, la condición de Routh se reduce a $3(10+K) > 16+3K$, o sea
$14 > 0$ — **se cumple para todo $K$**. Pero $\zeta$ cae de 0.151 ($K=1$) a
0.0009 ($K=386$). Y el centroide de las asíntotas del lugar de las raíces
da exactamente 0, así que la asíntota *es* el eje imaginario: las ramas se
le acercan sin cruzarlo. Los tres resultados dicen lo mismo desde tres
lados distintos, y juntos son el mejor argumento de que Routh contesta
sí-o-no, no "qué tan bien".

**`clase4.slx`** no se puede leer en detalle (es binario), pero la lista de
bloques alcanzó: `Relay` + `Random Number` + `Manual Switch` = el
experimento era ver qué le hace el ruido a un on-off. Simulado en Python:
43 conmutaciones/s sin histéresis contra 9 con $\Delta=1.5$, a cambio de
que el rizado suba de 2.8 a 4.9. El capítulo ya tenía la histéresis pero
justificada solo como "para que no conmute todo el tiempo"; con ruido el
argumento es mucho más fuerte y se puede cuantificar.

Figuras nuevas en `apoyo/figuras/clases_matlab.py`: `clase1_cero_origen`,
`clase3_estabilidad`, `clase2_pid`, `clase4_onoff_ruido`. Más 10
ejercicios nuevos con respuestas (5 en cada capítulo).

**Nota de armado de figuras**: dos de las cuatro hubo que rehacerlas
porque la primera versión no mostraba nada. En `clase2_pid` el panel
derecho a escala de horas se veía como una línea recta en 1.0 (la cola
lenta tiene amplitud chica) — se arregló haciendo zoom vertical a
0.985–1.004. En `clase4_onoff_ruido` el gráfico de $u(t)$ sobre 30 s era un
rectángulo negro sólido — se arregló mostrando una ventana ampliada de 4 s.
Conviene recordarlo: **si el fenómeno es de amplitud chica o de frecuencia
alta, hay que hacer zoom o la figura no dice nada.**

### Nueva carpeta: `practicas_matlab/` — original junto al equivalente

Pedido del usuario: *"tenemos ya código en matlab, puedes también sacar
el equivalente en Python y dejarlo junto al de matlab, el que está en
Python déjalo quieto."* Es un pedido distinto del anterior: no se toca el
Python ya narrado dentro de los capítulos 02, 05 y 08 — se crea una
carpeta nueva con **el `.m`/`.slx` original copiado** y, al lado, un
`.py` con la traducción directa (sin narrativa pedagógica, solo
código-a-código).

Copiados desde `~/Nextcloud/salvar/control_digital/` (raíz, mismo alcance
que antes — `matlab varios/` sigue fuera): `clase1.m`, `clase2.m`,
`clase3`, `clase3.m`, `clase4.slx`.

**Hallazgo al decodificar `clase4.slx`.** La vez anterior solo se había
leído la lista de tipos de bloque del XML (`BlockType=...`), sin sus
parámetros ni las conexiones (`<Line>`/`<Branch>`). Esta vez se parseó el
`simulink/blockdiagram.xml` completo (el `.slx` es un zip) y salieron tres
cosas que cambian la lectura del modelo:

1. La planta es explícita: `sys = tf(1,[1 1])`, o sea $1/(s+1)$ — no era
   necesario suponerla.
2. El segundo puerto del bloque `Sum` **no está cableado** (solo hay una
   línea a `3#in:1`, ninguna a `3#in:2`, a pesar de que el bloque pide dos
   entradas). El modelo tal como está guardado es **lazo abierto**: no hay
   comparación con una referencia ni realimentación. El `ManualSwitch`
   elige entre alimentar el `Relay` con el `Step` o con el `Random
   Number`, no entre "referencia limpia" y "referencia con ruido" como se
   había asumido.
3. El `Relay` no tiene parámetros propios en el XML, así que usa los
   valores por defecto de Simulink: umbral de encendido = umbral de
   apagado = 1. Verificado en Python: con el `Step` por defecto
   (`StepTime=1`, `Final=1`) la señal se queda parada **exactamente** en
   el umbral, y el relé entra en *chattering* — conmuta en cada paso de
   simulación porque nunca cruza el umbral, solo lo toca. Con la rama de
   `Random Number` (Mean=0, Variance=1, Ts=0.1 s — este último sí explícito
   en el XML) el relé conmuta con normalidad, 12 veces en 6 s.

**Esto es más preciso que lo que sostiene la figura `clase4_onoff_ruido.svg`
del capítulo 05** (un lazo cerrado con ruido aditivo en la medida y una
histéresis $\pm\Delta$, hecho como ilustración general del concepto de
on-off con ruido, antes de haber decodificado el `.slx` a este nivel de
detalle). Seguí las instrucciones del usuario y **no toqué esa figura ni
el capítulo** — el hallazgo queda documentado acá y en el `README.md` de
`practicas_matlab/`, no reescrito en el libro. Si en algún momento se
quiere corregir el capítulo 05 para reflejar la topología real, ya está
todo el análisis hecho.

Los `clase3` (sin extensión) y `clase3.m` dieron dos archivos Python
separados, `clase3a.py` y `clase3b.py`, porque ambos comparten el nombre
base "clase3" y no pueden convivir como un solo `.py`.

Todo corrido y verificado antes de dejarlo: `clase1.py`/`clase2.py`
reproducen exactamente los polos y ganancias ya verificados en el
capítulo 02/05; `clase3a.py`/`clase3b.py` dan la misma antitransformada
que `sympy` calculó antes; `clase4.py` se corrió y se graficó para
confirmar visualmente el *chattering* y la conmutación normal con ruido.
