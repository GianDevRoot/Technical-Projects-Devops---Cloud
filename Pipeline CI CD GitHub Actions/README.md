# Mini CI/CD Pipeline – GitHub Actions

Este proyecto demuestra la creación de un flujo automatizado (*pipeline CI/CD*) utilizando **GitHub Actions**.  
El objetivo es ejecutar pasos típicos del ciclo DevOps cada vez que se realiza un `push` al repositorio, tales como:

- Instalación de dependencias
- Ejecución de pruebas unitarias con **pytest**
- Construcción de una imagen **Docker**

---

## 🚀 ¿Cómo funciona?

### El archivo `ci.yml` ubicado en `.github/workflows/` define el pipeline y se activa automáticamente en GitHub cuando se hace *push* a la rama `main`.

``````
on:
  push:
    branches: ["main"]
``````

### ✅ Qué hace este pipeline
Obtiene el código del repositorio

Configura Python 3.10

Instala requirements.txt

Ejecuta pruebas unitarias (pytest) ubicadas en la carpeta /tests

Construye una imagen Docker (docker build)


## 📂 Estructura recomendada del repositorio

``````
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci.yml
``````

## 🧪 Ejemplo de test unitario (tests/test_app.py)

``````
from app import app

def test_home_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
``````

## ✍️ Autor
Giancarlos Mamani Benitez 