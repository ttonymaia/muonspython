import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Número de múons simulados
num_muons = 500  # Escolha um número menor para a animação ser mais leve

# Gerando ângulos zenitais (em radianos) com distribuição cos²(θ)
theta = np.arccos(np.sqrt(np.random.uniform(0, 1, num_muons)))  # Distribuição cos²(θ)

# Gerando ângulos azimutais uniformemente distribuídos (0 a 2π)
phi = np.random.uniform(0, 2 * np.pi, num_muons)

# Velocidades e direções dos múons
vx = np.sin(theta) * np.cos(phi)  # Componente x
vy = np.sin(theta) * np.sin(phi)  # Componente y
vz = -np.cos(theta)  # Componente z (múons descem, então negativo)

# Posição inicial (x, y, z) para todos os múons
x = np.random.uniform(-0.5, 0.5, num_muons)  # Largura da área (1 m²)
y = np.random.uniform(-0.5, 0.5, num_muons)  # Comprimento da área (1 m²)
z = np.ones(num_muons) * 5  # Começam a 5 metros de altura

# Preparar o gráfico
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 5])
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Simulação de Múons Descendo em Ângulos Aleatórios")

# Atualização dos frames da animação
def update(frame):
    global x, y, z
    ax.cla()  # Limpa o gráfico
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([0, 5])
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.set_title("Simulação de Múons Descendo em Ângulos Aleatórios")

    # Atualizando posições
    x += vx * 0.1  # Passo pequeno na direção x
    y += vy * 0.1  # Passo pequeno na direção y
    z += vz * 0.1  # Passo pequeno na direção z

    # Removendo múons que atravessam o plano Z=0
    mask = z > 0
    x, y, z = x[mask], y[mask], z[mask]

    # Plotando os múons restantes
    ax.scatter(x, y, z, color="blue", s=5, label="Múons")
    ax.legend()

# Criar animação
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
