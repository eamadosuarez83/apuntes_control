"""Figuras para el capitulo de tecnicas clasicas de diseno (complemento,
no sale del cuaderno). Usa la libreria `control` (pip install control),
el equivalente en Python del Control System Toolbox de MATLAB.

    python3 diseno.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import control as ct


def lugar_raices(nombre='lugar_raices'):
    """Root locus de G(s)=1/(s(s+4)), marcando el punto de diseno K=16
    (zeta=0.5). Mismo sistema que el ejercicio resuelto en el capitulo."""
    G = ct.tf([1], [1, 4, 0])

    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    ct.root_locus_plot(G, ax=ax, color='black', initial_gain=16, grid=True)
    ax.set_title('Lugar de las raíces: $G(s)=K/[s(s+4)]$')
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def nyquist_ilustrativo(nombre='nyquist_ilustrativo'):
    """Nyquist del mismo sistema ilustrativo usado en margen de ganancia/fase
    (K/[(s+1)(s+2)(s+3)], K=119.08) -- mismo K que ya se sabe inestable por
    MG y MF, para verificar con un tercer criterio."""
    K = 119.08
    G = ct.tf([K], np.polynomial.polynomial.polyfromroots([-1, -2, -3])[::-1])

    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    ct.nyquist_plot(G, ax=ax, color='black', label_freq=0)
    ax.plot([-1], [0], marker='+', ms=12, mew=2, color='0.4')
    ax.annotate('$-1$', (-1, 0), textcoords='offset points', xytext=(6, 6),
                fontsize=9)
    ax.set_title('Nyquist: $G(s)=K/[(s{+}1)(s{+}2)(s{+}3)]$')
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def bode_lead(nombre='bode_lead'):
    """Comparacion de Bode antes/despues de agregar el compensador de
    adelanto disenado en el texto, sobre G(s)=20/[s(s+1)(s+5)]."""
    G = ct.tf([20], [1, 6, 5, 0])
    # Compensador disenado en el ejercicio: Kc(s+0.956)/(s+11.631), Kc=12.162
    C = 12.162 * ct.tf([1, 0.956], [1, 11.631])
    L0 = G
    L1 = C * G

    w = np.logspace(-1, 2, 500)
    resp0 = ct.frequency_response(L0, w)
    resp1 = ct.frequency_response(L1, w)
    mag0, fase0 = resp0.magnitude, np.degrees(np.unwrap(resp0.phase))
    mag1, fase1 = resp1.magnitude, np.degrees(np.unwrap(resp1.phase))

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.4), sharex=True)
    a1.semilogx(w, 20*np.log10(mag0), color='0.6', lw=1.2, ls='--', label='sin compensar')
    a1.semilogx(w, 20*np.log10(mag1), color='black', lw=1.3, label='con adelanto')
    a1.axhline(0, color='0.8', lw=0.6)
    a1.set_ylabel('$|L|$ [dB]')
    a1.legend(fontsize=8, frameon=False)

    a2.semilogx(w, fase0, color='0.6', lw=1.2, ls='--')
    a2.semilogx(w, fase1, color='black', lw=1.3)
    a2.axhline(-180, color='0.8', lw=0.6, ls='--')
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
    lugar_raices()
    nyquist_ilustrativo()
    bode_lead()
