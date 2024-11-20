import matplotlib.pyplot as plt
import numpy as np

# Dimensão da área em m² (1x1 m)
area_size = 1.0
num_muons = 10000  # Número de múons por minuto

# Coordenadas x, y aleatórias para os múons
x = np.random.uniform(-area_size/2, area_size/2, num_muons)
y = np.random.uniform(-area_size/2, area_size/2, num_muons)

# Plotar os múons atingindo a superfície
plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=1, alpha=0.5, color='blue', label="Múons")
plt.title("Múons Atingindo uma Área de 1 m²")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()
plt.show()
