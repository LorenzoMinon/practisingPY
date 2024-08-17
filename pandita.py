import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('datos.csv')

# Mostrar el DataFrame
print(df)

# Operaciones adicionales
print("Nombres de las personas:", df["Nombre"].tolist())
print("Edad promedio:", df["Edad"].mean())
