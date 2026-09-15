"""Mapas de polos en el plano s para los problemas de la Unidad 1.

    python3 planos_s.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def plano_s(nombre, polos, titulo, xlim, ylim):
    fig, ax = plt.subplots(figsize=(4.2, 3.2))
    ax.axhline(0, color='0.35', lw=0.9)
    ax.axvline(0, color='0.35', lw=0.9)
    for sig, om in polos:
        ax.plot(sig, om, 'x', ms=11, mew=2.2, color='black')
        ax.annotate(f'{sig:+.2f}{om:+.3f}j', (sig, om),
                    textcoords='offset points', xytext=(8, 6), fontsize=8)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.set_title(titulo, fontsize=10)
    ax.grid(True, ls=':', lw=0.5, color='0.8')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    r15 = 15 ** 0.5 / 2
    plano_s('plano_s_estable',
            [(-0.5, r15), (-0.5, -r15)],
            r'$G(s)=1/(s^2+s+4)$: semiplano izquierdo',
            (-1.5, 1.5), (-2.5, 2.5))
    plano_s('plano_s_inestable',
            [(0.5, r15), (0.5, -r15)],
            r'$G(s)=1/(s^2-s+4)$: semiplano derecho',
            (-1.5, 1.5), (-2.5, 2.5))
    plano_s('plano_s_oscilatorio',
            [(0.0, 2.0), (0.0, -2.0)],
            r'$G(s)=1/(s^2+4)$: eje imaginario',
            (-1.5, 1.5), (-2.8, 2.8))
