import numpy as np
import matplotlib.pyplot as plt

# Dimensões da estrutura (em cm)
width, height = 39, 19

# Matriz da estrutura: 1 para concreto, 0 para furos, 2 para barras de aço
structure = np.ones((height, width))

# Criar furos no bloco (exemplo para blocos com dois furos grandes)
structure[5:14, 10:15] = 0  # Furo 1
structure[5:14, 24:29] = 0  # Furo 2

# Adicionar barras de aço (regiões muito densas)
structure[8:10, 6:33] = 2  # Barra horizontal
structure[2:17, 18:20] = 2  # Barra vertical

# Parâmetros de atenuação
attenuation_factors = {0: 1.0, 1: 0.8, 2: 0.5}  # Furo, concreto, aço
signal = np.zeros_like(structure, dtype=float)

# Simular o sinal do detector com base na atenuação
for i in range(height):
    for j in range(width):
        material = structure[i, j]
        signal[i, j] = attenuation_factors[material]

# Visualização
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Mapa da estrutura
ax[0].imshow(structure, cmap="coolwarm", origin="lower")
ax[0].set_title("Estrutura do Bloco")
ax[0].set_xlabel("Largura (cm)")
ax[0].set_ylabel("Altura (cm)")
ax[0].grid(False)

# Sinais do detector
im = ax[1].imshow(signal, cmap="viridis", origin="lower")
ax[1].set_title("Sinais de Detecção")
ax[1].set_xlabel("Largura (cm)")
ax[1].set_ylabel("Altura (cm)")
ax[1].grid(False)

# Barra de cores para os sinais
cbar = plt.colorbar(im, ax=ax[1])
cbar.set_label("Intensidade do Sinal")

plt.tight_layout()
plt.show()
