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
cd f1-web
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
