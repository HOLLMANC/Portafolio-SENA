import pandas as pd
import mysql.connector

print("--- INICIANDO PROCESO ETL ---")

# ==========================================
# 1. EXTRACCIÓN (Traer los datos de MySQL)
# ==========================================
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="proyecto_sena"
)

df = pd.read_sql("SELECT * FROM contactos", conexion)
conexion.close()

print("-> Paso 1: ¡Datos extraídos con éxito desde MySQL!")

# ==========================================
# 2. TRANSFORMACIÓN (Limpiar los datos)
# ==========================================
df['nombre'] = df['nombre'].str.upper().str.strip()

print("-> Paso 2: ¡Nombres transformados a mayúsculas y corregidos!")

# ==========================================
# 3. CARGA (Guardar el resultado en Excel)
# ==========================================
df.to_excel("reporte_contactos_limpios.xlsx", index=False)

print("-> Paso 3: ¡Proceso terminado! Archivo 'reporte_contactos_limpios.xlsx' creado.")
print("--- ETL FINALIZADO CON ÉXITO ---")