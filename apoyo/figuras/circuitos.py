"""Circuitos de los apuntes: modelado RC y divisor de tension de la practica.

    python3 circuitos.py   ->  genera .svg y .pdf
"""
import schemdraw
import schemdraw.elements as elm


def circuito_rc(ext):
    with schemdraw.Drawing(file=f'circuito_rc{ext}', show=False) as d:
        d.config(fontsize=12, unit=2.6)
        V = d.add(elm.SourceV().up().label('$V_{in}$', loc='left'))
        C = d.add(elm.Capacitor().right().label('$V_C$'))
        d += elm.CurrentLabelInline(direction='in').at(C).label('$I(t)$')
        d += elm.Resistor().down().label('$V_R$')
        d += elm.Line().left().tox(V.start)


def divisor_tension(ext):
    """Divisor de tension de la practica del motor: 9 V -> 5 V."""
    with schemdraw.Drawing(file=f'divisor_tension{ext}', show=False) as d:
        d.config(fontsize=12, unit=2.4)
        V = d.add(elm.SourceV().up().label('9 V', loc='left'))
        d += elm.Line().right().length(2)
        d += elm.Resistor().down().label('$R_1 = 4$')
        med = d.add(elm.Dot(open=True))
        d += elm.Line().right().length(1.2).label('5 V', loc='right')
        d += elm.Resistor().down().at(med.center).label('$R_2 = 5$')
        d += elm.Line().left().tox(V.start)
        d += elm.Ground()


if __name__ == '__main__':
    for backend, ext in (('svg', '.svg'), ('matplotlib', '.pdf')):
        schemdraw.use(backend)
        circuito_rc(ext)
        divisor_tension(ext)
