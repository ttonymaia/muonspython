import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
energia_muon = 4  # GeV
coef_atenuacao = 0.015  # Coeficiente de atenuação linear para concreto (em 1/cm)
espessura = np.linspace(0, 200, 500)  # Espessura em cm

# Intensidade inicial de múons
intensidade_inicial = 10000

# Cálculo da intensidade transmitida (Lei de Atenuação: I = I0 * exp(-mu * x))
intensidade_transmitida = intensidade_inicial * np.exp(-coef_atenuacao * espessura)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(espessura, intensidade_transmitida, label="Intensidade dos Múons")
plt.axvline(100, color='red', linestyle='--', label="Espessura de 100 cm")
plt.title("Atenuação de Múons de 4 GeV em Concreto")
plt.xlabel("Espessura do concreto (cm)")
plt.ylabel("Intensidade transmitida")
plt.grid()
plt.legend()
plt.show()
