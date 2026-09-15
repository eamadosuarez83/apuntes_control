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

**Variable controlada.** Cantidad que se mide o se controla.

**Señal de control (variable manipulada).** Cantidad que el controlador modifica para
afectar a la variable controlada.

**Controlar.** Medir el valor de la variable controlada y aplicar la variable manipulada.

**Planta.** El objeto físico a controlar. Ej.: un horno, un reactor químico.

**Sistema de control de lazo cerrado.** Compara la entrada con la salida y usa la
diferencia como medio de control.

![Lazo cerrado](../apoyo/figuras/lazo_cerrado_sd.svg)

**Sistema de control de lazo abierto.** La salida no tiene efecto sobre la acción de
control.

**Modelo matemático.** Describe la dinámica del sistema mediante ecuaciones
diferenciales (siempre con algún grado de aproximación).

| Dominio | Ley física | Resultado |
|---|---|---|
| Sistemas mecánicos | Leyes de Newton | modelo matemático |
| Sistemas eléctricos | Leyes de Kirchhoff | modelo matemático |

**Otros enfoques de control mencionados:** control óptimo, control en espacio de
estados, control robusto.

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
