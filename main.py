import pandas as pd
import sys
import os

# Datos de países BRICS (Brasil, Rusia, India, China, Sudáfrica)
data = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

# Crear DataFrame
frame = pd.DataFrame(data)

print("=== ANÁLISIS DE PAÍSES BRICS CON GITHUB ACTIONS ===")
print(frame)
print()

print("=== ESTADÍSTICAS ===")
print(f"Población total: {sum(frame['population']):.1f} millones")
print(f"Área total: {sum(frame['area']):.1f} millones km²")
print(f"País más poblado: {frame.loc[frame['population'].idxmax(), 'country']}")
print(f"País más grande: {frame.loc[frame['area'].idxmax(), 'country']}")

# Información del entorno de ejecución (útil para entender runners)
print()
print("=== INFORMACIÓN DEL ENTORNO ===")
print(f"Sistema operativo: {os.name}")
print(f"Versión de Python: {sys.version}")
print(f"Directorio actual: {os.getcwd()}")

# Variables de entorno de GitHub Actions (si están disponibles)
github_vars = {
    'GITHUB_ACTOR': os.getenv('GITHUB_ACTOR', 'No disponible'),
    'GITHUB_REPOSITORY': os.getenv('GITHUB_REPOSITORY', 'No disponible'),
    'RUNNER_OS': os.getenv('RUNNER_OS', 'No disponible')
}

print()
print("=== VARIABLES DE GITHUB ACTIONS ===")
for var, value in github_vars.items():
    print(f"{var}: {value}")

print()
print("✅ Análisis completado exitosamente en GitHub Actions!")
