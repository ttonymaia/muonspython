import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
ax.set_title("Múon Passando por Região de Alta Densidade", fontsize=14)
ax.set_xlabel("Distância")
ax.set_ylabel("Energia (MeV)")

# Trajetória do múon
x_data = []
y_data = []
absorbed = False

line, = ax.plot([], [], color="purple", label="Múon")
ax.legend()

# Partículas densas
particles_x = np.random.uniform(10, 15, 50)
particles_y = np.random.uniform(2, 8, 50)
particles, = ax.plot([], [], 'ro', label="Partículas Densas")

# Função de atualização da animação
def update_high_density(frame):
    global absorbed
    if absorbed:
        return line, particles

    x_data.append(frame)
    # Simulando atenuação
    if frame < 10:
        y_data.append(4.0)  # Energia constante até entrar na região densa
    elif frame < 15:
        attenuation = 0.015  # Coeficiente de atenuação
        y_data.append(max(0, y_data[-1] - attenuation))
    else:
        if y_data[-1] <= 0.2:  # Energia quase zero, múon absorvido
            absorbed = True
        y_data.append(max(0, y_data[-1] - 0.05))  # Absorção final

    line.set_data(x_data, y_data)
    particles.set_data(particles_x, particles_y)
    return line, particles

ani = FuncAnimation(fig, update_high_density, frames=np.linspace(0, 20, 100), interval=50, blit=True)
plt.show()
