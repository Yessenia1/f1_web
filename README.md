# f1_web
# 🏎️ F1 Web - Aplicación de Fórmula 1

Aplicación web desarrollada con Flask para gestionar información de pilotos, escuderías y carreras de Fórmula 1.

##  Características

- 🏁 **Gestión de Pilotos**: Visualiza y administra información de pilotos de F1
- 🏢 **Escuderías**: Consulta equipos y sus jefes de equipo
- 📅 **Calendario**: Visualiza todas las carreras de la temporada
- 🔐 **Panel Admin**: Sistema de autenticación para agregar nuevos pilotos
- 🎨 **Diseño Moderno**: Interfaz oscura y elegante inspirada en F1
- 📱 **Responsive**: Adaptado para móviles, tablets y desktop

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clona el repositorio (o descarga los archivos)

```bash
git clone https://github.com/tu-usuario/f1-web.git
cd f1_web
```

### 2. Crea un entorno virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crea la base de datos

```bash
python create_db.py
```

Esto creará:
- ✅ Base de datos SQLite (`database.db`)
- ✅ Tablas necesarias (usuarios, pilotos, escuderías, carreras)
- ✅ Usuario admin predeterminado
- ✅ Datos de ejemplo (5 pilotos, 5 escuderías, 8 carreras)

### 5. Ejecuta la aplicación

```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

## Estructura del Proyecto

```
f1-web/
│
├── app.py                  # Aplicación principal Flask
├── create_db.py           # Script para crear la base de datos
├── requirements.txt       # Dependencias del proyecto
├── database.db           # Base de datos SQLite (se crea al ejecutar create_db.py)
│
├── templates/            # Plantillas HTML
│   ├── layout.html       # Plantilla base
│   ├── index.html        # Página principal
│   ├── pilotos.html      # Lista de pilotos
│   ├── piloto_detalle.html  # Detalle de un piloto
│   ├── escuderias.html   # Lista de escuderías
│   ├── carreras.html     # Calendario de carreras
│   ├── login.html        # Página de login
│   └── admin.html        # Panel de administración
│
└── static/               # Archivos estáticos (opcional)
    └── styles.css        # Estilos personalizados
```

## Credenciales de Acceso

**Panel de Administración:**
- **Usuario:** `admin`
- **Contraseña:** `admin123`

**Acceso:** http://localhost:5000/login

##  Rutas Disponibles

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal |
| `/pilotos` | Lista de todos los pilotos |
| `/piloto/<id>` | Detalle de un piloto específico |
| `/escuderias` | Lista de escuderías |
| `/carreras` | Calendario de carreras |
| `/login` | Página de login |
| `/admin` | Panel de administración (requiere login) |
| `/logout` | Cerrar sesión |

## Tecnologías Utilizadas

- **Backend:**
  - Flask 3.0.2 - Framework web
  - SQLite3 - Base de datos
  
- **Frontend:**
  - HTML5
  - Tailwind CSS - Framework CSS
  - JavaScript (Vanilla)

## Estructura de la Base de Datos

### Tabla: `usuarios`
```sql
id          INTEGER PRIMARY KEY
username    TEXT
password    TEXT
```

### Tabla: `pilotos`
```sql
id          INTEGER PRIMARY KEY
nombre      TEXT
equipo      TEXT
numero      INTEGER
pais        TEXT
imagen      TEXT
```

### Tabla: `escuderias`
```sql
id          INTEGER PRIMARY KEY
nombre      TEXT
pais        TEXT
jefe        TEXT
```

### Tabla: `carreras`
```sql
id          INTEGER PRIMARY KEY
nombre      TEXT
pais        TEXT
fecha       TEXT
```



---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!

🏁 **¡Disfruta de F1 Web!**



https://docs.docker.com/engine/install/ubuntu/ 
docker --version
docker compose versión
Dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["python", "app.py"]

docker-compose.yml
version: "3.9"

services:
  web:
    build: .
    container_name: f1_web
    restart: always
    depends_on:
      - db
    environment:
      DB_HOST: db
      DB_USER: f1user
      DB_PASS: f1pass
      DB_NAME: f1db
    ports:
      - "8000:8000"
    networks:
      - f1net

  nginx:
    image: nginx:latest
    container_name: f1_nginx
    volumes:
      - ./config/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    ports:
      - "80:80"
    depends_on:
      - web
    networks:
      - f1net

  db:
    image: mysql:8.0
    container_name: f1_mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: f1db
      MYSQL_USER: f1user
      MYSQL_PASSWORD: f1pass
    volumes:
      - ./database:/var/lib/mysql
    networks:
      - f1net

networks:
  f1net:
    driver: bridge

config/nginx.conf
server {
    listen 80;

    location / {
        proxy_pass http://f1_web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

sudo docker compose up -d --build
sudo docker ps
sudo docker exec -it f1_mysql mysql -u root -p rootpass
CREATE DATABASE IF NOT EXISTS f1db;
USE f1db;

--  TABLA USUARIOS
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Insertar usuario admin
INSERT INTO usuarios (username, password)
VALUES ('admin', 'admin123');
--  TABLA PILOTOS
CREATE TABLE pilotos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    equipo VARCHAR(100) NOT NULL,
    numero INT NOT NULL,
    pais VARCHAR(100) NOT NULL,
    imagen TEXT
);

INSERT INTO pilotos (nombre, equipo, numero, pais, imagen) VALUES
('Max Verstappen', 'Red Bull Racing', 1, 'Países Bajos', 'https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png'),
('Sergio Pérez', 'Red Bull Racing', 11, 'México', 'https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png'),
('Lewis Hamilton', 'Mercedes', 44, 'Reino Unido', 'https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/L/LEWHAM01_Lewis_Hamilton/lewham01.png'),
('Charles Leclerc', 'Ferrari', 16, 'Mónaco', 'https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png'),
('Lando Norris', 'McLaren', 4, 'Reino Unido', 'https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/L/LANNOR01_Lando_Norris/lannor01.png');

--  TABLA ESCUDERÍAS
CREATE TABLE escuderias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    jefe VARCHAR(100) NOT NULL
);

INSERT INTO escuderias (nombre, pais, jefe) VALUES
('Red Bull Racing', 'Austria', 'Christian Horner'),
('Ferrari', 'Italia', 'Fred Vasseur'),
('Mercedes', 'Alemania', 'Toto Wolff'),
('McLaren', 'Reino Unido', 'Andrea Stella'),
('Aston Martin', 'Reino Unido', 'Mike Krack');

--  TABLA CARRERAS
CREATE TABLE carreras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    fecha VARCHAR(50) NOT NULL
);

INSERT INTO carreras (nombre, pais, fecha) VALUES
('GP de Bahréin', 'Bahréin', '2 de marzo, 2025'),
('GP de Arabia Saudita', 'Arabia Saudita', '9 de marzo, 2025'),
('GP de Australia', 'Australia', '16 de marzo, 2025'),
('GP de Japón', 'Japón', '6 de abril, 2025'),
('GP de China', 'China', '20 de abril, 2025'),
('GP de Miami', 'Estados Unidos', '4 de mayo, 2025'),
('GP de Emilia Romaña', 'Italia', '18 de mayo, 2025'),
('GP de Mónaco', 'Mónaco', '25 de mayo, 2025');
USE f1db;
SHOW TABLES; 
SELECT * FROM pilotos;

