# Sistemas de Control Digital

*Transcripción de las páginas 1–5 del cuaderno.*

## Temario

### Unidad 1

- Modelo matemático
- Función de transferencia
- Estabilidad
- Control on/off
- Sistemas de control discreto
  - Periodo de muestreo
- Transformada Z
- Relación entre el plano *s* y el plano *z*
- Técnica de mapeo de polos y ceros
- Transformación bilineal
- Retenedor de orden cero (ZOH)
- Retenedor de orden uno

### Unidad 2

- Respuesta transitoria de los sistemas
  - de 1.er orden
  - de 2.º orden
  - de orden *n*
- Toolbox `ident` (identificación de sistemas)
- Respuesta transitoria de sistemas discretos
- Control proporcional y control integral
- Criterios de estabilidad / margen de ganancia

### Unidad 3

- Control PID
- Sintonización del control PID
- Implementación

### Bibliografía

- Ogata — *Ingeniería de control moderna* / *Sistemas de control en tiempo discreto*
- Kuo — *Sistemas de control automático* / *Sistemas de control digital*

---

## Conceptos

*Sección ampliada — a pedido explícito (`pendiente.txt`): el cuaderno trae
estas definiciones muy resumidas, en una o dos líneas cada una. Se
profundiza cada concepto y se agregan varios que el cuaderno no define por
separado pero usa constantemente.*

**Sistema.** Un conjunto de elementos relacionados entre sí que, ante una o
más entradas, produce una o más salidas. En control, casi siempre interesa
un sistema con **una** entrada relevante (la referencia) y **una** salida
relevante (lo que se quiere regular) — aunque por dentro tenga muchas
variables.

**Variable controlada.** La cantidad que se mide y que se quiere llevar (o
mantener) en un valor deseado. Ej.: la temperatura de un horno, la
velocidad de un motor, el nivel de un tanque.

**Señal de control (variable manipulada).** La cantidad que el controlador
sí puede modificar directamente, y que a su vez afecta a la variable
controlada. Ej.: la potencia entregada a la resistencia del horno, el
voltaje aplicado al motor, la apertura de una válvula. Es importante no
confundir las dos: uno **mide** la variable controlada, pero **actúa
sobre** la variable manipulada — nunca se actúa directamente sobre lo que
se quiere controlar.

**Referencia (*setpoint*).** El valor deseado de la variable controlada.
Ej.: los 22 °C a los que se quiere el horno.

**Error.** La diferencia entre la referencia y el valor real de la
variable controlada ($e = r - y$). Es la señal que el controlador usa para
decidir qué hacer — si el error es cero, en principio no hace falta
corregir nada.

**Perturbación.** Cualquier entrada no deseada que afecta a la variable
controlada sin pasar por el controlador. Ej.: alguien abre la puerta del
horno (entra aire frío), cambia la carga del motor. El control existe, en
buena parte, para que el sistema rechace perturbaciones sin que el usuario
tenga que intervenir.

**Sensor / transductor.** El elemento que mide la variable controlada y la
convierte en una señal que el controlador pueda usar (normalmente
eléctrica). Ej.: una termocupla, un encoder.

**Actuador.** El elemento que aplica físicamente la señal de control sobre
la planta. Ej.: una resistencia calefactora, un motor, una válvula.

**Controlar.** Medir el valor de la variable controlada (vía el sensor) y
aplicar la variable manipulada (vía el actuador) de forma que el error
tienda a cero, incluso ante perturbaciones.

**Planta.** El objeto físico a controlar — el sistema cuya dinámica no se
elige, ya viene dada por la física del problema. Ej.: un horno, un reactor
químico, un motor.

### Lazo abierto vs. lazo cerrado

**Sistema de control de lazo abierto.** La señal de control se calcula solo
a partir de la referencia, **sin medir** la salida real — no hay sensor
retroalimentando información. Ej.: una lavadora con temporizador fijo (lava
20 minutos sin importar si la ropa ya quedó limpia), un microondas que
calienta un tiempo fijo. Es simple y barato, pero no corrige errores ni
rechaza perturbaciones: si algo cambia (menos ropa, más suciedad), el
sistema no se entera.

**Sistema de control de lazo cerrado.** Compara la entrada (referencia) con
la salida real (medida por el sensor) y usa la diferencia (el error) como
medio de control — de ahí el nombre **realimentación** (*feedback*): parte
de la salida "vuelve" a la entrada del controlador. Ej.: un aire
acondicionado con termostato (mide la temperatura real y enciende/apaga
según qué tan lejos esté del *setpoint*), un control de crucero de auto
(mide la velocidad real y ajusta el acelerador). Es más complejo (necesita
sensor) pero corrige errores y rechaza perturbaciones automáticamente —
es el tipo de sistema que ocupa prácticamente todo el curso.

![Lazo cerrado](../apoyo/figuras/lazo_cerrado_sd.svg)

### Modelo matemático

Describe la dinámica del sistema mediante **ecuaciones diferenciales**
(siempre con algún grado de aproximación — ningún modelo captura la
realidad al 100 %, solo lo suficiente para diseñar el control). La
transformada de Laplace (capítulo siguiente) es la herramienta que
convierte esas ecuaciones diferenciales en álgebra, mucho más fácil de
manipular.

| Dominio | Ley física | Resultado |
|---|---|---|
| Sistemas mecánicos | Leyes de Newton | modelo matemático |
| Sistemas eléctricos | Leyes de Kirchhoff | modelo matemático |

**Ejemplo mínimo, para no quedarse solo con la tabla**: un sistema
masa-amortiguador (sin resorte), con una fuerza $f(t)$ aplicada a una masa
$m$ que se mueve con velocidad $v(t)$ y roza con coeficiente $b$. La
segunda ley de Newton da la ecuación diferencial:

$$
m\,\frac{dv(t)}{dt} + b\,v(t) = f(t)
$$

Este es exactamente el tipo de ecuación que el capítulo siguiente aprende
a resolver con Laplace en vez de a mano — y de ahí sale, directo, la
función de transferencia $V(s)/F(s)$ (ver el ejemplo trabajado en la
sección de polos y ceros del capítulo 2).

**Otros enfoques de control mencionados:** control óptimo (elige la señal
de control que minimiza algún costo, ej. gastar el mínimo de energía),
control en espacio de estados (modela con variables de estado internas en
vez de una sola función de transferencia entrada-salida — necesario cuando
hay varias entradas/salidas), control robusto (diseñado para seguir
funcionando bien aunque el modelo de la planta tenga incertidumbre o
cambie un poco). Ninguno de los tres se desarrolla en este curso, pero
vale saber que existen y para qué sirven.

---

## Lazo cerrado con realimentación *H*

![Lazo cerrado con H](../apoyo/figuras/lazo_realimentado_sd.svg)

Nomenclatura:

- $e$ — error
- $y$ — salida
- $r$ — señal de entrada (referencia)
- $b$ — señal realimentada
- $G$ y $H$ — ganancias constantes (en este ejemplo)

### Deducción de la función de transferencia

Ecuaciones del lazo:

$$
\text{(1)}\quad e = r - b
\qquad
\text{(2)}\quad b = y\,H
\qquad
\text{(3)}\quad y = e\,G
$$

Reemplazando (3) en (1):

$$
\begin{aligned}
\frac{y}{G} &= r - b \\[2pt]
y &= (r - b)\,G \\[2pt]
y &= (r - y\,H)\,G \\[2pt]
y &= r\,G - y\,G\,H \\[2pt]
y + y\,G\,H &= r\,G \\[2pt]
y\,(1 + G\,H) &= r\,G \\[2pt]
y &= \frac{r\,G}{1 + G\,H}
\qquad\Longrightarrow\qquad
r = \frac{y\,(1 + G\,H)}{G}
\end{aligned}
$$

**Resultado:**

$$
\boxed{\;F = \frac{y}{r} = \frac{G}{1 + G\,H}\;}
\qquad
\text{función de transferencia} = \frac{\text{salida}}{\text{entrada}}
$$
