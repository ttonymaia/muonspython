import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
energia_inicial = 4.0  # GeV
coef_atenuacao_inicial = 0.015  # Coeficiente de atenuação inicial (1/cm)
taxa_ionizacao = 0.005  # Taxa de ionização (GeV/cm)
espessura = np.linspace(0, 200, 500)  # Espessura do concreto em cm

# Função para calcular a energia com o coeficiente de atenuação que varia conforme a energia
def calcular_energia(x, energia_inicial, coef_atenuacao, taxa_ionizacao):
    energia_atual = energia_inicial * np.exp(-(coef_atenuacao + taxa_ionizacao) * x)
    return energia_atual

# Função para atualizar o coeficiente de atenuação com base na energia restante
def atualizar_coeficiente(energia_atual, coef_atenuacao_inicial):
    # Aqui, o coeficiente de atenuação varia de acordo com a energia remanescente
    return coef_atenuacao_inicial * (energia_atual / energia_inicial)  # Ajuste simples para ilustrar

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, max(espessura))  # Limite do eixo X
ax.set_ylim(0, energia_inicial)  # Limite do eixo Y
ax.set_title("Atenuação de Energia de Múons com Ionização")
ax.set_xlabel("Espessura do Concreto (cm)")
ax.set_ylabel("Energia Remanescente (GeV)")

# Texto para mostrar a fórmula
formula_text = ax.text(0.5, 0.95, "", fontsize=14, ha='center', transform=ax.transAxes)

# Linha da energia remanescente
linea_energia, = ax.plot([], [], label="Energia Remanescente", color="b")

# Função de atualização da animação
def update(frame):
    # Cálculo da energia considerando atenuação e ionização
    energia_atual = calcular_energia(espessura[frame], energia_inicial, coef_atenuacao_inicial, taxa_ionizacao)
    
    # Atualizando o coeficiente de atenuação com base na energia remanescente
    coef_atenuacao_atualizado = atualizar_coeficiente(energia_atual, coef_atenuacao_inicial)
    
    # Atualizando a linha da energia remanescente
    energia_remanescente = energia_inicial * np.exp(-(coef_atenuacao_atualizado + taxa_ionizacao) * espessura[:frame+1])
    linea_energia.set_data(espessura[:frame+1], energia_remanescente)
    
    # Atualizando a fórmula dinâmica com o coeficiente de atenuação atualizado
    formula_text.set_text(f"$E(x) = {energia_inicial:.2f} \\cdot e^{{-({coef_atenuacao_atualizado:.3f} + {taxa_ionizacao:.3f}) \\cdot x}}$")
    
    return linea_energia, formula_text

# Criando a animação
ani = FuncAnimation(fig, update, frames=len(espessura), interval=50)

# Exibindo o gráfico com a animação
plt.legend()
plt.grid(True)
plt.show()
