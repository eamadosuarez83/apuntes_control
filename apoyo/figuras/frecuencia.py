"""Figuras de respuesta en frecuencia.

    python3 frecuencia.py   ->  genera los .svg y los .pdf

El margen de ganancia se ilustra sobre un sistema de tercer orden genérico:
G(s) = K/[(s+1)(s+2)(s+3)]. La forma de la curva es ilustrativa (no sale
del cuaderno), pero K se ajustó para que el MG que muestra la figura
coincida con el MG = -6 dB anotado en el texto (09-error-estacionario...).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def margen_ganancia(nombre='margen_ganancia'):
    w = np.logspace(-1, 1.6, 800)
    jw = 1j * w
    K = 119.08  # ajustado para que MG salga -6 dB, igual al texto
    G = K / ((jw + 1) * (jw + 2) * (jw + 3))
    mag = 20 * np.log10(np.abs(G))
    fase = np.degrees(np.unwrap(np.angle(G)))

    # frecuencia donde la fase cruza -180
    i = np.argmin(np.abs(fase + 180))
    w180, mag180 = w[i], mag[i]

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.4), sharex=True)

    a1.semilogx(w, mag, color='black', lw=1.3)
    a1.axhline(0, color='0.6', lw=0.8)
    a1.axvline(w180, color='0.6', lw=0.8, ls=':')
    a1.annotate('', xy=(w180, 0), xytext=(w180, mag180),
                arrowprops=dict(arrowstyle='<->', lw=1.1))
    a1.annotate(f'MG = {-mag180:.1f} dB', (w180, mag180 / 2),
                textcoords='offset points', xytext=(8, -4), fontsize=9)
    a1.set_ylabel('$|G|$ [dB]')

    a2.semilogx(w, fase, color='black', lw=1.3)
    a2.axhline(-180, color='0.6', lw=0.8, ls='--')
    a2.axvline(w180, color='0.6', lw=0.8, ls=':')
    a2.annotate('$-180°$', (w[0], -180), textcoords='offset points',
                xytext=(2, 5), fontsize=9)
    a2.set_ylabel('fase [°]')
    a2.set_xlabel('$\\omega$ [rad/s]')

    for ax in (a1, a2):
        ax.grid(True, which='both', ls=':', lw=0.5, color='0.85')
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    margen_ganancia()
