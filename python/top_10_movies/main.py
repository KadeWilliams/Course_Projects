from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_collection.db'

db = SQLAlchemy(app)

Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)


class UpdateMovie(FlaskForm):
    rating = StringField('Your rating out of 10', [DataRequired()])
    review = StringField('Your review', [DataRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    title = StringField('Movie Title', [DataRequired()])
    year = IntegerField('Year', [DataRequired()])
    description = StringField('Description', [DataRequired()])
    rating = StringField('Rating')
    ranking = StringField('Ranking')
    review = StringField('Review')
    img_url = StringField('Image URL')
    submit = SubmitField('Submit')


new_movie = Movie(title="Parasite",
                  year=2019,
                  description="Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
                  rating=9,
                  ranking=5,
                  review="Very heady movie about the class system of Korea and a very good critque of capitalism in general. Much good, very wow!",
                  img_url="https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg"
                  )

# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = UpdateMovie(request.form)
    movie_id = request.args.get('id')

    movie_to_edit = Movie.query.get(movie_id)
    if request.method == "POST":
        movie_to_edit.rating = request.form['rating']
        movie_to_edit.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_edit)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie(request.form)

    if request.method == "POST":
        new_movie = Movie(title=request.form['title'],
                          year=request.form['year'],
                          description=request.form['description'],
                          rating=request.form['rating'],
                          ranking=request.form['ranking'],
                          review=request.form['review'],
                          img_url=request.form['img_url'])

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
