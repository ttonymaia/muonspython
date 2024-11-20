import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros gerais
mu_inicial = 0.015  # Coeficiente de atenuação (cm^-1) para o concreto padrão
x = np.linspace(0, 200, 500)  # Espessura do concreto (0 a 200 cm)
I0 = 10000  # Intensidade inicial (número de múons)
energia_inicial = 4.0  # GeV

# Função para simular coeficiente de atenuação variável (com região mais densa)
def coef_atenuacao_variavel(x):
    coef = np.full_like(x, mu_inicial)
    # Aumenta o coeficiente de atenuação na região mais densa (por exemplo entre 80 a 120 cm)
    coef[(x >= 80) & (x <= 120)] = mu_inicial * 2  # Região densa (coeficiente dobrado)
    return coef

# Função para calcular a energia considerando o coeficiente de atenuação variável
def calcular_energia(x, energia_inicial, coef_atenuacao):
    return energia_inicial * np.exp(-coef_atenuacao * x)

# Cálculo da intensidade transmitida (baseada na atenuação)
def calcular_intensidade(x, I0, coef_atenuacao):
    return I0 * np.exp(-coef_atenuacao * x)

# Preparando o gráfico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Função de atualização para a animação
def update(frame):
    # Coeficiente de atenuação variando com a posição
    coef_atenuacao = coef_atenuacao_variavel(x)
    
    # Cálculo da intensidade e da energia para a animação
    I = calcular_intensidade(x[:frame+1], I0, coef_atenuacao[:frame+1])
    energia = calcular_energia(x[:frame+1], energia_inicial, coef_atenuacao[:frame+1])
    
    # Atualizando o gráfico de intensidade
    ax1.clear()
    ax1.plot(x[:frame+1], I, label="Intensidade Transmitida", color='b')
    ax1.axvline(100, color='red', linestyle='--', label="Espessura típica de 1m")
    ax1.fill_between(x[:frame+1], I, color='blue', alpha=0.2)  # Destaque para a área
    ax1.set_xlabel("Espessura do Concreto (cm)")
    ax1.set_ylabel("Intensidade Transmitida (múons)")
    ax1.set_title("Atenuação de Múons - Intensidade")
    ax1.grid(True)
    ax1.legend()
    
    # Atualizando o gráfico de energia
    ax2.clear()
    ax2.plot(x[:frame+1], energia, label="Energia Remanescente", color='g')
    ax2.axvline(100, color='red', linestyle='--', label="Espessura típica de 1m")
    ax2.fill_between(x[:frame+1], energia, color='green', alpha=0.2)  # Destaque para a área
    ax2.set_xlabel("Espessura do Concreto (cm)")
    ax2.set_ylabel("Energia Remanescente (GeV)")
    ax2.set_title("Atenuação de Múons - Energia")
    ax2.grid(True)
    ax2.legend()
    
    # Destaque visual da região densa
    ax1.axvspan(80, 120, color='red', alpha=0.3, label="Região Densa")
    ax2.axvspan(80, 120, color='red', alpha=0.3, label="Região Densa")
    
    # Adicionando a informação sobre o coeficiente de atenuação duplicado na região densa
    ax1.text(100, I.max() * 0.7, "Coeficiente de Atenuação\nduplicado aqui: 0.030", 
             color='black', fontsize=12, ha='center', va='center', backgroundcolor='white')
    ax2.text(100, energia.max() * 0.7, "Coeficiente de Atenuação\nduplicado aqui: 0.030", 
             color='black', fontsize=12, ha='center', va='center', backgroundcolor='white')
    
    # Atualizando a legenda
    ax1.legend()
    ax2.legend()

    return ax1, ax2

# Criando a animação
ani = FuncAnimation(fig, update, frames=len(x), interval=50, blit=False)

# Exibindo a animação
plt.tight_layout()
plt.show()
