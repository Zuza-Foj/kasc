import numpy as np
import matplotlib.pyplot as plt

b0 = 2
b1 = 0.5
l_bi = []
M = 5000
l_n = [20, 50, 100, 500]
c = np.sqrt(12/5)


def losuj_blad(model, n):
    if model == 1:
        return np.random.normal(0, np.sqrt(3), n)
    elif model == 2:
        return np.random.standard_t(3, n)
    else:
        return c * np.random.standard_t(10, n)

naz_mod = {1: "N(0,3)", 2: "$t_3$", 3: "$c \\cdot t_{10}$"}

wyn = {}
for model in [1, 2, 3]:
    for n in l_n:
        l_bi = []
        x = np.linspace(1/n, 1, n)
        for j in range(M):
            e = losuj_blad(model, n)
            y = b0 + b1*x + e
            bi = np.polyfit(x, y, 1)
            l_bi.append(bi)
        l_bi = np.array(l_bi)
        wyn[(model, n)] = l_bi

        b1_hat = l_bi[:, 0]
        b0_hat = l_bi[:, 1]
        print(f"model {naz_mod[model]:>12}, n={n:>3} | "
              f"obciążenie b0: {np.mean(b0_hat) - b0:+.4f}, "
              f"b1: {np.mean(b1_hat) - b1:+.4f} | "
              f"wariancja b0: {np.var(b0_hat, ddof=1):.4f}, "
              f"b1: {np.var(b1_hat, ddof=1):.4f}")

for kol, nazwa_par, prawdziwa in [(1, "$\\hat\\beta_0$", b0), (0, "$\\hat\\beta_1$", b1)]:
    fig, osie = plt.subplots(1, 4, figsize=(16, 4))
    for ax, n in zip(osie, l_n):
        dane = [wyn[(model, n)][:, kol] for model in [1, 2, 3]]
        ax.boxplot(dane, labels=[naz_mod[m] for m in [1, 2, 3]])
        ax.axhline(prawdziwa, color="red", linestyle="--")
        ax.set_title(f"n = {n}")
        ax.set_xlabel("rozkład błędu")
        ax.set_ylabel(f"estymator {nazwa_par}")
    plt.tight_layout()
    plt.show()

