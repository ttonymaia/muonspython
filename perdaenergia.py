import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
energia_inicial = 4.0  # GeV
coef_atenuacao = 0.015  # Coeficiente de atenuação para concreto (1/cm)
espessura = np.linspace(0, 200, 500)  # Espessura do concreto em cm

# Variáveis para simulação de ionização
ionizacao_x = []
ionizacao_y = []

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, max(espessura))  # Limite do eixo X
ax.set_ylim(0, energia_inicial)  # Limite do eixo Y
ax.set_title("Perda de Energia de Múons através do Concreto")
ax.set_xlabel("Espessura do Concreto (cm)")
ax.set_ylabel("Energia Remanescente (GeV)")

# Plotando a linha da energia remanescente
linea_energia, = ax.plot([], [], label="Energia Remanescente", color="b")

# Plotando os pontos de ionização
linea_ionizacao, = ax.plot([], [], 'ro', label="Ionizações", markersize=5)

# Plotando o ponto do múon
point_muo, = ax.plot([], [], 'go', label="Posição do Múon", markersize=8)

# Função de atualização da animação
def update(frame):
    # Calculando a energia remanescente no ponto atual
    energia_atual = energia_inicial * np.exp(-coef_atenuacao * espessura[frame])
    
    # Atualizando a linha da energia remanescente
    linea_energia.set_data(espessura[:frame+1], energia_inicial * np.exp(-coef_atenuacao * espessura[:frame+1]))
    
    # Simulando o processo de ionização e interações, que ocorrem a intervalos aleatórios
    if np.random.rand() < 0.05:  # 5% de chance a cada passo de simular uma ionização
        ionizacao_x.append(espessura[frame])
        ionizacao_y.append(energia_atual)
    
    # Atualizando a linha de ionizações
    linea_ionizacao.set_data(ionizacao_x, ionizacao_y)
    
    # Atualizando a posição do múon
    point_muo.set_data([espessura[frame]], [energia_atual])  # Corrigido para passar como lista
    
    return linea_energia, linea_ionizacao, point_muo

# Criando a animação
ani = FuncAnimation(fig, update, frames=len(espessura), interval=50, blit=True)

# Exibindo o gráfico com a animação
plt.legend()
plt.grid(True)
plt.show()
