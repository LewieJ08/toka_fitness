from flask import Flask, render_template

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
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)