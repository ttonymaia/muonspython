import numpy as np

# Taxa média de múons por m² por minuto
muon_rate_per_minute = 10000  # múons/min/m²

# Definir a área da superfície em m² (1 m², como no seu TCC)
area_m2 = 1.0

# Calcular múons por minuto na área especificada
muons_per_minute = muon_rate_per_minute * area_m2

print(f"Média de múons atravessando {area_m2} m² por minuto: {muons_per_minute}")
