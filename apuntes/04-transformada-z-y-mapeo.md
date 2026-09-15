# Transformada Z y mapeo de polos y ceros

*Transcripción de las páginas 23, 24 y 27–30 del cuaderno.*

## Transformada Z

$$
H(z) = \frac{Y(z)}{X(z)}
$$

La señal continua se toma muestreada:

$$
x(t) \;\longrightarrow\; x(kT)
\qquad (T: \text{periodo de muestreo})
$$

### Estabilidad

El semiplano izquierdo del plano $s$ se corresponde con el interior del
círculo unitario del plano $z$, con

$$
z = r\,e^{j\omega}
$$

![Mapeo del plano s al plano z](../apoyo/figuras/mapeo_s_z.svg)

### Forma factorizada

$$
H(z) = \frac{b_0}{a_0}\, z^{\,N-M}\,
\frac{(z-z_1)(z-z_2)\cdots(z-z_n)}{(z-p_1)(z-p_2)\cdots(z-p_n)}
$$

- $M$ ceros: $z_1, z_2, \ldots, z_n$
- $N$ polos: $p_1, p_2, \ldots, p_n$
- Ganancia: $\dfrac{b_0}{a_0}$ — factor de amplificación, $K$

---

## Mapeo de polos y ceros

Relación entre un polo (o cero) del plano $s$ y su imagen en el plano $z$:

$$
z_i = e^{T s_i}
\qquad\Longleftrightarrow\qquad
s_i = \frac{1}{T}\ln z_i
$$

### Reglas, dada una función $G(s)$

1. Todo polo y cero (existente) de $G(s)$ se ve reflejado en el plano $z$ con
   la relación $z_i = e^{Ts_i}$.
2. Los **ceros en el infinito** de $G(s)$ se ven reflejados en el plano $z$ en
   $z_i = -1$. Si existieran $r$ ceros en el infinito, entonces hay
   $(z_i + 1)^{\,r-1}$ ceros en $G(z)$.
3. Si la planta $G(s)$ **no** presenta integrador, se debe cumplir:

$$
\lim_{s \to 0} G(s) = \lim_{z \to 1} G(z)
$$

   Si la planta **sí** presenta integrador:

$$
\lim_{s \to 0} s\,G(s)
= \lim_{z \to 1} \left(\frac{z-1}{z}\right)\frac{1}{T}\,G(z)
$$

Se define como ceros en el infinito a la diferencia entre el número de polos y
el número de ceros finitos de $G(s)$:

$$
r = n - m
\qquad
n = \#\,\text{polos}, \quad m = \#\,\text{ceros}
$$

---

## Ejercicio de mapeo

Código: `clase-control_mapeo.m`

De la gráfica se obtiene $\omega = 62.4$ rad/s, y de ahí el periodo de
muestreo:

$$
T = \frac{\pi}{624} = 5.03\;\text{ms}
$$

Con MATLAB se hallan los polos (figura 2, `pzmap(gf)`):

$$
s_1 = -62.8
\qquad
s_{2,3} = -31.4 \pm 54.4j
$$

### 1. Polos al plano $z$ con $z_i = e^{T s_i}$

$$
e^{(0.005)(-62.8)} = 0.7305
$$

$$
e^{(0.005)(-31.4 \pm 54.4j)} = e^{-0.157 \pm 0.272j}
$$

Pasando a rectangular:

$$
e^{-0.157}\left[\cos(0.272) + j\operatorname{sen}(0.272)\right]
= 0.8233 \pm 0.2296j
$$

### 2. Ceros en el infinito

$$
r = 3 - 0 = 3
\qquad\Longrightarrow\qquad
(z+1)^{\,r-1} = (z+1)^2
$$

### 3. Condición de ganancia

$$
\lim_{s \to 0} G(s) = \lim_{z \to 1} G(z) \;\longrightarrow\; K
$$

$$
G(z) = \frac{K\,(z+1)^2}
{(z - 0.7305)\,(z^2 - 1.6466z + 0.7305)}
$$

### Reconstruir el binomio a partir de un par complejo

$$
s^2 - 2\,\mathrm{Re}\,s + \mathrm{Re}^2 + \mathrm{Im}^2
$$

Ejemplo, para $-2 \pm 3j$:

$$
s^2 - 2(-2)\,s + (-2)^2 + (3)^2
= s^2 + 4s + 13
$$

### Cálculo de $K$

Imponiendo ganancia unitaria en continua:

$$
\lim_{s \to 0} = 1
\qquad\Longrightarrow\qquad
1 = \frac{4K}{(0.2693)(0.0839)}
$$

$$
K = 5.6\times 10^{-3}
$$

### Verificación por MATLAB

```matlab
gFz = c2d(gF, T, 'matched')
zpk(gFz)
```

---

## Ejemplo: sistema de control muestreado

![Lazo muestreado con ZOH](../apoyo/figuras/sistema_muestreado_sd.svg)

Con $T = 1$, retenedor de orden cero y planta con retardo:

$$
G(z) = \frac{\left(1 - e^{-Ts}\right)K\,e^{-1.25 s}}{s^2\,(s+1)}
$$

$$
G(z) = 0.2223\,K\;
\frac{(z + 1.755)(z + 0.03)}{z^2\,(z-1)\,(z-0.368)}
$$

### Rutina MATLAB

```matlab
G = zpk([-0.03 -1.755], [0, 0, 1, 0.368], [0.2223], 1)
rlocus(G)
```
