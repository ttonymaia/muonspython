import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
depths = np.linspace(0, 100, 500)  # Profundidades em cm
coefficients = {
    "Concreto (ρ ~ 2.4 g/cm³)": 0.015,
    "Água (ρ ~ 1.0 g/cm³)": 0.005,
    "Aço (ρ ~ 7.8 g/cm³)": 0.04
}

# Função para calcular intensidade de múons
def muon_intensity(depth, muon_flux, attenuation_coefficient):
    return muon_flux * np.exp(-attenuation_coefficient * depth)

# Fluxo inicial de múons
initial_flux = 10000  # múons/m²/min

# Cálculo e plotagem
plt.figure(figsize=(10, 6))
for material, coef in coefficients.items():
    intensity = muon_intensity(depths, initial_flux, coef)
    plt.plot(depths, intensity, label=material)

plt.title("Intensidade de Múons em Diferentes Materiais")
plt.xlabel("Profundidade (cm)")
plt.ylabel("Intensidade de Múons (múons/m²/min)")
plt.legend()
plt.grid()
plt.show()
