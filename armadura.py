import numpy as np
import matplotlib.pyplot as plt

# Parâmetros gerais
bloco_comprimento = 200  # Comprimento do bloco (cm)
bloco_largura = 100  # Largura do bloco (cm)
n_muons = 50000000  # Número de múons simulados
detector_resolucao = (200, 100)  # Resolução do detector (pixels)
mu_concreto = 0.015  # Coeficiente de atenuação para concreto
mu_armadura = 0.045  # Coeficiente de atenuação para armadura

# Criar uma matriz representando o bloco com armadura
def criar_armadura(res_x, res_y):
    bloco = np.full((res_x, res_y), mu_concreto)
    # Inserindo barras de armadura como regiões mais densas
    bloco[80:120, :] = mu_armadura  # Barra horizontal no meio
    bloco[:, 40:60] = mu_armadura  # Barra vertical no centro
    return bloco

# Gerar a trajetória dos múons
def simular_muons(n_muons, comprimento, largura):
    origem_x = np.random.uniform(0, comprimento, n_muons)
    origem_y = np.random.uniform(0, largura, n_muons)
    return origem_x, origem_y

# Simular a muongrafia
def gerar_muongrafia(muons_x, muons_y, bloco, res_x, res_y, comprimento, largura):
    muongrafia = np.zeros((res_x, res_y))
    x_bins = np.linspace(0, comprimento, res_x + 1)
    y_bins = np.linspace(0, largura, res_y + 1)

    for x, y in zip(muons_x, muons_y):
        x_idx = np.digitize(x, x_bins) - 1
        y_idx = np.digitize(y, y_bins) - 1
        if 0 <= x_idx < res_x and 0 <= y_idx < res_y:
            muongrafia[x_idx, y_idx] += np.exp(-bloco[x_idx, y_idx])  # Atenuação no ponto

    return muongrafia

# Criar o bloco com armadura
bloco = criar_armadura(detector_resolucao[0], detector_resolucao[1])

# Gerar os múons
muons_x, muons_y = simular_muons(n_muons, bloco_comprimento, bloco_largura)

# Gerar a imagem de muongrafia
muongrafia = gerar_muongrafia(muons_x, muons_y, bloco, detector_resolucao[0], detector_resolucao[1], bloco_comprimento, bloco_largura)

# Visualizar o bloco com armadura e a muongrafia
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Bloco com armadura (coeficientes de atenuação)
ax[0].imshow(bloco.T, cmap='gray', origin='lower', extent=[0, bloco_comprimento, 0, bloco_largura])
ax[0].set_title("Estrutura Interna do Bloco (Armadura)")
ax[0].set_xlabel("Comprimento (cm)")
ax[0].set_ylabel("Largura (cm)")

# Projeção da muongrafia
ax[1].imshow(muongrafia.T, cmap='viridis', origin='lower', extent=[0, bloco_comprimento, 0, bloco_largura])
ax[1].set_title("Muongrafia Simulada")
ax[1].set_xlabel("Comprimento (cm)")
ax[1].set_ylabel("Largura (cm)")

plt.tight_layout()
plt.show()
