# Imagen base
FROM python:3.10-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de requisitos
COPY requirements.txt /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY app.py /app

# Puerto donde correrá Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
