# Discretización con distintos periodos de muestreo

*Transcripción de las páginas 50–55 del cuaderno.*

Se repite el mismo mapeo $s \to z$ del capítulo 4 sobre varios sistemas y con
distintos valores de $T$, para ver cómo se mueven los polos y cómo cambia la
ganancia $K$ que ajusta el modelo discreto.

## Caso 1 — $T = 0.1$

Polos del sistema continuo:

$$
s_1 = -49.375
\qquad
s_{2,3} = -37.81 \pm 52.27j
$$

Mapeo con $z_i = e^{T s_i}$:

$$
z_1 = 0.00717
$$

$$
z_{2,3} = e^{\,0.1\,(-37.81 \pm 52.27j)}
= e^{-3.781}\,e^{\pm 5.227j}
$$

$$
= e^{-3.781}\left(\cos 5.227 + j\operatorname{sen}5.227\right)
$$

$$
z_{2,3} = 0.01122 \pm (-0.0198j)
$$

Reconstruyendo el binomio del par complejo:

$$
z^2 - 2\,(0.01122)\,z + 0.01122^2 + 0.0198^2
$$

$$
z^2 - 0.02244\,z + 0.000517
$$

$$
\frac{K\,(z+1)^2}{z^2 - 0.02244\,z + 0.000517}
$$

$$
4K = 1
\qquad\Longrightarrow\qquad
K = 0.2445
$$

## Caso 2 — $T = 0.001$

Los mismos polos continuos:

$$
s_1 = -49.375
\qquad
s_2 = -37.81 \pm 52.27j
$$

$$
z_1 = e^{\,-0.001 \times 49.375} = 0.9518
$$

$$
z_{2,3} = e^{\,0.001\,(-37.81 \pm 52.27j)}
= e^{-0.03781}\,e^{\pm 0.05227i}
$$

$$
= e^{-0.03781}\left(\cos 0.05227 \pm j\operatorname{sen}0.05227\right)
$$

$$
z_{2,3} = 0.9615 \pm j\,0.0503
$$

$$
z^2 - 2\,(0.9615)\,z + 0.9615^2 + 0.0503^2
\qquad\Longrightarrow\qquad
z^2 - 1.923\,z + 0.927
$$

$$
\frac{K\,(z+1)^2}{(z - 0.9518)\,(z^2 - 1.923\,z + 0.927)} = 20\,746.68
$$

$$
K = 4.82 \times 10^{-5}
$$

Con $T$ mil veces menor los tres polos se pegan al punto $z = 1$: el polo real
pasa de $0.007$ a $0.95$ y el par complejo de $0.011$ a $0.96$.

---

## Caso 3 — sistema con retardo

$$
\frac{3898\,(s + 0.1006)}{s^2 + 0.2564\,s + 0.1172}
$$

$$
s_{1} = -0.1282 \pm 0.3174j
\quad\Longrightarrow\quad
s^2 - 0.2564\,s + 0.11778
$$

El cero real se mapea directo:

$$
z - e^{-0.1006} \;\longrightarrow\; z - 0.904
$$

Y el par de polos:

$$
\left(s + (0.1282 - 0.3174j)\right)\left(s - (0.1282 + 0.3174j)\right)
$$

$$
\left(z - e^{-0.1282 - 0.3174j}\right)\left(z - e^{-0.1282 + 0.3174j}\right)
$$

$$
e^{-0.1282 - 0.3174j} = e^{-0.1282}\cdot e^{-0.3174j}
= e^{-0.1282}\left(\cos(-0.3174) - \operatorname{sen}(-0.3174)\right)
$$

$$
= 0.83529 \pm 0.27457
$$

$$
\frac{z - 0.904}{z^2 - 1.671458\,z + 0.77363}
$$

### El retardo

$$
e^{-4.4 s}
\quad\Longrightarrow\quad
f(t - t_0)\,u(t - t_0) = e^{-t_0 s}
$$

$$
f(t)\cdot u(t - 4.4)
\qquad\Longrightarrow\qquad
z^{-4.4}
$$

Constante derivativa anotada en la hoja siguiente:

$$
K_d = 3594.112
$$

---

## Caso 4 — controlador de tercer orden, $T = 0.1$

$$
G_c(s) = \frac{205\,500}{s^3 + 125\,s^2 + 7896\,s + 205\,500}
$$

Equivalencias usadas:

$$
s + a \;\longrightarrow\; \left(z - e^{-aT}\right)
\qquad
s + b \;\longrightarrow\; \left(z - e^{-bT}\right)
$$

$$
K'_c = \frac{K\,z\left(1 - e^{-pT}\right)}{p\left(1 - e^{-zT}\right)}
\qquad
G_c(z) = K'_c\,\frac{z - e^{-zT}}{z - e^{-pT}}
$$

### Polos

$$
s_1 = -2.613
\qquad
s_{2,3} = -61.1935 \pm 273.68j
$$

$$
z_1 = e^{\,0.1 \times (-2.613)} = 0.77
$$

$$
z_{2,3} = e^{\,0.1\,(-61.1935 \pm 273.68j)}
= e^{-6.11935}\,e^{\pm 27.368j}
$$

$$
z_{2,3} = 2.2\times10^{-3}\left(\cos 27.368 \pm j\operatorname{sen}27.368\right)
$$

$$
z_{2,3} = -0.00135 \pm 0.00173j
$$

### Ceros en el infinito y ganancia

$$
r = 3 - 0 = 3
\qquad\Longrightarrow\qquad
(z+1)^2
$$

$$
G(z) = \frac{K\,(z+1)^2}
{(z - 1.3)\,(z - 0.00135)\,(z + 0.00173)}
$$

El par complejo se junta en un binomio:

$$
z^2 + z\,(0.00173 - 0.00135) + 2.33\times10^{-6}
$$

$$
1 = \frac{K\,(z+1)^2}{z^2 + 380\times10^{-6}\,z + 2.33\times10^{-6}}
$$

$$
1 = \frac{4K}{1}
\qquad\Longrightarrow\qquad
K = \tfrac{1}{4}
$$

$$
\boxed{\;
G(z) = \frac{0.25\,(z+1)^2}
{(z - 1.3)\left(z^2 + 360\times10^{-6}\,z + 2.33\times10^{-6}\right)}
\;}
$$
