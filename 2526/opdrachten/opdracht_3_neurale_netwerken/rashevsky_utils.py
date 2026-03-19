import numpy as np
import matplotlib.pyplot as plt


def plot_time_series_comparison(simulate_rashevsky, params_list, names, x0=(0.0, 1.0), t=None):
    if t is None:
        t = np.linspace(0, 25, 1000)

    fig, axes = plt.subplots(len(params_list), 1, figsize=(8, 4 * len(params_list)), sharex=True)
    if len(params_list) == 1:
        axes = [axes]

    for ax, params, name in zip(axes, params_list, names):
        sol = simulate_rashevsky(x0, t, params)
        ax.plot(t, sol[:, 0], label="e1(t)", linewidth=2)
        ax.plot(t, sol[:, 1], label="e2(t)", linewidth=2, linestyle="--")
        ax.set_title(name)
        ax.set_ylabel("activation")
        ax.set_ylim(0, 1.0)
        ax.legend()

    axes[-1].set_xlabel("time")
    plt.tight_layout()
    plt.show()


def plot_many_initial_conditions(simulate_rashevsky, params, title, grid=None, t=None):
    if grid is None:
        grid = np.linspace(0, 1.2, 7)
    if t is None:
        t = np.linspace(0, 25, 1000)

    plt.figure(figsize=(8, 5))
    for e0 in grid:
        sol = simulate_rashevsky([e0, e0], t, params)
        plt.plot(t, sol[:, 0], alpha=0.8, label=f"{e0:.2f}")

    plt.xlabel("time")
    plt.ylabel("activation")
    plt.title(title)
    plt.legend(title="initial e1=e2", ncol=2, fontsize=8)
    plt.show()


def plot_phase_plane_trajectories(simulate_rashevsky, params, initials, t=None, title="Phase plane trajectories"):
    if t is None:
        t = np.linspace(0, 25, 1000)

    plt.figure(figsize=(6, 6))
    for x0 in initials:
        sol = simulate_rashevsky(x0, t, params)
        plt.plot(sol[:, 0], sol[:, 1], label=f"{x0}")
        arrow_idx = max(8, len(sol) // 10)
        plt.annotate(
            "",
            xy=(sol[arrow_idx + 3, 0], sol[arrow_idx + 3, 1]),
            xytext=(sol[arrow_idx - 3, 0], sol[arrow_idx - 3, 1]),
            arrowprops=dict(arrowstyle="->", color="black", lw=1),
        )
        plt.scatter(sol[0, 0], sol[0, 1], s=20)
        plt.scatter(sol[-1, 0], sol[-1, 1], s=30)

    plt.xlabel("e1")
    plt.ylabel("e2")
    plt.title(title)
    plt.legend()
    plt.axis("equal")
    plt.show()


def plot_rashevsky_paper_phase_portrait(simulate_rashevsky_paper, params, t=None, x_max=1.5, highlighted_initial=(0.0, 0.9779547)):
    if t is None:
        t = np.linspace(0, 10, 1000)

    x = np.linspace(0, 4, 400)
    A = params["A"]
    alpha = params["alpha"]
    h1 = params["h1"]
    h2 = params["h2"]

    e1_nullcline = A * (1.0 - np.exp(-alpha * np.maximum(0.0, x - h2)))
    e2_nullcline_input = A * (1.0 - np.exp(-alpha * np.maximum(0.0, x - h1)))

    plt.figure(figsize=(7, 7))
    plt.plot(x, e1_nullcline, linewidth=2, label=r"$\dot e_1 = 0$")
    plt.plot(e2_nullcline_input, x, linestyle="--", linewidth=2, label=r"$\dot e_2 = 0$")

    c0 = np.arange(0, x_max + 1e-9, 0.25)
    for e0 in c0:
        for x0 in ([e0, 0.0], [e0, x_max], [0.0, e0], [x_max, e0]):
            sol = simulate_rashevsky_paper(x0, t, params)
            plt.plot(sol[:, 0], sol[:, 1], color="black", alpha=0.55, linewidth=1)

    sol_highlight = simulate_rashevsky_paper(highlighted_initial, t, params)
    plt.plot(
        sol_highlight[:, 0],
        sol_highlight[:, 1],
        linestyle=":",
        linewidth=2.5,
        color="tab:red",
        label=f"highlighted trajectory: {highlighted_initial}",
    )

    plt.xlim(0, x_max)
    plt.ylim(0, x_max)
    plt.xlabel("e1")
    plt.ylabel("e2")
    plt.title("Paper-style phase portrait for the symmetric Rashevsky model")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.show()


def plot_nullclines(rashevsky_rhs, params, e1_range=(0, 1.5), e2_range=(0, 1.5), n=300, title="Nullclines"):
    e1_vals = np.linspace(*e1_range, n)
    e2_vals = np.linspace(*e2_range, n)
    E1g, E2g = np.meshgrid(e1_vals, e2_vals)

    U = np.zeros_like(E1g)
    V = np.zeros_like(E2g)

    for i in range(n):
        for j in range(n):
            de1dt, de2dt = rashevsky_rhs([E1g[i, j], E2g[i, j]], 0, params)
            U[i, j] = de1dt
            V[i, j] = de2dt

    plt.figure(figsize=(6, 6))
    plt.contour(E1g, E2g, U, levels=[0], linewidths=2)
    plt.contour(E1g, E2g, V, levels=[0], linewidths=2)
    plt.xlabel("e1")
    plt.ylabel("e2")
    plt.title(title)
    plt.xlim(e1_range)
    plt.ylim(e2_range)
    plt.show()


def plot_r_style_inhibitory_phase_portrait(simulate_inhibitory, params, t=None, x_plot_max=1.5, x_curve_max=4.0, highlighted_initial=(0.0, 0.9779547)):
    if t is None:
        t = np.linspace(0, 40, 4000)

    x = np.linspace(0, x_curve_max, 400)
    e1_curve = 1.0 - np.exp(-params["a"] * np.maximum(0.0, x - params["h2"]))
    e2_curve_input = np.exp(-params["a"] * np.maximum(0.0, x - params["h1"]))

    plt.figure(figsize=(6, 6))
    plt.plot(x, e1_curve, linewidth=2, color="black")
    plt.plot(e2_curve_input, x, linestyle="--", linewidth=2, color="black")

    c0 = np.arange(0, x_plot_max + 1e-9, 0.25)
    for e0 in c0:
        for x0 in ([e0, 0.0], [e0, x_plot_max], [0.0, e0], [x_plot_max, e0]):
            sol = simulate_inhibitory(x0, t, params)
            plt.plot(sol[:, 0], sol[:, 1], color="0.35", linewidth=0.9)

    sol_highlight = simulate_inhibitory(highlighted_initial, t, params)
    plt.plot(sol_highlight[:, 0], sol_highlight[:, 1], linestyle=":", linewidth=2, color="tab:red")

    plt.xlim(0, x_plot_max)
    plt.ylim(0, x_plot_max)
    plt.xlabel("e2")
    plt.ylabel("e1")
    plt.grid(alpha=0.15)
    plt.show()


def plot_inhibitory_alpha_sweep(simulate_inhibitory, params_inhibitory, alphas, t=None, x_plot_max=1.5, x_curve_max=4.0, highlighted_initial=(0.0, 0.9779547)):
    if t is None:
        t = np.linspace(0, 40, 4000)

    fig, axes = plt.subplots(1, len(alphas), figsize=(4 * len(alphas), 4), sharey=True)

    for ax, alpha in zip(axes, alphas):
        params = params_inhibitory.copy()
        params["alpha"] = alpha

        x = np.linspace(0, x_curve_max, 400)
        e1_curve = 1.0 - np.exp(-params["a"] * np.maximum(0.0, x - params["h2"]))
        e2_curve_input = np.exp(-params["a"] * np.maximum(0.0, x - params["h1"]))
        ax.plot(x, e1_curve, linewidth=2, color="black")
        ax.plot(e2_curve_input, x, linestyle="--", linewidth=2, color="black")

        c0 = np.arange(0, x_plot_max + 1e-9, 0.25)
        for e0 in c0:
            for x0 in ([e0, 0.0], [e0, x_plot_max], [0.0, e0], [x_plot_max, e0]):
                sol = simulate_inhibitory(x0, t, params)
                ax.plot(sol[:, 0], sol[:, 1], color="0.35", linewidth=0.8)

        sol_highlight = simulate_inhibitory(highlighted_initial, t, params)
        ax.plot(sol_highlight[:, 0], sol_highlight[:, 1], color="tab:red", linestyle=":", linewidth=2)
        ax.set_title(f"alpha = {alpha}")
        ax.set_xlabel("e2")
        ax.set_ylabel("e1")
        ax.set_xlim(0, x_plot_max)
        ax.set_ylim(0, x_plot_max)
        ax.grid(alpha=0.15)

    plt.tight_layout()
    plt.show()
