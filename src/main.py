import os
from fastapi import FastAPI
from dotenv import load_dotenv
from .database import engine
from .models.model import Base
from .routes.posts import router as posts_router

# Cargar variables de entorno
load_dotenv(".env.development")

app = FastAPI(title="Publicaciones API", debug=True)

# Registrar rutas
app.include_router(posts_router)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Manejo de errores personalizados
@app.exception_handler(Exception)
def handle_exception(request, err):
    return HTTPException(status_code=500, detail=str(err))

# Endpoint GET que devuelve una lista de números
@app.get("/numeros")
def get_numeros():
    return [{"numero": i} for i in range(1, 11)]

# Endpoint POST que devuelve el JSON recibido
@app.post("/echo")
def echo_data(data: dict):
    print(f"Datos recibidos: {data}")  # Log en consola
    return data

# Verificar si las variables de entorno se cargaron correctamente
print(f"VERSION: {os.getenv('VERSION')}")
