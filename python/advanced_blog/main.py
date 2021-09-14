from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route("/")
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    post = db.session.query(BlogPost).filter_by(id=index).first()
    return render_template("post.html", post=post)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    start = 'new_post'
    form = CreatePostForm()
    post = BlogPost(title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            author=request.form.get("author"),
            date=datetime.now().strftime(f"%B %d, %Y"),
            img_url=request.form.get("img_url"),
            body=request.form.get("body"))
    if request.method == 'POST':
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('make-post.html', form=form, start=start)

# {{url_for('edit_post', post_id=post.id)}}

@app.route("/edit-post/<int:index>" , methods=["GET", "POST"])
def edit_post(index):
    post = db.session.query(BlogPost).filter_by(id=index).first()
    edit_form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            author=post.author,
            img_url=post.img_url,
            body=post.body
            )

    if request.method == 'POST':
        post.title=edit_form.title.data 
        post.subtitle=edit_form.title.data 
        post.author=edit_form.title.data 
        post.img_url=edit_form.title.data 
        post.body=edit_form.title.data 
        db.session.commit()
        return redirect('/')

    return render_template('make-post.html', form=edit_form)

@app.route('/delete/<int:index>', methods=["GET", "POST"])
def delete(index):
    post = db.session.query(BlogPost).filter_by(id=index).first()

    db.session.delete(post)
    db.session.commit()
    return redirect('/')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
