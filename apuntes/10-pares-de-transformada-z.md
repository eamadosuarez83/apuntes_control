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
\operatorname{sen}(\omega n T) = \frac{e^{j\omega n T} - e^{-j\omega n T}}{2j}
\qquad
\cos(\omega n T) = \frac{e^{j\omega n T} + e^{-j\omega n T}}{2}
$$

Con $x(nT) = \cos(\omega n T)$, la transformada es la serie muestreada:

$$
X(z) = \sum_{n=0}^{\infty} \cos(\omega n T)\,z^{-n}
= \frac{1}{2}\sum_{n=0}^{\infty} e^{j\omega n T} z^{-n}
+ \frac{1}{2}\sum_{n=0}^{\infty} e^{-j\omega n T} z^{-n}
$$

Cada suma es la serie geométrica del par exponencial ya visto (con
$a \to e^{\mp j\omega T}$). El factor $\tfrac12$ de la identidad del coseno
**se mantiene** al sumar, no se pierde:

$$
X(z) = \frac{1}{2}\left[
\frac{1}{1 - e^{j\omega T} z^{-1}} + \frac{1}{1 - e^{-j\omega T} z^{-1}}
\right]
$$

$$
= \frac{1}{2}\cdot
\frac{\left(1 - e^{-j\omega T} z^{-1}\right) + \left(1 - e^{j\omega T} z^{-1}\right)}
{\left(1 - e^{j\omega T} z^{-1}\right)\left(1 - e^{-j\omega T} z^{-1}\right)}
= \frac{1}{2}\cdot
\frac{2 - \left(e^{j\omega T} + e^{-j\omega T}\right) z^{-1}}
{1 - \left(e^{j\omega T} + e^{-j\omega T}\right) z^{-1} + z^{-2}}
$$

Usando de nuevo la identidad del coseno en numerador y denominador
($e^{j\omega T} + e^{-j\omega T} = 2\cos\omega T$):

$$
X(z) = \frac{1}{2}\cdot
\frac{2 - 2\cos(\omega T)\,z^{-1}}{1 - 2\cos(\omega T)\,z^{-1} + z^{-2}}
= \frac{1 - \cos(\omega T)\,z^{-1}}{1 - 2\cos(\omega T)\,z^{-1} + z^{-2}}
$$

$$
\boxed{\;
X(z) = \frac{z^2 - z\cos(\omega T)}{z^2 - 2\cos(\omega T)\,z + 1}
\;}
$$

<!-- Nota fig. NOTAS-DESARROLLO.md #39: el cuaderno pierde el factor 1/2 al
     sumar las dos series (queda con el doble del resultado correcto).
     Reescrita la derivacion completa llevando el 1/2 explicito paso a paso
     para que no se pueda perder, y unificada la notacion a omega*T (el
     cuaderno mezclaba omega y omega*n en los exponentes -- NOTAS #40). -->
