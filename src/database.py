from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv(".env.development")

# Verificar si DATABASE_URL se está cargando
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"🔍 DATABASE_URL cargada: {DATABASE_URL}")

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL no está configurada en .env.development")

# Crear la conexión con SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver las consultas SQL en consola
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
