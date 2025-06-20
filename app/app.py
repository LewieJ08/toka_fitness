from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv

from database import init_database, add_user, get_user_by_id, get_user_by_username

#Load .Env Variables
load_dotenv()

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

# Flask login config
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self,id,username,hashed_password):
        self.id = id
        self.username = username
        self.hashed_password = hashed_password

    @classmethod
    def get(cls,user_id):
        user = get_user_by_id(user_id)
        if user:
            return cls(user[0][0],user[0][1],user[0][2])
        else:
            return None

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# GUEST Routes

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

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            user_data = get_user_by_username(username)
        except IndexError:
            return render_template("login.html", error = "Invalid Username or Password")
        
        if check_password_hash(user_data[0][2], password):
            user = User(user_data[0][0], user_data[0][1], user_data[0][2])
            login_user(user)

            return redirect(url_for("dashboard"))
        
        else: 
            return render_template ("login.html", error = "Invalid Username or Password")

    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])

def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirmPassword"]
        email = request.form["email"].lower()
        membership_type = request.form["membershipType"]

        if password != confirm_password:
            return render_template("register.html")
        
        hashed_password = generate_password_hash(password)
        add_user(username, hashed_password, email, membership_type)
        
        return redirect(url_for("login"))

    return render_template("register.html")

# MEMBER Routes

@app.route("/dashboard",methods=["GET","POST"])

def dashboard():
    return render_template("dashboard.html")

# ADMIN Routes

# ERROR Handlers

if __name__ == "__main__":
    init_database()
    app.run(debug=True)