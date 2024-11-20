import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações básicas
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-50, 50)
ax.set_ylim(0, 150)
ax.set_title("Bombardeio de Raios Cósmicos e Geração de Múons", fontsize=14)
ax.set_xlabel("Posição Horizontal (km)")
ax.set_ylabel("Altura (km)")

# Desenhando camadas da atmosfera e da Terra
atmosfera = plt.Rectangle((-50, 50), 100, 100, color='skyblue', alpha=0.5, label='Atmosfera')
terra = plt.Rectangle((-50, 0), 100, 50, color='green', label='Terra')
ax.add_patch(atmosfera)
ax.add_patch(terra)

# Dados iniciais
raios = []  # Lista para raios cósmicos
muons = []  # Lista para múons gerados
n_raios_por_minuto = 15000  # Aproximadamente 1,5x o número de múons esperados
n_frames = 100  # Número de frames
tempo_minuto = 60  # Simulação de 1 minuto em segundos
taxa_muons_por_raio = 2  # Cada raio gera 2 múons em média

# Função para atualizar os frames da animação
def update(frame):
    ax.clear()
    ax.set_xlim(-50, 50)
    ax.set_ylim(0, 150)
    ax.set_title("Bombardeio de Raios Cósmicos e Geração de Múons", fontsize=14)
    ax.set_xlabel("Posição Horizontal (km)")
    ax.set_ylabel("Altura (km)")

    # Desenhar atmosfera e Terra
    ax.add_patch(plt.Rectangle((-50, 50), 100, 100, color='skyblue', alpha=0.5, label='Atmosfera'))
    ax.add_patch(plt.Rectangle((-50, 0), 100, 50, color='green', label='Terra'))

    # Adicionar raios cósmicos
    for r in raios:
        ax.plot(r[0], r[1], color='orange', linewidth=1, label='Raio Cósmico' if frame == 0 else "")

    # Adicionar múons
    for m in muons:
        ax.plot(m[0], m[1], color='purple', linewidth=1, linestyle='--', label='Múon' if frame == 0 else "")

    # Atualizando posição dos raios
    for r in raios:
        r[1][1] -= 1  # Mover o raio para baixo
    raios[:] = [r for r in raios if r[1][1] > 50]  # Remover raios que saíram do campo de visão

    # Gerar novos raios a partir do espaço
    if frame % 2 == 0:  # Simular novos raios a cada 2 frames
        for _ in range(n_raios_por_minuto // (tempo_minuto * n_frames)):
            x_start = np.random.uniform(-50, 50)
            raios.append(([x_start, x_start], [150, 100]))

    # Gerar múons na atmosfera
    for r in raios:
        if r[1][1] <= 100:  # Quando o raio atinge a atmosfera
            for _ in range(taxa_muons_por_raio):  # Cada raio gera dois múons em média
                angle = np.random.uniform(-0.5, 0.5)  # Ângulo de dispersão
                x_start = r[0][1]
                x_end = x_start + np.tan(angle) * 100
                muons.append(([x_start, x_end], [100, 0]))
            raios.remove(r)  # Remover raio após interação

    ax.legend(loc='upper left')

# Criando a animação
ani = FuncAnimation(fig, update, frames=n_frames, interval=100)

plt.show()
