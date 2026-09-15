"""Figuras de los scripts de clase traducidos de MATLAB
(clase1.m, clase2.m, clase3.m, clase4.slx -> ver capitulos 02 y 05).

    python3 clases_matlab.py   ->  genera los .svg y los .pdf
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import control as ct

DEN1 = np.polymul([1, 2], [1, 1, 8])      # (s+2)(s^2+s+8)


def _limpiar(ax):
    ax.grid(True, ls=':', lw=0.5, color='0.85')
    for lado in ('top', 'right'):
        ax.spines[lado].set_visible(False)


def _guardar(fig, nombre):
    fig.tight_layout()
    for ext in ('.svg', '.pdf'):
        fig.savefig(nombre + ext, transparent=True)
    plt.close(fig)


def cero_origen(nombre='clase1_cero_origen'):
    """clase1.m: G = s/[(s+2)(s^2+s+8)]. El cero en el origen anula la
    ganancia de DC: el escalon vuelve a cero."""
    G = ct.tf([1, 0], DEN1)
    Gsin = ct.tf([ct.dcgain(ct.tf([1], DEN1))*0 + 1], DEN1)   # mismo denominador
    t = np.linspace(0, 12, 2000)
    _, y = ct.step_response(G, t)
    _, y2 = ct.step_response(Gsin/ct.dcgain(Gsin), t)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9),
                                 gridspec_kw={'width_ratios': [1, 1.25]})

    p = G.poles()
    a1.axhline(0, color='0.6', lw=0.8)
    a1.axvline(0, color='0.6', lw=0.8)
    a1.plot(p.real, p.imag, ls='none', marker='x', ms=9, mew=1.6, color='black')
    a1.plot([0], [0], ls='none', marker='o', ms=8, mfc='none', mec='black')
    a1.annotate('cero en\nel origen', (0, 0), textcoords='offset points',
                xytext=(-46, -30), fontsize=7.5, color='0.4')
    a1.set_xlabel(r'$\sigma$')
    a1.set_ylabel(r'$j\omega$')
    a1.set_xlim(-2.6, 0.8)
    a1.set_title('polos y ceros', fontsize=10)

    a2.axhline(0, color='0.7', lw=0.8, ls=':')
    a2.plot(t, y, color='black', lw=1.3, label=r'$G=\dfrac{s}{(s+2)(s^2+s+8)}$')
    a2.plot(t, y2, color='0.6', lw=1.0, ls='--',
            label='sin el cero (normalizada)')
    a2.set_xlabel('$t$ [s]')
    a2.set_ylabel('$y(t)$')
    a2.set_title('respuesta al escalón', fontsize=10)
    a2.set_ylim(-0.2, 1.95)
    a2.legend(fontsize=7.5, frameon=False, loc='upper right')

    for ax in (a1, a2):
        _limpiar(ax)
    _guardar(fig, nombre)


def estabilidad(nombre='clase3_estabilidad'):
    """clase3: un signo de diferencia entre 1/(s^2+4) y 1/(s^2-s+4) separa
    la oscilacion sostenida de la divergente."""
    t = np.linspace(0, 12, 3000)
    y_marg = (1 - np.cos(2*t))/4                     # de 1/[s(s^2+4)]
    r15 = np.sqrt(15)
    y_ines = (0.25 - np.exp(t/2)*np.cos(r15*t/2)/4
              + r15*np.exp(t/2)*np.sin(r15*t/2)/60)  # de 1/[s(s^2-s+4)]

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(5.4, 3.8), sharex=True)
    a1.plot(t, y_marg, color='black', lw=1.2)
    a1.set_ylabel('$y(t)$')
    a1.set_title(r'$G=\frac{1}{s^2+4}$: polos en $\pm 2j$, oscilación sostenida',
                 fontsize=9.5)
    a2.plot(t, y_ines, color='black', lw=1.2)
    a2.set_ylabel('$y(t)$')
    a2.set_xlabel('$t$ [s]')
    a2.set_title(r'$G=\frac{1}{s^2-s+4}$: polos en $0.5\pm1.936j$, diverge',
                 fontsize=9.5)
    a2.set_yscale('symlog', linthresh=1)
    for ax in (a1, a2):
        ax.axhline(0, color='0.7', lw=0.8, ls=':')
        _limpiar(ax)
    _guardar(fig, nombre)


def pid_clase(nombre='clase2_pid'):
    """clase2.m: K=386, Ti=900, Td=1000 contra una sintonia diseñada."""
    G = ct.tf([1, 3], DEN1)
    Gc_cl = ct.tf([386*1000, 386, 386/900], [1, 0])
    Gc_di = ct.tf([7.5, 22, 59], [1, 0])
    T_cl = ct.feedback(Gc_cl*G, 1)
    T_di = ct.feedback(Gc_di*G, 1)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.9))

    t1 = np.linspace(0, 6, 3000)
    _, y_cl = ct.step_response(T_cl, t1)
    _, y_di = ct.step_response(T_di, t1)
    a1.axhline(1, color='0.7', lw=0.8, ls=':')
    a1.plot(t1, y_cl, color='0.55', lw=1.2, ls='--', label='clase: $T_d=1000$')
    a1.plot(t1, y_di, color='black', lw=1.3, label='diseñada')
    a1.set_xlabel('$t$ [s]')
    a1.set_ylabel('$y(t)$')
    a1.set_title('primeros 6 s: las dos "funcionan"', fontsize=9.5)
    a1.legend(fontsize=8, frameon=False, loc='lower right')

    t2 = np.linspace(0, 9000, 40000)
    _, y_cl2 = ct.step_response(T_cl, t2)
    _, y_di2 = ct.step_response(T_di, t2)
    a2.axhline(1, color='0.7', lw=0.8, ls=':')
    a2.axhspan(0.995, 1.005, color='0.9', label='banda $\\pm0.5$ %')
    a2.plot(t2/60, y_cl2, color='0.55', lw=1.2, ls='--')
    a2.plot(t2/60, y_di2, color='black', lw=1.3)
    a2.set_xlabel('$t$ [minutos]')
    a2.set_ylabel('$y(t)$')
    a2.set_ylim(0.985, 1.004)
    a2.set_title('la cola lenta: 34 min hasta el 0.5 %', fontsize=9.5)
    a2.legend(fontsize=8, frameon=False, loc='lower right')

    for ax in (a1, a2):
        _limpiar(ax)
    _guardar(fig, nombre)


def onoff_ruido(nombre='clase4_onoff_ruido'):
    """clase4.slx: rele + ruido. La histeresis es lo que evita el
    castañeteo cuando la medida tiene ruido."""
    T, N = 0.01, 3000
    tau, K, SP = 2.0, 1.0, 50.0
    Umax, Umin = 100.0, 0.0
    a, b = np.exp(-T/tau), K*(1-np.exp(-T/tau))

    def sim(delta, sigma, seed=11):
        rng = np.random.default_rng(seed)
        y = np.zeros(N); u = np.zeros(N); u[0] = Umax; sw = 0
        for k in range(1, N):
            m = y[k-1] + (rng.normal(0, sigma) if sigma else 0.0)
            if m > SP + delta:
                nu = Umin
            elif m < SP - delta:
                nu = Umax
            else:
                nu = u[k-1]
            sw += (nu != u[k-1])
            u[k] = nu
            y[k] = a*y[k-1] + b*u[k-1]
        return y, u, sw

    t = np.arange(N)*T
    fig, ax = plt.subplots(2, 2, figsize=(6.4, 3.8))
    for col, (d, s, tit) in enumerate((
            (0.0, 0.8, 'sin histéresis, medida con ruido'),
            (1.5, 0.8, 'con histéresis $\\pm1.5$'))):
        y, u, sw = sim(d, s)
        ax[0][col].axhline(SP, color='0.7', lw=0.8, ls=':')
        if d:
            ax[0][col].axhspan(SP-d, SP+d, color='0.9')
        ax[0][col].plot(t, y, color='black', lw=1.0)
        ax[0][col].set_ylim(0, 70)
        ax[0][col].set_title(tit, fontsize=9)
        vent = (t >= 20) & (t <= 24)
        ax[1][col].plot(t[vent], u[vent], color='black', lw=0.8)
        ax[1][col].set_xlabel('$t$ [s]  (ventana ampliada)')
        ax[1][col].set_ylim(-10, 135)
        ax[1][col].set_xlim(20, 24)
        ax[1][col].annotate(f'{sw/(N*T):.0f} conmutaciones/s', (20.1, 118),
                            fontsize=8, color='0.35')
    ax[0][0].set_ylabel('$y(t)$')
    ax[1][0].set_ylabel('$u(t)$')
    for fila in ax:
        for a_ in fila:
            _limpiar(a_)
    _guardar(fig, nombre)


if __name__ == '__main__':
    cero_origen()
    estabilidad()
    pid_clase()
    onoff_ruido()
