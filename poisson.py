import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Taxa de múons por minuto (esperança λ)
lambda_muons = 10000  # múons/min

# Gerar valores de 0 a 15000 múons
x = np.arange(0, 15000, 1)

# Distribuição de Poisson
poisson_dist = poisson.pmf(x, lambda_muons)

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, poisson_dist, marker='o', linestyle='', markersize=2, label=f"λ = {lambda_muons}")
plt.title("Distribuição de Poisson - Contagem de Múons por Minuto")
plt.xlabel("Número de múons")
plt.ylabel("Probabilidade")
plt.legend()
plt.grid()
plt.show()
