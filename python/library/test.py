from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)

    def __repr__(self):
        self.title
        self.author
        self.rating
        return f'{self.title}'




all_books = Book.query.all()
book = Book.query.get(4)
# print(book)
# for elem in book:
#     print(elem)

# print(type(all_books))

# print(all_books)
# for book in all_books:
#     print(book)

book_to_edit = Book.query.filter_by(id=1).first()

print(book_to_edit.rating)

print(book)
