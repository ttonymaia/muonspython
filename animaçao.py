import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import poisson

# Parâmetros da área e múons
area_size = 1.0
mean_muons_per_frame = 100  # λ: Média de múons por frame
frames = 50  # Número de frames na animação

# Configuração inicial
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-area_size / 2, area_size / 2)
ax.set_ylim(-area_size / 2, area_size / 2)
ax.set_title("Animação: Múons Atingindo uma Área de 1 m²")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
scat = ax.scatter([], [], s=1, alpha=0.5, color='blue')

# Função de atualização para animação
def update(frame):
    # Número de múons por frame baseado na distribuição de Poisson
    num_muons = poisson.rvs(mean_muons_per_frame)
    
    # Gerar posições x e y para os múons
    x = np.random.uniform(-area_size / 2, area_size / 2, num_muons)
    y = np.random.uniform(-area_size / 2, area_size / 2, num_muons)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Criar a animação
ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=True)
plt.show()
