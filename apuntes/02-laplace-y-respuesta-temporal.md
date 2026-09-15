# Transformada de Laplace y respuesta temporal

*Transcripción de las páginas 6–15 del cuaderno.*

## Transformada de Laplace

$$
F(s) = \int_{0}^{\infty} e^{-st} f(t)\, dt
$$

Válida para sistemas **LTI** (lineales e invariantes en el tiempo).

### Polos y ceros

$$
G(s) = \frac{\mathrm{Num}(s)}{\mathrm{Den}(s)}
$$

- $\mathrm{Num}(s) = 0$ → **ceros**
- $\mathrm{Den}(s) = 0$ → **polos**

### Estabilidad según la ubicación de los polos

| Condición | Comportamiento |
|---|---|
| $\operatorname{Re}\{s\} < 0$ | estable |
| $\operatorname{Re}\{s\} > 0$ | inestable |
| $s = \pm j\alpha$ | oscilatorio |
| un polo en $s = 0$ | integrador |
| un cero en $s = 0$ | derivador |

Variable compleja:

$$
s = \sigma + j\omega
$$

### Forma general y polinomio característico

$$
G(s) = \frac{Y(s)}{X(s)}
= \frac{b_0 s^{m} + b_1 s^{m-1} + \cdots}{a_0 s^{n} + a_1 s^{n-1} + \cdots}
$$

El denominador es el **polinomio característico**.

### En Matlab

$$
\texttt{[num, den] = feedback(num1, den1, \ldots)}
$$

---

## Funciones de transferencia en el lazo

![Lazo en el dominio de Laplace](../apoyo/figuras/lazo_laplace_sd.svg)

**Función de transferencia de lazo abierto:**

$$
\frac{B(s)}{E(s)} = G(s)\,A(s)
$$

**Función de transferencia de la trayectoria directa:**

$$
\frac{Y(s)}{E(s)} = G(s)
$$

---

## Ejercicio 1 — polo real simple

$$
G(s) = \frac{Y(s)}{X(s)} = \frac{1}{s-a}
\qquad
x(t) =
\begin{cases}
1 & t > 0 \\
0 & t < 0
\end{cases}
\qquad
X(s) = \frac{1}{s}
$$

$$
Y(s) = G(s)\,X(s) = \left(\frac{1}{s-a}\right)\left(\frac{1}{s}\right)
$$

Fracciones parciales:

$$
\begin{aligned}
Y &= \frac{A}{s-a} + \frac{B}{s}
   = \frac{A\,s + B\,s - a\,B}{s\,(s-a)}
   = \frac{(A+B)\,s - a\,B}{s\,(s-a)}
   = \frac{1}{s\,(s-a)} \\[4pt]
(A+B)\,s - a\,B &= 1
\end{aligned}
$$

Igualando coeficientes:

$$
\begin{aligned}
A + B &= 0 \\
-a\,B &= 1 \quad\Longrightarrow\quad B = -\frac{1}{a},
\qquad A = \frac{1}{a}
\end{aligned}
$$

Reemplazando:

$$
Y(s) = \frac{1/a}{s-a} - \frac{1/a}{s}
\qquad\Longrightarrow\qquad
\boxed{\,y(t) = \frac{1}{a}\,e^{a t} - \frac{1}{a}\,}
$$

El cuaderno anota que hay singularidades en $s = a$ y en $s = 0$, y dibuja una
exponencial creciente — el caso $a > 0$, inestable.

## Ejercicio 2 — planteamiento con polo en $-a$

$$
Y(s) = \frac{1}{(s+a)\,s}
$$

$$
\begin{aligned}
Y &= \frac{A}{s+a} + \frac{B}{s}
   = \frac{A\,s + B\,s + a\,B}{(s+a)\,s}
   = \frac{s\,(A+B) + a\,B}{s\,(s+a)}
   = \frac{1}{s\,(s+a)} \\[4pt]
A + B &= 0, \qquad a\,B = 1
\end{aligned}
$$

*(El cuaderno deja el desarrollo aquí; el resultado sería
$y(t) = \frac{1}{a}\left(1 - e^{-a t}\right)$.)*

---

## Pares de transformadas usados

| $F(s)$ | $f(t)$ |
|---|---|
| $\dfrac{1}{s+\alpha}$ | $e^{-\alpha t}$ |
| $\dfrac{s+a}{(s+a)^2 + \omega^2}$ | $e^{-a t}\cos \omega t$ |
| $\dfrac{\omega}{(s+a)^2 + \omega^2}$ | $e^{-a t}\operatorname{sen} \omega t$ |

---

## Problema — polos complejos conjugados

$$
G(s) = \frac{1}{s^2 + s + 4}
\qquad
X(s) = \frac{1}{s}
$$

### Estabilidad

$$
s_{1,2} = -0.5 \pm j\,1.936
$$

![Polos en el semiplano izquierdo](../apoyo/figuras/plano_s_estable.svg)

### Caso complejo conjugado

$$
Y(s) = \frac{A}{s} + \frac{B\,s + C}{s^2 + s + 4}
$$

$$
\begin{aligned}
\frac{A s^2 + A s + 4A + B s^2 + C s}{s\,(s^2+s+4)}
 &= \frac{1}{(s^2+s+4)\,s} \\[4pt]
(A+B)\,s^2 + (A+C)\,s + 4A &= 1
\end{aligned}
$$

$$
A + B = 0, \qquad A + C = 0, \qquad 4A = 1
$$

$$
A = \tfrac{1}{4}, \qquad C = -\tfrac{1}{4}, \qquad B = -\tfrac{1}{4}
$$

El cuaderno anota aquí: *parte real del polo → respuesta natural; parte
imaginaria → respuesta forzada.*

$$
Y(s) = \frac{1/4}{s} + \frac{-\tfrac{1}{4}s - \tfrac{1}{4}}{s^2+s+4}
$$

### Completar cuadrados

$$
s^2 + s + \tfrac{1}{4} - \tfrac{1}{4} + 4
= \left(s + \tfrac{1}{2}\right)^2 - \tfrac{1}{4} + 4
= \left(s + \tfrac{1}{2}\right)^2 + \tfrac{15}{4}
$$

### Ajuste al par coseno–seno

$$
\frac{-\tfrac{1}{4}\,(s+1)}{\left(s+\tfrac12\right)^2 + \tfrac{15}{4}}
= \frac{-\tfrac{1}{4}\left[\left(s+\tfrac12\right) + \tfrac12\right]}
        {\left(s+\tfrac12\right)^2 + \tfrac{15}{4}}
$$

El segundo término se multiplica y divide por $\sqrt{15/4} = \sqrt{15}/2$ para
dejarlo en la forma $\omega/\left[(s+a)^2+\omega^2\right]$:

$$
\frac{\tfrac12}{\sqrt{15}/2} = \frac{1}{\sqrt{15}}
$$

### Resultado

$$
Y(s) = \frac{1/4}{s}
- \frac{1}{4}\left[
\frac{s + \tfrac12}{\left(s+\tfrac12\right)^2 + \tfrac{15}{4}}
+ \frac{1}{\sqrt{15}}\cdot
\frac{\sqrt{15}/2}{\left(s+\tfrac12\right)^2 + \tfrac{15}{4}}
\right]
$$

Antitransformando:

$$
\boxed{\;
y(t) = \frac{1}{4}
- \frac{1}{4}\left[
e^{-t/2}\cos\frac{\sqrt{15}}{2}t
+ \frac{1}{\sqrt{15}}\,e^{-t/2}\operatorname{sen}\frac{\sqrt{15}}{2}t
\right]\;}
$$

---

## Tarea — polos en el semiplano derecho

$$
G(s) = \frac{1}{s^2 - s + 4}
\qquad
X(s) = \frac{1}{s}
$$

*(En la misma hoja aparece también $G(s) = 1/(s^2+4)$, que se resuelve más
abajo como segundo ejercicio.)*

![Polos en el semiplano derecho](../apoyo/figuras/plano_s_inestable.svg)

### Solución

$$
Y(s) = G(s)\,X(s) = \frac{1}{s^2-s+4}\cdot\frac{1}{s}
$$

$$
Y(s) = \frac{A}{s} + \frac{B\,s + C}{s^2 - s + 4}
= \frac{A s^2 - A s + 4A + B s^2 + C s}{s\,(s^2-s+4)}
= \frac{(A+B)\,s^2 + (C-A)\,s + 4A}{s\,(s^2-s+4)}
$$

$$
\begin{aligned}
A + B &= 0 \quad\Longrightarrow\quad A = -B \\
C - A &= 0 \quad\Longrightarrow\quad C = A \\
4A &= 1 \quad\Longrightarrow\quad A = \tfrac14 = C, \qquad B = -\tfrac14
\end{aligned}
$$

$$
Y(s) = \frac{1/4}{s} + \frac{-\tfrac14 s + \tfrac14}{s^2-s+4}
     = \frac{1/4}{s} - \frac{\tfrac14 s - \tfrac14}{s^2-s+4}
$$

### Completar cuadrados

$$
2\gamma = -1 \;\Longrightarrow\; \gamma = -\tfrac12, \quad \gamma^2 = \tfrac14
$$

$$
s^2 - s + \tfrac14 - \tfrac14 + \tfrac{16}{4}
= \left(s - \tfrac12\right)^2 + \tfrac{15}{4}
$$

$$
\begin{aligned}
Y(s) &= \frac{1}{4}\left[
\frac{1}{s} - \frac{s-1}{\left(s-\tfrac12\right)^2 + \tfrac{15}{4}}\right] \\[4pt]
&= \frac{1}{4}\left[
\frac{1}{s} - \frac{\left(s-\tfrac12\right) - \tfrac12}
                    {\left(s-\tfrac12\right)^2 + \tfrac{15}{4}}\right] \\[4pt]
&= \frac{1}{4}\left[
\frac{1}{s}
- \frac{s-\tfrac12}{\left(s-\tfrac12\right)^2 + \tfrac{15}{4}}
+ \frac{\tfrac12}{\left(s-\tfrac12\right)^2 + \tfrac{15}{4}}\right]
\end{aligned}
$$

El último término se normaliza igual que antes, multiplicando y dividiendo por
$\sqrt{15}/2$.

### Resultado del cuaderno

$$
y(t) = \frac{1}{4}
- e^{t/2}\cos\frac{\sqrt{15}}{2}t
- e^{t/2}\operatorname{sen}\frac{\sqrt{15}}{2}t
$$

La exponencial es **creciente** ($e^{+t/2}$), coherente con los polos en
$+\tfrac12 \pm j\tfrac{\sqrt{15}}{2}$: el sistema es inestable.

## Segundo ejercicio — polos sobre el eje imaginario

$$
Y(s) = \frac{1}{(s^2+4)\,s}
$$

![Polos sobre el eje imaginario](../apoyo/figuras/plano_s_oscilatorio.svg)

$$
Y(s) = \frac{A}{s} + \frac{B\,s + C}{s^2+4}
= \frac{A s^2 + 4A + B s^2 + C s}{s\,(s^2+4)}
$$

$$
(A+B)\,s^2 + C\,s + 4A = 1
$$

$$
A + B = 0 \;\Longrightarrow\; A = -B,
\qquad C = 0,
\qquad 4A = 1 \;\Longrightarrow\; A = \tfrac14
$$

$$
Y(s) = \frac{1/4}{s} - \frac{\tfrac14 s}{s^2+4}
     = \frac{1}{4}\left[\frac{1}{s} - \frac{s}{s^2+4}\right]
$$

### Completar cuadrado

$$
(s+0)^2 + 4
\qquad\Longrightarrow\qquad
Y(s) = \frac{1}{4}\left[\frac{1}{s} - \frac{s+0}{(s+0)^2+4}\right]
$$

$$
\boxed{\;
y(t) = \frac{1}{4}\left[1 - \cos 2t\right]
     = \frac{1}{4} - \frac{\cos 2t}{4}\;}
$$

Oscilación sostenida, sin envolvente que decaiga ni crezca: es el caso
marginal de los polos sobre el eje imaginario.
