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

 1. Abrir PowerShell como Administrador
Presiona Win + X y selecciona "Terminal de Windows (Admin)" o "Windows PowerShell (Admin)".

Habilita la ejecución de scripts ejecutando este comando:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
```
🔹 2. Instalar Chocolatey
Ejecuta el siguiente comando en PowerShell (Admin):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
🔹 3. Verificar Instalación
Cierra y abre una nueva ventana de PowerShell y ejecuta:

```powershell
choco --version
```
Si ves un número de versión (X.X.X), Chocolatey se instaló correctamente. 🎉



🔹 1. Usar Uvicorn con Certificado SSL (Local o en Servidor)
Si tienes un certificado SSL, puedes ejecutarlo con Uvicorn:

```sh
uvicorn src.main:app --host 0.0.0.0 --port 8000 --ssl-keyfile=clave_privada.key --ssl-certfile=certificado.crt
```
🔹 Explicación:


--ssl-keyfile=clave_privada.key: Archivo de clave privada.

--ssl-certfile=certificado.crt: Certificado SSL.

Si no tienes un certificado, puedes generar uno con OpenSSL (solo para pruebas locales):


Verifica si OpenSSL está instalado
Ejecuta este comando en PowerShell:

powershell
Copiar
Editar
Get-Command openssl -ErrorAction SilentlyContinue
Si no devuelve ninguna información, significa que OpenSSL no está instalado o no está en el PATH.

2️⃣ Instala OpenSSL con Chocolatey
Ahora que ya tienes Chocolatey, puedes instalar OpenSSL fácilmente ejecutando:

powershell
Copiar
Editar
choco install openssl -y
Una vez instalado, cierra y vuelve a abrir PowerShell.

3️⃣ Verifica la instalación
Ejecuta:

powershell
Copiar
Editar
openssl version
Si ves algo como OpenSSL 3.0.2 (o similar), significa que OpenSSL ya está listo.



```sh
openssl req -x509 -newkey rsa:2048 -keyout clave_privada.key -out certificado.crt -days 365 -nodes
```