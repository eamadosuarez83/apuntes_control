# Error en estado estable y criterios de estabilidad

*Transcripción de las páginas 42–47 del cuaderno.*

## Control proporcional

![Lazo con control proporcional](../apoyo/figuras/lazo_proporcional_sd.svg)

Forma general de la planta, con $r$ integradores explícitos:

$$
G(s) = \frac{b_0 s^{m} + b_1 s^{m-1} + \cdots + b_m}
{s^{\,r}\left(a_0 s^{n} + a_1 s^{n-1} + \cdots + a_n\right)}
$$

De acuerdo al error, la acción proporcional actúa.

### Entrada escalón

$$
R(s) = \frac{1}{s}
$$

$$
\frac{E(s)}{R(s)} = \frac{1}{1 + K\,G(s)} = T(s)
\qquad
K_p = K\,G(s)
$$

$$
\begin{aligned}
E_{ss} &= \lim_{s \to 0} s\,E(s) = \lim_{s \to 0} s\,T(s)\,R(s) \\[4pt]
E_{ss} &= \lim_{s \to 0} s\,\frac{1}{s}\,\frac{1}{1 + K\,G(s)} \\[4pt]
E_{ss} &= \lim_{s \to 0} \frac{1}{1 + K_p}
\end{aligned}
$$

Despejando la ganancia:

$$
(1 + K_p)\,E_{ss} = 1
\qquad
1 + K_p = \frac{1}{E_{ss}}
\qquad
\boxed{\;K_p = \frac{1}{E_{ss}} - 1\;}
$$

$K_p$ es la **ganancia de error de posición**:

$$
K_p = \lim_{s \to 0} K\,G(s)
$$

| $r$ | $K_p$ | $E_{ss}$ |
|---|---|---|
| 0 | $\dfrac{K\,b_m}{a_n}$ | $\dfrac{1}{1+K_p}$ |
| $r \geq 1$ | $\infty$ | 0 |

El cuaderno dibuja las dos respuestas: con $r = 0$ la salida se queda a una
distancia $E_{ss}$ de la referencia; con $r \geq 1$ la alcanza.

### Entrada rampa

$$
R(s) = \frac{1}{s^2}
$$

$$
E_{ss} = \lim_{s \to 0} s\,T(s)\,R(s)
= \lim_{s \to 0} s\,\frac{1}{s^2}\,\frac{1}{1 + K\,G(s)}
$$

$K_v$ es la **constante de error de velocidad**:

$$
K_v = \lim_{s \to 0} s\,K\,G(s)
$$

| $r$ | $K_v$ | $E_{ss}$ |
|---|---|---|
| 0 | 0 | $\infty$ |
| 1 | $\dfrac{K\,b_m}{a_n}$ | $\dfrac{1}{K_v}$ |
| $r \geq 2$ | $\infty$ | 0 |

---

## Caso discreto

### Entrada escalón

$$
E_{ss} = \frac{1}{1 + K_p}
\qquad\Longrightarrow\qquad
K_p = \lim_{s \to 0} K\,G(s) = \lim_{z \to 1} K\,G(z)
$$

### Entrada rampa

$$
E_{ss} = \frac{1}{K_v}
\qquad
K_v = \lim_{s \to 0} s\,K\,G(s)
= \lim_{z \to 1}\left(\frac{z-1}{z}\right)\frac{1}{T}\,K\,G(z)
$$

---

## Margen de ganancia

La ganancia máxima a la que el sistema puede trabajar.

$$
MG = -6\;\text{dB}
$$

Es el punto o valor en frecuencia donde la fase vale $180°$.

![Margen de ganancia sobre el diagrama de Bode](../apoyo/figuras/margen_ganancia.svg)

Ganancia crítica:

$$
\boxed{\;K_{max} = 10^{\,MG/20}\;}
$$

### Ejemplo

$$
E_{ss} = 0.05 \;\longrightarrow\; 5\%
$$

$$
K_p = \frac{1}{0.05} - 1 = 19
$$

$$
K = \frac{K_p}{\lim\limits_{s \to 0} G(s)}
= \frac{K_p}{\lim\limits_{z \to 1} G(z)}
$$

Con la planta

$$
G(z) = \frac{z^2 + z + 0.5}{z^3 + 32z^2 + 4z + 0.2}
$$

$$
\lim_{z \to 1} G(z) = \frac{2.5}{37.2} = 0.0672
$$

$$
K = \frac{19}{0.0672} = 282.73
$$

---

## Control integral

![Lazo con control integral en discreto](../apoyo/figuras/lazo_integral_z_sd.svg)

$$
E_{ss} = \frac{1}{K_v} = 0.5
$$

$$
K_v = \lim_{s \to 0} K\,s\,G(s)
= \lim_{z \to 1}\left(\frac{z-1}{z}\right)\frac{1}{T}\,K\,\frac{z}{z-1}\,G(z)
$$

---

## Criterio de Routh

Permite determinar la cantidad de polos en lazo cerrado que se encuentran en
el semiplano derecho del plano $s$, **sin factorizar el polinomio**.

Procedimiento:

1. Se escribe el polinomio característico (el denominador).
2. Ver que todos los coeficientes sean positivos y que todos los coeficientes
   estén presentes.
3. Se acomodan los coeficientes en filas y columnas.

$$
\frac{C(s)}{R(s)} =
\frac{b_0 s^{m} + b_1 s^{m-1} + \cdots + b_{m-1}s + b_m}
{a_0 s^{n} + a_1 s^{n-1} + \cdots + a_{n-1}s + a_n}
$$

La tabla:

| | | | | |
|---|---|---|---|---|
| $s^{n}$ | $a_0$ | $a_2$ | $a_4$ | $a_6 \;\cdots$ |
| $s^{n-1}$ | $a_1$ | $a_3$ | $a_5$ | $a_7 \;\cdots$ |
| $s^{n-2}$ | $b_1$ | $b_2$ | $b_3$ | $b_4$ |
| $s^{n-3}$ | $c_1$ | $c_2$ | $c_3$ | $c_4$ |
| $\vdots$ | | | | |

El número total de filas es $n + 1$.
