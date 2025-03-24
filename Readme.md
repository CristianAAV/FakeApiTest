# Pasos para ejecutar el proyecto
## Clonar el repositorio (si aplica)

```bash
git clone <tu-repositorio>
cd <tu-repositorio>
```

## Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv

## Windows
venv/Scripts/Activate


## Linux
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configurar variables de entorno


Crea un archivo .env.development en la raíz del proyecto y define tus variables.

Ejecutar el servidor

```bash
uvicorn src.main:app --reload
```

Probar los endpoints

GET /numeros:

``` bash

curl -X 'GET' 'http://127.0.0.1:8000/numeros' -H 'accept: application/json'
```

POST /echo:

```bash

curl -X 'POST' 'http://127.0.0.1:8000/echo' -H 'Content-Type: application/json' -d '{"mensaje": "Hola FastAPI"}'

```