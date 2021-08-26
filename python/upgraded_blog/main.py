from flask import Flask, render_template, request
from smtplib import SMTP_SSL
import ssl
import requests

url = "https://api.npoint.io/e4b2170430d11154fe8e"
FROM = "a.python.smtp.test@gmail.com"
FROM_PASS = "QJcppZ4y69npg7D"
response = requests.get(url)

app = Flask(__name__)


@app.route("/")
def home():
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        print(name)
        email = request.form["email"]
        print(email)
        number = request.form["number"]
        print(number)
        message = request.form["message"]
        print(message)

        with SMTP_SSL("smtp.gmail.com") as server:
            # server.starttls()
            server.login(user=FROM, password=FROM_PASS)
            server.sendmail(
                from_addr=FROM, to_addrs="kadewilliams0@gmail.com", msg=message
            )
        return f"<h1>Successfully sent your message</h1>"
    else:
        return render_template("contact.html")


@app.route("/post/<int:id>")
def post(id):
    posts = response.json()
    return render_template("post.html", posts=posts, id=id)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form["name"]
#     print(name)
#     email = request.form["email"]
#     print(email)
#     number = request.form["number"]
#     print(number)
#     message = request.form["message"]
#     print(message)

#     return f"<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
