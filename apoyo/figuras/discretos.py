"""Figuras de la parte discreta: mapeo s->z, muestreo/aliasing y control on-off.

    python3 discretos.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def _guardar(fig, nombre):
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def mapeo_s_z(nombre='mapeo_s_z', T=0.005,
              polos=(-62.8 + 0j, -31.4 + 54.4j, -31.4 - 54.4j)):
    """Plano s (semiplano izquierdo) y su imagen en el plano z (circulo unitario).

    Usa los polos del ejercicio de mapeo del cuaderno.
    """
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.4))

    # --- plano s ---
    a1.axvspan(-80, 0, color='0.88')
    a1.axhline(0, color='0.35', lw=0.9)
    a1.axvline(0, color='0.35', lw=0.9)
    for p in polos:
        a1.plot(p.real, p.imag, 'x', ms=10, mew=2, color='black')
    a1.set_xlim(-80, 30)
    a1.set_ylim(-75, 75)
    a1.set_title('plano $s$  (estable: $\\mathrm{Re}<0$)', fontsize=9)
    a1.set_xlabel('Re')
    a1.set_ylabel('Im')

    # --- plano z ---
    th = np.linspace(0, 2 * np.pi, 400)
    a2.fill(np.cos(th), np.sin(th), color='0.88')
    a2.plot(np.cos(th), np.sin(th), color='0.35', lw=0.9)
    a2.axhline(0, color='0.35', lw=0.9)
    a2.axvline(0, color='0.35', lw=0.9)
    for p in polos:
        z = np.exp(T * p)
        a2.plot(z.real, z.imag, 'x', ms=10, mew=2, color='black')
    a2.set_xlim(-1.4, 1.4)
    a2.set_ylim(-1.4, 1.4)
    a2.set_aspect('equal')
    a2.set_title('plano $z$  (estable: $|z|<1$)', fontsize=9)
    a2.set_xlabel('Re')

    for ax in (a1, a2):
        ax.grid(True, ls=':', lw=0.5, color='0.8')
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
    _guardar(fig, nombre)


def muestreo_aliasing(nombre='muestreo_aliasing'):
    """Espectro base y sus replicas: sin solape y con solape."""
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 4.2), sharex=True)

    def triangulo(ax, centro, ancho, alto=1.0, **kw):
        ax.plot([centro - ancho, centro, centro + ancho],
                [0, alto, 0], **kw)

    fbw = 1.0
    for ax, fn, titulo in ((a1, 3.0, '$f_N \\geq 2f_{BW}$: no hay solape'),
                           (a2, 1.4, '$f_N < 2f_{BW}$: solape (aliasing)')):
        triangulo(ax, 0, fbw, color='black', lw=1.3)
        triangulo(ax, fn, fbw, color='0.45', lw=1.1, ls='--')
        triangulo(ax, -fn, fbw, color='0.45', lw=1.1, ls='--')
        ax.axvline(fn, color='0.75', lw=0.8)
        ax.set_yticks([])
        ax.set_xticks([-fn, -fbw, 0, fbw, fn])
        ax.set_xticklabels(['$-f_N$', '$-f_{BW}$', '0', '$f_{BW}$', '$f_N$'])
        ax.set_title(titulo, fontsize=9)
        ax.set_xlim(-4.2, 4.2)
        ax.set_ylim(0, 1.25)
        for lado in ('top', 'right', 'left'):
            ax.spines[lado].set_visible(False)
    a2.set_xlabel('frecuencia')
    _guardar(fig, nombre)


def control_onoff(nombre='control_onoff', sp=1.0, delta=0.12, tau=1.0,
                  u_max=2.0, u_min=0.0, t_fin=12.0, dt=0.002):
    """Planta de primer orden con control on-off con histeresis SP +/- delta."""
    n = int(t_fin / dt)
    t = np.arange(n) * dt
    h = np.zeros(n)
    u = np.zeros(n)
    encendido = True
    for k in range(1, n):
        if encendido and h[k - 1] > sp + delta:
            encendido = False
        elif not encendido and h[k - 1] < sp - delta:
            encendido = True
        u[k] = u_max if encendido else u_min
        h[k] = h[k - 1] + dt * (u[k] - h[k - 1]) / tau

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.6, 4.0), sharex=True,
                                 gridspec_kw={'height_ratios': [2, 1]})
    a1.axhline(sp, color='0.45', lw=0.9, ls='--')
    a1.axhline(sp + delta, color='0.7', lw=0.8, ls=':')
    a1.axhline(sp - delta, color='0.7', lw=0.8, ls=':')
    a1.plot(t, h, color='black', lw=1.3)
    a1.set_yticks([sp - delta, sp, sp + delta])
    a1.set_yticklabels(['$SP-\\Delta$', '$SP$', '$SP+\\Delta$'])
    a1.set_ylabel('$h(t)$')
    a1.set_title('Control on-off con histéresis', fontsize=10)

    a2.step(t, u, where='post', color='black', lw=1.2)
    a2.set_yticks([u_min, u_max])
    a2.set_yticklabels(['$U_{min}$', '$U_{max}$'])
    a2.set_ylim(u_min - 0.3, u_max + 0.3)
    a2.set_ylabel('$u(t)$')
    a2.set_xlabel('t')

    for ax in (a1, a2):
        ax.grid(True, ls=':', lw=0.5, color='0.85')
        for lado in ('top', 'right'):
            ax.spines[lado].set_visible(False)
    _guardar(fig, nombre)


def plano_z_polos(nombre='plano_z_polos',
                  polos=(0.4 + 0j, 0.8 + 0.4j, 0.8 - 0.4j),
                  ceros=(0.2 + 0j,)):
    """Polos y ceros de G(z) del ejercicio, con el circulo unitario.

    El polo dominante es el mas cercano a z = 1.
    """
    th = np.linspace(0, 2 * np.pi, 400)
    fig, ax = plt.subplots(figsize=(4.4, 3.8))
    ax.fill(np.cos(th), np.sin(th), color='0.9')
    ax.plot(np.cos(th), np.sin(th), color='0.4', lw=1.0)
    ax.axhline(0, color='0.4', lw=0.9)
    ax.axvline(0, color='0.4', lw=0.9)
    for p in polos:
        ax.plot(p.real, p.imag, 'x', ms=11, mew=2.2, color='black')
    for c in ceros:
        ax.plot(c.real, c.imag, 'o', ms=8, mfc='none', mew=1.6, color='black')
    ax.plot(1, 0, marker='|', ms=9, color='0.3')
    ax.annotate('$z=1$', (1, 0), textcoords='offset points',
                xytext=(2, 8), fontsize=8)
    ax.annotate('polo dominante', (0.8, 0.4), textcoords='offset points',
                xytext=(-6, 12), fontsize=8, ha='right')
    ax.set_xlim(-1.3, 1.5)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    _guardar(fig, nombre)


def respuesta_identificacion(nombre='respuesta_identificacion',
                             K=0.4, zeta=0.1479, wn=1.44, amplitud=2.0,
                             t_fin=14.0):
    """Respuesta al escalon del modelo identificado en el ejemplo.

    Reproduce el trazo del cuaderno: escalon de amplitud 2, y_ss = 0.8,
    pico 1.3 en t_p = 2.2 s.
    """
    sig = zeta * wn
    wd = wn * np.sqrt(1 - zeta ** 2)
    t = np.linspace(0, t_fin, 1200)
    yss = K * amplitud
    y = yss * (1 - np.exp(-sig * t) * (np.cos(wd * t) + (sig / wd) * np.sin(wd * t)))
    tp = np.pi / wd
    yp = yss * (1 + np.exp(-zeta * np.pi / np.sqrt(1 - zeta ** 2)))

    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    ax.plot(t, y, color='black', lw=1.3)
    ax.axhline(yss, color='0.5', lw=0.9, ls='--')
    ax.plot([tp], [yp], 'o', ms=4, color='black')
    ax.annotate(f'$y_p$ = {yp:.2f}', (tp, yp), textcoords='offset points',
                xytext=(8, 2), fontsize=8)
    ax.annotate(f'$y_{{ss}}$ = {yss:.1f}', (t_fin, yss),
                textcoords='offset points', xytext=(-6, 6),
                fontsize=8, ha='right')
    ax.set_xlabel('t [s]')
    ax.set_ylabel('y(t)')
    ax.set_title('Respuesta del modelo identificado (escalón de amplitud 2)',
                 fontsize=9)
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)
    _guardar(fig, nombre)


if __name__ == '__main__':
    mapeo_s_z()
    muestreo_aliasing()
    control_onoff()
    plano_z_polos()
    respuesta_identificacion()
