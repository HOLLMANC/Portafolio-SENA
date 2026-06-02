import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as tuple

# Configuración del título de nuestra app web en Python
print("--- CARGANDO TABLERO DE CONTROL EN PYTHON ---")

# 1. Leer los datos del Excel que generó tu ETL
df = pd.read_excel("reporte_contactos_limpios.xlsx")

# 2. Configurar el diseño visual de los gráficos
sns.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize=(8, 5))

# 3. Crear un gráfico de barras interactivo: Contar cuántos mensajes envió cada persona
sns.countplot(x='nombre', data=df, ax=ax, palette="Blues_d")
plt.title("Cantidad de Mensajes Recibidos por Usuario", fontsize=14, fontweight='bold')
plt.xlabel("Nombre del Contacto", fontsize=12)
plt.ylabel("Número de Mensajes", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# 4. Mostrar el gráfico en una ventana o guardarlo como imagen para tu presentación
plt.savefig("grafico_presentacion.png", dpi=300)
plt.show()

print("-> ¡Gráfico generado con éxito como 'grafico_presentacion.png'!")