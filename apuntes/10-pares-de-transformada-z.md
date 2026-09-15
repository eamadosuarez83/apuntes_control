# Pares de transformada Z desde la serie

*Transcripción de las páginas 48 y 49 del cuaderno.*

## Serie geométrica

$$
\sum_{k=n_1}^{n_2} a^{k}
= \frac{a^{\,n_1} - a^{\,n_2+1}}{1 - a}
$$

Es la herramienta con la que se obtienen los pares que siguen.

---

## Exponencial

$$
x(t) = e^{-at}
$$

$$
X(z) = \sum_{n=0}^{\infty} e^{-anT} z^{-n}
= \sum_{n=0}^{\infty}\left(e^{-aT} z^{-1}\right)^{n}
$$

Aplicando la serie:

$$
X(z) = \frac{1 - 0}{1 - e^{-aT} z^{-1}}
= \frac{1}{1 - \dfrac{e^{-aT}}{z}}
$$

$$
X(z) = \frac{\dfrac{1}{z}}{\dfrac{z - e^{-aT}}{z}}
\qquad\Longrightarrow\qquad
\boxed{\;X(z) = \frac{z}{z - e^{-aT}}\;}
$$

## Potencia

$$
x(t) = a^{n}
$$

$$
X(z) = \sum_{n=0}^{\infty} a^{n} z^{-n}
= \sum_{n=0}^{\infty}\left(a\,z^{-1}\right)^{n}
$$

*(el cuaderno deja el desarrollo a medias; la serie da
$X(z) = \dfrac{z}{z-a}$)*

---

## Coseno

Identidades de partida:

$$
\operatorname{sen}\omega t = \frac{e^{j\omega t} - e^{-j\omega t}}{2j}
\qquad
\cos \omega t = \frac{e^{j\omega t} + e^{-j\omega t}}{2}
$$

$$
\cos \omega t \;\longrightarrow\;
\sum_{n=0}^{\infty}\frac{e^{j\omega t}}{2} z^{-n}
+ \sum_{n=0}^{\infty}\frac{e^{-j\omega t}}{2} z^{-n}
$$

Sumando las dos series geométricas:

$$
\frac{1}{1 - e^{j\omega} z^{-1}} + \frac{1}{1 - e^{-j\omega} z^{-1}}
$$

$$
= \frac{1 - e^{-j\omega n} z^{-1} + 1 - e^{j\omega n} z^{-1}}
{\left(1 - e^{j\omega n} z^{-1}\right)\left(1 - e^{-j\omega n} z^{-1}\right)}
$$

$$
= \frac{2 - \left(e^{-j\omega n} + e^{j\omega n}\right) z^{-1}}
{1 - e^{-j\omega n} z^{-1} - e^{j\omega n} z^{-1}
+ e^{\,j(\omega n - \omega n)} z^{-2}}
$$

Usando de nuevo la identidad del coseno en numerador y denominador:

$$
= \frac{2 - z^{-1}\,(2\cos \omega n)}
{1 - \left(e^{-j\omega} + e^{j\omega}\right) z^{-1} + z^{-2}}
= \frac{2 - z^{-1}\,2\cos \omega n}
{1 - 2\cos \omega n\; z^{-1} + z^{-2}}
$$

$$
\boxed{\;
\frac{2\left(1 - z^{-1}\cos\omega\right)}
{1 - 2\cos\omega\,z^{-1} + z^{-2}}
= \frac{2\left(z^2 - z\cos\omega\right)}{z^2 - 2\cos\omega\,z + 1}
\;}
$$
