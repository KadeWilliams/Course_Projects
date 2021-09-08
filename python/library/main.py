from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# Instantiates Flask and the Database 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Generates the schema of the database with the appropriate data types
class Book(db.Model):
    # The id will auto increment
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)

    # The return value is what will be printed out
    def __repr__(self):
        self.title
        self.author
        self.rating
        return f"{self.title} - {self.author} - {self.rating}"


# Establishes our home route
@app.route("/", methods=['GET', 'POST'])
def home():
    # Queries all of the values within the db and generates them on the page
    all_books = Book.query.all()

    # If we are making a get request the page home page will redirect the user to the edit page
    if request.method == 'get':
        return redirect(request(url_for('edit')), )

    # The index page is going to be rendered and pass through all_books to the index.html
    # To be looped over
    return render_template("index.html", all_books=all_books)


# Establishes our add route to add books to the db
@app.route("/add", methods=["GET", "POST"])
def add():
    # if we are making a POST request we retrieve the value from the form @ add.html
    if request.method == "POST":
        # store the values in a dictionary
        book_info = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        book = Book(title=book_info['title'], author=book_info['author'], rating=book_info['rating'])
        
        # Add the book instance and commit it to the db
        db.session.add(book)
        db.session.commit()
        return redirect(request.url)
    return render_template("add.html")


# Establishes our edit route to adjust the rating of books in our db
# We pass through an id of a book when clicked to redirect us to the correct edit page
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # get the correct book based on the id argument
    book_to_edit = Book.query.filter_by(id=id).first()
    if request.method == "POST":
        # update the rating and commit it to the db
        book_to_edit.rating = request.form['rating']
        db.session.commit()
        return redirect((url_for('home')))
    # Render the edit page and pass through the book_to_edit (the book info that will be rendered)
    # and the id
    return render_template('edit.html', book_to_edit=book_to_edit, book_id=id)

# Establishes our add route to add books to the db
@app.route('/delete')
def delete():
    # retrieve ("get") the id based on the item within the for loop in the jinja template
    book_id = request.args.get('id')

    # pass the book_id and ping the db to get the information to remove from the db and commit the change
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    # immediately redirect to the home page
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

