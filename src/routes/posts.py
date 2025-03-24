from fastapi import APIRouter

router = APIRouter()

@router.get("/numeros")
def get_numeros():
    return [{"numero": i} for i in range(1, 11)]

@router.post("/echo")
def echo_data(data: dict):
    print(f"Datos recibidos: {data}")  # Log en consola
    return data
