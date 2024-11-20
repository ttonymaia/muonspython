import numpy as np
import matplotlib.pyplot as plt

# Parâmetros para intensidade
mu = 0.015  # Coeficiente de atenuação (cm^-1)
x = np.linspace(0, 200, 500)  # Espessura do concreto (0 a 200 cm)
I0 = 10000  # Intensidade inicial (número de múons)

# Cálculo da intensidade transmitida
I = I0 * np.exp(-mu * x)

# Parâmetros para energia
energia_inicial = 4.0  # GeV
coef_atenuacao = 0.015  # Coeficiente de atenuação para concreto (1/cm)
energia = energia_inicial * np.exp(-coef_atenuacao * x)

# Criando o gráfico lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico de intensidade
ax1.plot(x, I, label="Intensidade Transmitida", color='b')
ax1.axvline(100, color='red', linestyle='--', label="Espessura típica de 1m")
ax1.set_xlabel("Espessura do Concreto (cm)")
ax1.set_ylabel("Intensidade Transmitida (múons)")
ax1.set_title("Atenuação de Múons - Intensidade")
ax1.grid(True)
ax1.legend()

# Gráfico de energia
ax2.plot(x, energia, label="Energia Remanescente", color='g')
ax2.axvline(100, color='red', linestyle='--', label="Espessura típica de 1m")
ax2.set_xlabel("Espessura do Concreto (cm)")
ax2.set_ylabel("Energia Remanescente (GeV)")
ax2.set_title("Atenuação de Múons - Energia")
ax2.grid(True)
ax2.legend()

# Exibindo o gráfico
plt.tight_layout()
plt.show()
