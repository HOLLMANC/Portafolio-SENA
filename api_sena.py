from fastapi import FastAPI
import pymysql
from fastapi.responses import JSONResponse

# Inicializamos FastAPI
app = FastAPI(
    title="API de Contactos - Proyecto SENA",
    description="API independiente para consultar los datos del proceso ETL",
    version="1.0.0"
)

# Función para conectarse a tu base de datos local de XAMPP
def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        port=3307,  # Asegúrate de que este puerto coincide con el que usas en XAMPP
        user="root",
        password="",  # Déjalo vacío si no le pusiste clave en XAMPP
        database="proyecto_sena",  # <-- REEMPLAZA AQUÍ con el nombre real de tu BD
        cursorclass=pymysql.cursors.DictCursor
    )

# Ruta base de bienvenida (Endpoint raíz)
@app.get("/")
def inicio():
    return {"mensaje": "¡API del Proyecto SENA funcionando correctamente!"}

# Ruta para consultar todos los contactos limpios (Endpoint GET)
@app.get("/api/contactos")
def obtener_contactos():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Consultamos la tabla que alimenta tu proyecto
            cursor.execute("SELECT * FROM contactos")
            resultados = cursor.fetchall()
        conexion.close()

        # Retornamos los datos en formato JSON impecable para Postman
        return JSONResponse(content={"total": len(resultados), "datos": resultados})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Error de conexión: {str(e)}"})