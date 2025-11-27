from flask import Flask, render_template, request, redirect, session
import sqlite3
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecret"

def get_db():
    return mysql.connector.connect(
        host="db",
        user="f1user",
        password="f1pass",
        database="f1db"
    )

@app.route("/")
def index():
    return render_template("index.html")

# ===========================
#   LOGIN / LOGOUT
# ===========================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute(
            "SELECT * FROM usuarios WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()

        if user:
            session["user"] = username
            return redirect("/admin")
        else:
            return "Usuario o contraseña incorrectos"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# ===========================
#   PILOTOS
# ===========================

@app.route("/pilotos")
def pilotos():
    db = get_db()
    data = db.execute("SELECT * FROM pilotos").fetchall()
    return render_template("pilotos.html", pilotos=data)

@app.route("/piloto/<int:id>")
def piloto_detalle(id):
    db = get_db()
    piloto = db.execute("SELECT * FROM pilotos WHERE id = ?", (id,)).fetchone()
    return render_template("piloto_detalle.html", p=piloto)

# ===========================
#   PANEL ADMIN
# ===========================

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        nombre = request.form["nombre"]
        equipo = request.form["equipo"]
        numero = request.form["numero"]
        pais = request.form["pais"]
        imagen = request.form["imagen"]

        db = get_db()
        db.execute(
            "INSERT INTO pilotos (nombre, equipo, numero, pais, imagen) VALUES (?, ?, ?, ?, ?)",
            (nombre, equipo, numero, pais, imagen)
        )
        db.commit()
        return redirect("/pilotos")

    return render_template("admin.html")

# ===========================
#   ESCUDERÍAS
# ===========================

@app.route("/escuderias")
def escuderias():
    db = get_db()
    data = db.execute("SELECT * FROM escuderias").fetchall()
    return render_template("escuderias.html", escuderias=data)

# ===========================
#   CARRERAS
# ===========================

@app.route("/carreras")
def carreras():
    db = get_db()
    data = db.execute("SELECT * FROM carreras").fetchall()
    return render_template("carreras.html", carreras=data)

# ===========================
#   MAIN
# ===========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
