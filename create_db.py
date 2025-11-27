import sqlite3
import os

# Eliminar base de datos anterior si existe
if os.path.exists("database.db"):
    os.remove("database.db")
    print("✅ Base de datos anterior eliminada")

# Crear nueva base de datos
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Tabla de usuarios
c.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
print("✅ Tabla 'usuarios' creada")

# Tabla de pilotos (CON COLUMNA IMAGEN)
c.execute("""
CREATE TABLE pilotos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    equipo TEXT NOT NULL,
    numero INTEGER NOT NULL,
    pais TEXT NOT NULL,
    imagen TEXT
)
""")
print("✅ Tabla 'pilotos' creada")

# Tabla de escuderías
c.execute("""
CREATE TABLE escuderias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pais TEXT NOT NULL,
    jefe TEXT NOT NULL
)
""")
print("✅ Tabla 'escuderias' creada")

# Tabla de carreras
c.execute("""
CREATE TABLE carreras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    pais TEXT NOT NULL,
    fecha TEXT NOT NULL
)
""")
print("✅ Tabla 'carreras' creada")

# Insertar usuario admin de prueba
c.execute("INSERT INTO usuarios (username, password) VALUES ('admin', 'admin123')")
print("✅ Usuario admin creado (usuario: admin, contraseña: admin123)")

# Insertar algunos pilotos de ejemplo
pilotos_ejemplo = [
    ("Max Verstappen", "Red Bull Racing", 1, "Países Bajos", "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png"),
    ("Sergio Pérez", "Red Bull Racing", 11, "México", "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/S/SERPER01_Sergio_Perez/serper01.png"),
    ("Lewis Hamilton", "Mercedes", 44, "Reino Unido", "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/L/LEWHAM01_Lewis_Hamilton/lewham01.png"),
    ("Charles Leclerc", "Ferrari", 16, "Mónaco", "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/C/CHALEC01_Charles_Leclerc/chalec01.png"),
    ("Lando Norris", "McLaren", 4, "Reino Unido", "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/content/dam/fom-website/drivers/L/LANNOR01_Lando_Norris/lannor01.png"),
]

c.executemany("INSERT INTO pilotos (nombre, equipo, numero, pais, imagen) VALUES (?, ?, ?, ?, ?)", pilotos_ejemplo)
print(f"✅ {len(pilotos_ejemplo)} pilotos de ejemplo insertados")

# Insertar algunas escuderías de ejemplo
escuderias_ejemplo = [
    ("Red Bull Racing", "Austria", "Christian Horner"),
    ("Ferrari", "Italia", "Fred Vasseur"),
    ("Mercedes", "Alemania", "Toto Wolff"),
    ("McLaren", "Reino Unido", "Andrea Stella"),
    ("Aston Martin", "Reino Unido", "Mike Krack"),
]

c.executemany("INSERT INTO escuderias (nombre, pais, jefe) VALUES (?, ?, ?)", escuderias_ejemplo)
print(f"✅ {len(escuderias_ejemplo)} escuderías de ejemplo insertadas")

# Insertar algunas carreras de ejemplo
carreras_ejemplo = [
    ("GP de Bahréin", "Bahréin", "2 de marzo, 2025"),
    ("GP de Arabia Saudita", "Arabia Saudita", "9 de marzo, 2025"),
    ("GP de Australia", "Australia", "16 de marzo, 2025"),
    ("GP de Japón", "Japón", "6 de abril, 2025"),
    ("GP de China", "China", "20 de abril, 2025"),
    ("GP de Miami", "Estados Unidos", "4 de mayo, 2025"),
    ("GP de Emilia Romaña", "Italia", "18 de mayo, 2025"),
    ("GP de Mónaco", "Mónaco", "25 de mayo, 2025"),
]

c.executemany("INSERT INTO carreras (nombre, pais, fecha) VALUES (?, ?, ?)", carreras_ejemplo)
print(f"✅ {len(carreras_ejemplo)} carreras de ejemplo insertadas")

# Guardar cambios
conn.commit()
conn.close()

print("\n" + "="*50)
print("🏁 BASE DE DATOS CREADA EXITOSAMENTE")
print("="*50)
print("\n📋 Credenciales de acceso:")
print("   Usuario: admin")
print("   Contraseña: admin123")
print("\n🚀 Ahora ejecuta: python app.py")
print("="*50)