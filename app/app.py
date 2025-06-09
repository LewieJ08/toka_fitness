from flask import Flask, render_template, request
from database import init_database

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
    return render_template("index.html")

@app.route("/about", methods=["GET","POST"])

def about():
    return render_template("about.html")

@app.route("/articles", methods=["GET","POST"])

def articles():
    return render_template("articles.html")

@app.route("/login", methods=["GET","POST"])

def login():
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])

def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirmPassword"]
        
        return render_template("register.html", username = username)

    return render_template("register.html")

if __name__ == "__main__":
    init_database()
    app.run(debug=True)