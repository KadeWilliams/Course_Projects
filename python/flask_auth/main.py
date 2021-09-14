from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
    abort,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)


app.config[
    "SECRET_KEY"
] = "any-secret-key-you-choose"  # TODO Change this secret key before pushing to git hub
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

## CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


## Create Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        

        if db.session.query(User).filter_by(email=request.form.get("email")).first():
            flash("User already exists, try logging in")
            return redirect(url_for("login"))
        
        password = generate_password_hash(
            password=request.form.get("password"), method="pbkdf2:sha256", salt_length=8
        )
        user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=password,
        )

        db.session.add(user)
        db.session.commit()
        login_user(user)

        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Error handling if the provided credentials do not exist in the DB
        try:
            # Get user information from the database via the provided email address
            email = request.form.get("email")
            password = request.form.get("password")
            user = db.session.query(User).filter_by(email=email).first()

            # Check if db.password == provided password
            if not user:
                flash("That email does not exist, please try again.")
                return redirect(url_for("login"))
            elif not check_password_hash(user.password, password):
                flash("Password does not match")
                return redirect(url_for("login"))
            else:
                login_user(user)
                return redirect(url_for("secrets"))
        except Exception as e:
            abort(404)
    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    if current_user.is_authenticated:
        return render_template("secrets.html", name=current_user.name)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    try:
        if current_user.is_authenticated:
            return send_from_directory("static", "files/cheat_sheet.pdf")
    except Exception as e:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
