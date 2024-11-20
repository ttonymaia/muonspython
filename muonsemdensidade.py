import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
ax.set_title("Múon Passando por Região de Baixa Densidade", fontsize=14)
ax.set_xlabel("Distância")
ax.set_ylabel("Energia (MeV)")

# Trajetória do múon
x_data = []
y_data = []

line, = ax.plot([], [], color="blue", label="Múon")
ax.legend()

# Função de atualização da animação
def update_low_density(frame):
    x_data.append(frame)
    y_data.append(4.0)  # Energia constante (4 GeV = 4000 MeV)
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update_low_density, frames=np.linspace(0, 20, 100), interval=50, blit=True)
plt.show()
