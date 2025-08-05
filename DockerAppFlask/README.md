# Flask Docker Hello World 🌐🐳

Proyecto de demostración que dockeriza una aplicación mínima desarrollada con **Flask** (Python), desplegándola dentro de un contenedor **Docker**. Esta aplicación devuelve un mensaje “Hola Mundo desde Flask en Docker” al acceder vía navegador.

---

## 📁 Estructura del proyecto

flask-docker-hello/ <br>
├── app.py # Aplicación Flask <br>
├── Dockerfile # Imagen Docker personalizada <br>
├── requirements.txt # Dependencias de Python <br>
└── README.md

## 🐍 Requisitos

- Python 3 instalado en el entorno local (solo para pruebas locales)
- Docker Engine
- Sistema operativo: Linux / WSL2 / Windows / macOS

---

## 🚀 Pasos de uso

### 1. Construir la imagen

docker build -t flask-hello .

### 2. Ejecutar el contenedor
docker run -d -p 5000:5000 --name flask-hello-container flask-hello

### 3. Acceder en el navegador
http://localhost:5000


## 🛑 Detener el contenedor

docker stop flask-hello-container <br>
docker rm flask-hello-container

## 📌 Contenido del Dockerfile

FROM python:3.10-slim <br>
WORKDIR /app <br>
COPY requirements.txt /app <br>
RUN pip install --no-cache-dir -r requirements.txt <br>
COPY app.py /app <br>
EXPOSE 5000 <br>
CMD ["python", "app.py"] <br>

## 📫 Autor
Giancarlos Mamani Benitez