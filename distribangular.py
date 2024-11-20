import matplotlib.pyplot as plt
import numpy as np

# Número de múons
num_muons = 10000

# Distribuição angular (ângulos em radianos)
angles = np.random.uniform(0, np.pi/2, num_muons)

# Plotar histograma dos ângulos
plt.figure(figsize=(8, 6))
plt.hist(angles, bins=50, density=True, alpha=0.7, color='green', label="Distribuição Angular")
plt.title("Distribuição Angular dos Múons")
plt.xlabel("Ângulo (radianos)")
plt.ylabel("Densidade")
plt.legend()
plt.grid()
plt.show()
