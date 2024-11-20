import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
mu = 0.015  # Coeficiente de atenuação (cm^-1)
x = np.linspace(0, 200, 500)  # Espessura do concreto (0 a 200 cm)
I0 = 10000  # Intensidade inicial (número de múons)

# Cálculo da intensidade transmitida
I = I0 * np.exp(-mu * x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x, I, label="Intensidade Transmitida")
plt.axvline(100, color='red', linestyle='--', label="Espessura típica de 1m")
plt.xlabel("Espessura do Concreto (cm)")
plt.ylabel("Intensidade Transmitida (múons)")
plt.title("Atenuação de Múons em Concreto")
plt.grid()
plt.legend()
plt.show()
