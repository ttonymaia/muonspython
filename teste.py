import numpy as np
import matplotlib.pyplot as plt

# Dimensões do bloco (cm)
comprimento = 39  # comprimento total
altura = 19       # altura total
espessura = 3     # espessura das paredes
comprimento_furo = 14  # comprimento dos furos
largura_furo = 6       # largura dos furos

# Configuração do grid
resolucao = 0.5  # cm
x = np.arange(0, comprimento, resolucao)
y = np.arange(0, altura, resolucao)
bloco = np.ones((len(y), len(x)))  # Concreto inicial

# Adicionar os furos ao bloco
x_furo1_ini, x_furo1_fim = espessura, espessura + comprimento_furo
x_furo2_ini, x_furo2_fim = comprimento - comprimento_furo - espessura, comprimento - espessura
y_furo_ini, y_furo_fim = espessura, espessura + largura_furo

for i in range(len(x)):
    for j in range(len(y)):
        if (x_furo1_ini <= x[i] <= x_furo1_fim and y_furo_ini <= y[j] <= y_furo_fim) or \
           (x_furo2_ini <= x[i] <= x_furo2_fim and y_furo_ini <= y[j] <= y_furo_fim):
            bloco[j, i] = 0.2  # Menor atenuação nos furos

# Configuração dos múons
np.random.seed(42)
n_muons = 10000
coef_atenuacao = 0.015
trajetorias = np.random.uniform(0, comprimento, n_muons)  # Posições iniciais dos múons

# Simular a interação dos múons com o bloco
sinal_detector = np.zeros(len(x))
for i, pos in enumerate(trajetorias):
    coluna = int(pos / resolucao)
    for j in range(len(y)):
        sinal_detector[coluna] += bloco[j, coluna] * coef_atenuacao

# Normalizar o sinal do detector
sinal_detector = sinal_detector / np.max(sinal_detector)

# Reconstrução da imagem a partir do sinal
imagem_reconstruida = np.tile(sinal_detector, (len(y), 1))

# Visualizar os resultados
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Vista do bloco original
axes[0].imshow(bloco, extent=[0, comprimento, 0, altura], origin="lower", cmap="gray", alpha=0.8)
axes[0].set_title("Bloco Original")
axes[0].set_xlabel("Comprimento (cm)")
axes[0].set_ylabel("Altura (cm)")

# Sinal do detector
axes[1].plot(x, sinal_detector, color="blue")
axes[1].fill_between(x, 0, sinal_detector, color="blue", alpha=0.3)
axes[1].set_title("Sinal do Detector")
axes[1].set_xlabel("Posição Horizontal (cm)")
axes[1].set_ylabel("Intensidade Normalizada")
axes[1].grid()

# Imagem reconstruída
axes[2].imshow(imagem_reconstruida, extent=[0, comprimento, 0, altura], origin="lower", cmap="viridis", aspect="auto")
axes[2].set_title("Imagem Reconstruída")
axes[2].set_xlabel("Comprimento (cm)")
axes[2].set_ylabel("Altura (cm)")

plt.tight_layout()
plt.show()
