# Práctica del motor

*Transcripción de las páginas 33 y 34 del cuaderno.*

## Objetivo

Modelar el motor: la entrada es **tensión** y la salida **velocidad**.

- Motor → identificación con el toolbox `ident`.
- Medida de velocidad con encoder.

## Caso último del ejercicio anterior

El cálculo manual que se retoma en la práctica:

$$
G(z) = \frac{z - 1.1}{(z - 0.4)\,(z^2 - 1.6z + 0.8)}
$$

*(el valor de $T$ quedó sin anotar en el cuaderno)*

## Divisor de tensión para el acople de señal

Para bajar los 9 V a los 5 V del nivel lógico:

![Divisor de tensión](../apoyo/figuras/divisor_tension.svg)

$$
5 = 9 \cdot \frac{R_2}{R_1 + R_2}
\qquad\Longrightarrow\qquad
\frac{5}{9} = \frac{R_2}{R_1 + R_2}
$$

$$
R_2 = 5
\qquad
R_1 + R_2 = 9
\qquad
R_1 = 4
$$

Escalados anotados al margen:

| Relación | ×2 | | |
|---|---|---|---|
| $R_1 = 4$ | 800 | 1.2 | 20 k |
| $R_2 = 5$ | 1000 | 1.5 | 25 k |

*(la cabecera de las dos últimas columnas no quedó anotada)*
