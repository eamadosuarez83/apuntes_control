"""Figuras de la practica de identificacion y discretizacion del motor DC
(informe de laboratorio, UTS 2018 - ver capitulo 08).

    python3 informe_motor.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import control as ct

# Modelo identificado con el toolbox Ident (ajuste 58 %), sin el retardo
K_Z, CERO, DEN = 3898.0, 0.1006, [1, 0.2564, 0.1172]
T_M = 1.0            # periodo de muestreo del ensayo: 1 s
RETARDO = 4.4        # segundos


def _limpiar(ax):
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)


def _discreta_manual():
    """Correspondencia de polos y ceros hecha a mano: z = e^{sT}."""
    p = np.roots(DEN)
    zp, zz = np.exp(p*T_M), np.exp(-CERO*T_M)
    den = [1, -2*zp[0].real, abs(zp[0])**2]
    num = np.polymul([1, 1], [1, -zz])           # (z+1)(z - e^{-0.1006 T})
    G = ct.tf([K_Z, K_Z*CERO], DEN)
    kd = ct.dcgain(G)/(np.polyval(num, 1)/np.polyval(den, 1))
    return G, ct.tf(kd*np.array(num), den, dt=T_M), kd, zp, zz


def respuesta(nombre='informe_motor_respuesta'):
    """Escalon del modelo continuo contra el discretizado a mano."""
    G, Gd, _, _, _ = _discreta_manual()
    t = np.linspace(0, 60, 2000)
    _, y = ct.step_response(G, t)
    td = np.arange(0, 61, T_M)
    _, yd = ct.step_response(Gd, td)

    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    ax.plot(t + RETARDO, y, color='0.45', lw=1.2, ls='--',
            label='$G(s)$ continua')
    ax.step(td + RETARDO, yd, color='black', lw=1.2, where='post',
            label='$G(z)$ discretizada, $T=1$ s')
    ax.axhline(ct.dcgain(G), color='0.7', lw=0.8, ls=':')
    ax.annotate(f'$K_{{dc}}$ = {ct.dcgain(G):.0f} RPM/V', (55, ct.dcgain(G)),
                textcoords='offset points', xytext=(-30, 6), fontsize=8,
                color='0.35')
    ax.annotate('retardo de 4.4 s', (RETARDO, 0), textcoords='offset points',
                xytext=(6, 18), fontsize=8, color='0.35',
                arrowprops=dict(arrowstyle='->', lw=0.7, color='0.5'))
    ax.set_xlabel('$t$ [s]')
    ax.set_ylabel('RPM')
    ax.set_xlim(0, 60)
    ax.set_title('Respuesta al escalón del modelo identificado')
    ax.legend(fontsize=8, frameon=False, loc='upper right')
    _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def mapeo(nombre='informe_motor_mapeo'):
    """Los polos y el cero de G(s) llevados al plano z con z = e^{sT}."""
    _, _, _, zp, zz = _discreta_manual()
    p = np.roots(DEN)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.2, 3.0))

    a1.axhline(0, color='0.6', lw=0.8)
    a1.axvline(0, color='0.6', lw=0.8)
    a1.plot(p.real, p.imag, ls='none', marker='x', ms=9, mew=1.6, color='black')
    a1.plot([-CERO], [0], ls='none', marker='o', ms=8, mfc='none', mec='black')
    a1.set_title('plano $s$', fontsize=10)
    a1.set_xlabel(r'$\sigma$')
    a1.set_ylabel(r'$j\omega$')
    a1.set_xlim(-0.35, 0.1)
    a1.set_ylim(-0.45, 0.45)

    ang = np.linspace(0, 2*np.pi, 300)
    a2.plot(np.cos(ang), np.sin(ang), color='0.6', lw=0.9)
    a2.axhline(0, color='0.6', lw=0.8)
    a2.axvline(0, color='0.6', lw=0.8)
    a2.plot(zp.real, zp.imag, ls='none', marker='x', ms=9, mew=1.6,
            color='black')
    a2.plot([zz], [0], ls='none', marker='o', ms=8, mfc='none', mec='black')
    a2.plot([-1], [0], ls='none', marker='o', ms=8, mfc='none', mec='0.55')
    a2.annotate('cero agregado\nen $z=-1$', (-1, 0), textcoords='offset points',
                xytext=(0, -46), fontsize=7.5, color='0.4', ha='center')
    a2.set_title('plano $z$   ($z=e^{sT}$, $T=1$ s)', fontsize=10)
    a2.set_xlabel('Re')
    a2.set_ylabel('Im')
    a2.set_xlim(-1.35, 1.35)
    a2.set_ylim(-1.2, 1.2)
    a2.set_aspect('equal')

    for ax in (a1, a2):
        _limpiar(ax)
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


if __name__ == '__main__':
    respuesta()
    mapeo()
