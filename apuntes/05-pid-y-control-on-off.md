# Lazo cerrado, PID y control on-off

*Transcripción de las páginas 21 y 22 del cuaderno.*

## Lazo cerrado con controlador

![Lazo cerrado con controlador y planta](../apoyo/figuras/lazo_pid_sd.svg)

$$
\frac{Y(s)}{R(s)} = \frac{G_c(s)\,G(s)}{1 + G_c(s)\,G(s)}
$$

## Control PID

En el tiempo:

$$
u(t) = K\left[\,e(t)
+ \frac{1}{T_i}\int e(t)\,dt
+ T_d\,\frac{de(t)}{dt}\,\right]
$$

Aplicando Laplace:

$$
U(s) = K\left[\,E(s)
+ \frac{1}{T_i}\,\frac{E(s)}{s}
+ T_d\,s\,E(s)\,\right]
$$

Función de transferencia del controlador:

$$
\boxed{\;
G_c = \frac{U(s)}{E(s)}
= K\left[\,1 + \frac{1}{T_i}\,\frac{1}{s} + T_d\,s\,\right]
\;}
\qquad \text{(PID)}
$$

## Sintonización del PID

*Tema explícito de la Unidad 3 del temario que no llegó a aparecer en el
cuaderno — se completa acá porque es, literalmente, el objetivo declarado
de esa unidad: tener el PID no alcanza, hay que saber elegir $K$, $T_i$,
$T_d$.*

Las reglas de **Ziegler-Nichols** (1942) siguen siendo el punto de partida
más enseñado: no dan el ajuste óptimo, pero dan un punto de arranque
razonable a partir de mediciones simples de la planta.

### Método 1 — curva de reacción (lazo abierto)

Se aplica a plantas **estables sin integrador** que responden a un escalón
con forma de "S" (sobreamortiguadas o con retardo) — exactamente el
`Modelo sobreamortiguado` $K e^{-T_d s}/(\tau s+1)$ que ya se planteó en el
capítulo de identificación.

Del ensayo a lazo abierto se miden tres números sobre la curva de reacción:
$K$ (ganancia estática, $y_{ss}/x_{ss}$), $L$ (retardo aparente, donde la
tangente en el punto de inflexión corta al eje de tiempo) y $\tau$
(constante de tiempo, desde ese cruce hasta donde la tangente llega a
$y_{ss}$).

| Controlador | $K_p$ | $T_i$ | $T_d$ |
|---|---|---|---|
| P | $\tau/(KL)$ | — | — |
| PI | $0.9\,\tau/(KL)$ | $L/0.3$ | — |
| PID | $1.2\,\tau/(KL)$ | $2L$ | $0.5L$ |

**Ejemplo.** Ensayo da $K=2$, $L=0.5\,\text{s}$, $\tau=2\,\text{s}$. Para
PID:

$$
K_p = \frac{1.2\,(2)}{(2)(0.5)} = 2.4
\qquad
T_i = 2(0.5) = 1\,\text{s}
\qquad
T_d = 0.5(0.5) = 0.25\,\text{s}
$$

### Método 2 — ganancia última (lazo cerrado)

Se usa cuando no se puede (o no conviene) sacar la planta de operación para
un ensayo a lazo abierto. Con solo control **proporcional** ($T_i\to\infty$,
$T_d=0$) en el lazo, se sube $K_p$ hasta que la salida oscile de forma
**sostenida** (ni crece ni decae) — ese es el punto de estabilidad marginal
visto en el criterio de Routh/margen de ganancia. Se registran:
$K_u$ (ganancia última, la $K_p$ a la que empezó a oscilar) y $P_u$
(periodo de esa oscilación).

| Controlador | $K_p$ | $T_i$ | $T_d$ |
|---|---|---|---|
| P | $0.5\,K_u$ | — | — |
| PI | $0.45\,K_u$ | $P_u/1.2$ | — |
| PID | $0.6\,K_u$ | $P_u/2$ | $P_u/8$ |

**Ejemplo.** Se encuentra oscilación sostenida en $K_u=4$, con
$P_u=2\,\text{s}$. Para PID:

$$
K_p = 0.6(4) = 2.4
\qquad
T_i = \frac{2}{2} = 1\,\text{s}
\qquad
T_d = \frac{2}{8} = 0.25\,\text{s}
$$

(Es coincidencia que salga igual al ejemplo anterior — son dos plantas
distintas con dos métodos distintos; se eligieron los datos para que el
resultado fuera fácil de comparar entre tablas.)

**Cuándo usar cuál**: la curva de reacción es más segura (no hay que llevar
el sistema al borde de la inestabilidad a propósito), pero requiere poder
ensayar a lazo abierto. La ganancia última se usa cuando eso no es posible,
con la planta ya operando en lazo cerrado — con el cuidado de no dejar la
oscilación sostenida corriendo más tiempo del necesario para medir $P_u$.

### El problema del *windup*

La acción integral sigue acumulando error mientras exista, **incluso si el
actuador ya se saturó** (una válvula 100 % abierta, un PWM al 100 %) y no
puede entregar más señal de control real. El integrador sigue creciendo por
dentro sin que la salida real cambie — al "enrollarse" (*windup*) acumula un
término enorme, y cuando el error finalmente cambia de signo, el sistema
tarda en "desenrollarse" antes de reaccionar: se ve como un sobrepaso
grande y lento, muy por encima de lo que predice el modelo lineal del PID.

**Anti-windup por saturación (clamping)**, la solución más simple: cuando la
salida del controlador se satura, se **detiene la integración** (no se suma
más error al integrador) hasta que la salida vuelve a estar dentro de rango.
Esquemas más finos (*back-calculation*) restan del integrador la diferencia
entre la salida calculada y la salida realmente aplicada, para que el
integrador "sepa" que se saturó y se corrija más rápido — pero el clamping
ya resuelve la mayoría de los casos prácticos con control on/off o PWM.

## Control on-off

El cuaderno dibuja la señal de control $u(t)$ conmutando entre $U_{max}$ y
$U_{min}$, y la variable $h(t)$ subiendo hacia el *setpoint* y oscilando
alrededor de él.

## Control on-off con histéresis

Se define una banda alrededor del *setpoint*: $SP + \Delta$ y $SP - \Delta$.
La salida conmuta a $U_{min}$ al superar el límite superior y vuelve a
$U_{max}$ al caer por debajo del límite inferior, de modo que $u(t)$ no
conmuta de forma continua.

![Control on-off con histéresis](../apoyo/figuras/control_onoff.svg)

*(La figura reproduce el trazo del cuaderno simulando una planta de primer
orden; los valores de $\Delta$ y de la constante de tiempo son ilustrativos.)*
