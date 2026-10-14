'''zadanie domowe:
porównanie estymatorów przy użyciu symulacji montecarlo:
- generujemy próbkę z rozkładu norm(1, 2), N=1000
- liczymy estymator mi1 (empiryczna średnia z próby)
- liczymy mi2 = pierwsza obserwacja z próby
- liczymy mi3 = mediane z próby
powtarzamy tę pentlę M=10000 razy
potem rysujemy boxplot i porównujemy rozkłady estymatorów'''

import numpy as np
import matplotlib.pyplot as plt

M = 10000
mi_1_l = []
mi_2_l = []
mi_3_l = []
for i in range(M):
    x_i = np.random.normal(1, 2, 1000)
    mi_1_l.append(np.mean(x_i))
    mi_2_l.append(x_i[0])
    mi_3_l.append(np.median(x_i))

plt.figure(figsize=(9, 6))
plt.boxplot(
    [mi_1_l, mi_2_l, mi_3_l],
    tick_labels=["Średnia ($\mu_1$)", "1. obserwacja ($\mu_2$)", "Mediana ($\mu_3$)"],)

plt.axhline(1, color="red", linestyle="--", label="Prawdziwe $\mu = 1$")
plt.title("Porównanie estymatorów (Monte Carlo)")
plt.ylabel("Wartość estymatora")
plt.grid(axis="y", linestyle=":", alpha=0.6)
plt.legend()
plt.show()



