from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecret"

# ===========================
#   CONEXIÓN A MYSQL
# ===========================
def get_db():
    return mysql.connector.connect(
        host="f1_mysql",      # nombre del servicio en docker-compose
        user="root",
        password="rootpass",
        database="f1db"
    )

# ===========================
#   HOME
# ===========================
@app.route("/")
def index():
    return render_template("index.html")

# ===========================
#   LOGIN
# ===========================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM usuarios WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()

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
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pilotos")
    data = cursor.fetchall()
    return render_template("pilotos.html", pilotos=data)


@app.route("/piloto/<int:id>")
def piloto_detalle(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pilotos WHERE id=%s", (id,))
    piloto = cursor.fetchone()
    return render_template("piloto_detalle.html", p=piloto)


# ===========================
#   ADMIN
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
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO pilotos (nombre, equipo, numero, pais, imagen) VALUES (%s, %s, %s, %s, %s)",
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
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM escuderias")
    data = cursor.fetchall()
    return render_template("escuderias.html", escuderias=data)

# ===========================
#   CARRERAS
# ===========================
@app.route("/carreras")
def carreras():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM carreras")
    data = cursor.fetchall()
    return render_template("carreras.html", carreras=data)

# ===========================
#   MAIN
# ===========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
