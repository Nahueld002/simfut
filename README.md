# ⚽ Simulador de Torneos de Fútbol

Aplicación web desarrollada en **Flask + PostgreSQL** para la gestión y simulación
de torneos de fútbol utilizando un sistema de ranking **ELO**.

## 🚀 Tecnologías
- Python (Flask)
- PostgreSQL
- HTML / JavaScript
- Docker

## 📂 Estructura
- backend/: aplicación web
- database/: scripts SQL y simulación
- docker/: docker de postgresql y ejemplo de .env

## ▶️ Ejecución
```bash
cd backend
python app.py


---

## ▶️ Ejecución del proyecto

### 1️⃣ Levantar la base de datos con Docker

Dentro del directorio `docker/`:

```bash
docker-compose up -d

📌 El archivo .env.example contiene un ejemplo de configuración.
Renombralo a .env y adaptá los valores según tu entorno.
2️⃣ Crear las tablas en la base de datos

Actualmente las tablas se crean ejecutando el script SQL:

database/sql/create_table.sql

    ⚠️ Pendiente de mejora: desarrollar un script Python que ejecute automáticamente este archivo SQL.

3️⃣ Migrar los datos iniciales

Ejecutar el script de carga de datos, el cual lee el archivo Excel y vuelca la información en la base de datos:

cd database
python migrar_datos.py

📌 Este script:

    Lee ListaClubes.xlsx

    Inserta confederaciones, países, regiones, ciudades, equipos y torneos

4️⃣ Ejecutar la aplicación web

cd backend
python app.py

La aplicación quedará disponible en:

http://localhost:5000
