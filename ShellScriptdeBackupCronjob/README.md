# Backup Automation Script (Bash + Cron)

Este proyecto consiste en un script Bash que realiza **copias de seguridad automáticas** de una carpeta específica del sistema Linux, generando archivos comprimidos (`.tar.gz`) almacenados de forma organizada por fecha. Un **cronjob** se encarga de ejecutar el script automáticamente en horarios predefinidos, eliminando la necesidad de intervención manual.

---

## 📁 Funcionalidades

- Respaldo de carpetas locales mediante `tar + gzip`
- Generación de backups con nombre basado en fecha y hora
- Automatización de la tarea con `cron`
- Fácil configuración y despliegue en sistemas Linux

---

## ⚙️ Tecnologías usadas

- Bash scripting  
- Comandos `tar`, `gzip`, `date`  
- Cron (crontab)  
- Distribución Linux (probado en Kali Linux)

---

## 📂 Estructura del repositorio

backup-script/ <br>
│ <br>
├── backup.sh → Script principal de backup <br>
├── crontab.txt → Ejemplo de entrada cron programada <br>
└── README.md

## 🔧 Configuración del Script

<h3>Editar las rutas dentro de `backup.sh` según tu entorno:</h3>
SOURCE="/ruta/a/respaldo"
DEST="/ruta/de/backups"

<h3> Dar permisos de ejecución:</h3>

chmod +x backup.sh
<h3> Ejecutar manualmente:</h3>

./backup.sh

## 🕒 Programar ejecución automática
<h3>Editar tareas de cron:</h3>

crontab -e
<h3>Agregar una línea como la siguiente (ejecutar todos los días a las 03:00 AM):</h3>

0 3 * * * /ruta/completa/backup.sh

<h3>verificar con:</h3>

crontab -l

## ✅ Resultado
Se generarán archivos comprimidos (.tar.gz) dentro del directorio de respaldos — por ejemplo:

backup_2024-07-30_03-00-00.tar.gz
backup_2024-07-31_03-00-00.tar.gz

## 📌 Autor
Giancarlos Mamani Benitez