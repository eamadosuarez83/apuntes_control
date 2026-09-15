"""Diagramas de bloques de los apuntes, hechos con schemdraw.

    pip install schemdraw
    python3 bloques_schemdraw.py   ->  genera los .svg y los .pdf

SVG para leer el Markdown en cualquier visor; PDF vectorial porque XeLaTeX
no incrusta SVG.
"""
import schemdraw
import schemdraw.elements as elm
from schemdraw import dsp, flow


def _sum_labels(s):
    return (s.label('+', loc='left', ofst=(-.1, .25))
             .label('\u2212', loc='bottom', ofst=(-.25, -.1)))


def lazo_cerrado(ext):
    """x -> (+/-) -> C -> G -> y, con realimentacion unitaria."""
    with schemdraw.Drawing(file=f'lazo_cerrado_sd{ext}', show=False) as d:
        d.config(fontsize=13, unit=2)
        d += dsp.Arrow().right().label('x', loc='left')
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).label('e', loc='top')
        C = d.add(flow.Box(w=1.4, h=1).anchor('W').label('C'))
        d += dsp.Arrow().right().at(C.E).length(1)
        G = d.add(flow.Box(w=1.4, h=1).anchor('W').label('G'))
        d += dsp.Line().right().at(G.E).length(1)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.2).label('y', loc='right')
        d += dsp.Line().down().at(tap.center).length(1.8)
        d += dsp.Line().left().tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


def lazo_realimentado(ext):
    """Lazo con realimentacion H:  y/r = G/(1+GH)."""
    with schemdraw.Drawing(file=f'lazo_realimentado_sd{ext}', show=False) as d:
        d.config(fontsize=13, unit=2)
        d += dsp.Arrow().right().label('r', loc='left')
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).label('e', loc='top')
        G = d.add(flow.Box(w=1.4, h=1).anchor('W').label('G'))
        d += dsp.Line().right().at(G.E).length(1)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.2).label('y', loc='right')
        d += dsp.Line().down().at(tap.center).length(1.8)
        d += dsp.Line().left().length(0.8)
        H = d.add(flow.Box(w=1.4, h=1).anchor('E').label('H'))
        d += dsp.Arrow().left().at(H.W).tox(s.S).label('b', loc='bottom')
        d += dsp.Arrow().up().toy(s.S)


def lazo_laplace(ext):
    """Lazo en el dominio de Laplace: R(s), E(s), G(s), A(s), B(s), Y(s)."""
    with schemdraw.Drawing(file=f'lazo_laplace_sd{ext}', show=False) as d:
        d.config(fontsize=12, unit=2)
        d += dsp.Arrow().right().label('R(s)', loc='left')
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).label('E(s)', loc='top')
        G = d.add(flow.Box(w=1.7, h=1).anchor('W').label('G(s)'))
        d += dsp.Line().right().at(G.E).length(1)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.4).label('Y(s)', loc='right')
        d += dsp.Line().down().at(tap.center).length(1.9)
        d += dsp.Line().left().length(0.8)
        A = d.add(flow.Box(w=1.7, h=1).anchor('E').label('A(s)'))
        d += dsp.Arrow().left().at(A.W).tox(s.S).label('B(s)', loc='bottom')
        d += dsp.Arrow().up().toy(s.S)


def lazo_pid(ext):
    """Lazo cerrado con controlador Gc(s) y planta G(s)."""
    with schemdraw.Drawing(file=f'lazo_pid_sd{ext}', show=False) as d:
        d.config(fontsize=12, unit=2)
        d += dsp.Arrow().right().label('R(s)', loc='left')
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).label('E(s)', loc='top')
        Gc = d.add(flow.Box(w=1.8, h=1).anchor('W').label('$G_c(s)$'))
        d += dsp.Arrow().right().at(Gc.E).length(0.9).label('U(s)', loc='top')
        G = d.add(flow.Box(w=1.8, h=1).anchor('W').label('G(s)'))
        d += dsp.Line().right().at(G.E).length(0.9)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.2).label('Y(s)', loc='right')
        d += dsp.Line().down().at(tap.center).length(1.9)
        d += dsp.Line().left().tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


def sistema_muestreado(ext):
    """Lazo muestreado: muestreador T, retenedor ZOH y planta con retardo."""
    with schemdraw.Drawing(file=f'sistema_muestreado_sd{ext}', show=False) as d:
        d.config(fontsize=11, unit=1.9)
        d += dsp.Arrow().right()
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Line().right().at(s.E).length(0.7)
        d += elm.Switch().right().label('T', loc='top')
        d += dsp.Line().right().length(0.5)
        zoh = d.add(flow.Box(w=2.3, h=1.1).anchor('W')
                    .label(r'$\dfrac{1-e^{-Ts}}{s}$'))
        d += dsp.Arrow().right().at(zoh.E).length(0.7)
        G = d.add(flow.Box(w=2.3, h=1.1).anchor('W')
                  .label(r'$\dfrac{K\,e^{-1.25s}}{s(s+1)}$'))
        d += dsp.Line().right().at(G.E).length(0.6)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.0).label('Y(s)', loc='right')
        d += dsp.Line().down().at(tap.center).length(2.0)
        d += dsp.Line().left().tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


def lazo_proporcional(ext):
    """Control proporcional: solo la ganancia K delante de la planta."""
    with schemdraw.Drawing(file=f'lazo_proporcional_sd{ext}', show=False) as d:
        d.config(fontsize=12, unit=2)
        d += dsp.Arrow().right().label('R(s)', loc='left')
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).label('E(s)', loc='top')
        K = d.add(flow.Box(w=1.3, h=1).anchor('W').label('K'))
        d += dsp.Arrow().right().at(K.E).length(0.9)
        G = d.add(flow.Box(w=1.8, h=1).anchor('W').label('G(s)'))
        d += dsp.Line().right().at(G.E).length(0.9)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.2).label('Y(s)', loc='right')
        d += dsp.Line().down().at(tap.center).length(1.9)
        d += dsp.Line().left().tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


def lazo_integral_z(ext):
    """Control integral en discreto: el integrador z/(z-1) antes de la ganancia."""
    with schemdraw.Drawing(file=f'lazo_integral_z_sd{ext}', show=False) as d:
        d.config(fontsize=11, unit=1.9)
        d += dsp.Arrow().right().label('R(z)', loc='left')
        s = d.add(_sum_labels(dsp.Sum().anchor('W')))
        d += dsp.Arrow().right().at(s.E).length(0.7)
        I = d.add(flow.Box(w=1.9, h=1.1).anchor('W').label(r'$\dfrac{z}{z-1}$'))
        d += dsp.Arrow().right().at(I.E).length(0.6)
        K = d.add(flow.Box(w=1.2, h=1.1).anchor('W').label('K'))
        d += dsp.Arrow().right().at(K.E).length(0.6)
        G = d.add(flow.Box(w=1.8, h=1.1).anchor('W').label('G(z)'))
        d += dsp.Line().right().at(G.E).length(0.7)
        tap = d.add(dsp.Dot())
        d += dsp.Arrow().right().length(1.0).label('Y(z)', loc='right')
        d += dsp.Line().down().at(tap.center).length(2.0)
        d += dsp.Line().left().tox(s.S)
        d += dsp.Arrow().up().toy(s.S)


if __name__ == '__main__':
    for backend, ext in (('svg', '.svg'), ('matplotlib', '.pdf')):
        schemdraw.use(backend)
        lazo_cerrado(ext)
        lazo_realimentado(ext)
        lazo_laplace(ext)
        lazo_pid(ext)
        sistema_muestreado(ext)
        lazo_proporcional(ext)
        lazo_integral_z(ext)
