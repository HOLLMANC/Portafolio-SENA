import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuración del título de la página web
st.set_page_config(page_title="Dashboard Sena", layout="centered")

st.title("📊 Prueba de Dashboard Interactivo con Python Para Proyecto SENA")
st.write("Bienvenido, Hollman. Este sistema lee tu Excel del ETL en tiempo real.")

# 2. Cargar los datos del Excel que ya creamos
df = pd.read_excel("reporte_contactos_limpios.xlsx")

# 3. CREAR UN FILTRO INTERACTIVO (La magia de Streamlit)
st.subheader("🔍 Filtro de Mensajes por Usuario")

# Creamos una lista desplegable con los nombres del Excel
nombres_unicos = df['nombre'].unique()
seleccion = st.selectbox("Selecciona un usuario para ver su mensaje:", nombres_unicos)

# Filtramos la tabla según lo que el usuario elija en la página web
datos_filtrados = df[df['nombre'] == seleccion]
st.write(datos_filtrados)

# 4. CREAR EL GRÁFICO VISUAL CORREGIDO
st.subheader("📈 Estadísticas del Portafolio")

# Le damos un poco más de altura a la figura para que quepan los nombres rotados
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='nombre', data=df, ax=ax, palette="Blues_d")

plt.title("Mensajes Totales por Persona", fontsize=14, fontweight='bold')
plt.xlabel("Nombres", fontsize=12)
plt.ylabel("Cantidad", fontsize=12)

# ==========================================
# 🔥 AQUÍ ESTÁ EL TRUCO DE LA CORRECCIÓN:
# Rotamos los nombres 45 grados y los alineamos a la derecha
# ==========================================
plt.xticks(rotation=45, ha='right', fontsize=10)

# Esto ajusta automáticamente los márgenes para que no se corte ningún apellido
plt.tight_layout()

# Le decimos a Streamlit que dibuje el gráfico en la pantalla web
st.pyplot(fig)