from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

from werkzeug.utils import redirect

app = Flask(__name__)

param = { "apiKey": "TopSecretAPIKey"}

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    rows = db.session.query(Cafe).all()
    rand_cafe = random.choice(rows)
    return jsonify(cafe=rand_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    rows = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in rows])


@app.route("/search")
def search():
    loc = request.args.get("loc")
    locations = db.session.query(Cafe).filter_by(location=loc).all()
    if len(locations) >= 1:
        return jsonify(cafe=[location.to_dict() for location in locations])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price'))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success":"Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update(cafe_id):
    try:
        cafe = db.session.query(Cafe).get(cafe_id)
        new_price = request.args.get('new_price')    

        cafe.coffee_price = new_price

        db.session.commit()

        return jsonify({"success": "Successfully updated the price."}), 200
    except Exception as e:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404

## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get('api-key')
    if api_key != param['apiKey']:
        return jsonify({"Unauthorized Access": "You do not have the correct permissions to delete elements from the database"}), 403
    try:
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify({"Success": "Cafe delete successful"}), 200
    except Exception as e:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404





if __name__ == "__main__":
    app.run(debug=True)
