from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, URL
import csv
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', validators=[URL()])
    opening = StringField('Opening Time (12 hour clock)')
    closing = StringField('Closing Time (12 hour clock)')
    rating = SelectField('Coffee Rating', choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi = SelectField('Wifi Strength', choices=['✘', '💪', '💪💪' ,'💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power = SelectField('Power Outlet Rating', choices=['✘', '🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌' ,'🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # cafe = form.data['cafe']
        # location = form.data['cafe_location']
        # opening = form.data['opening']
        # closing = form.data['closing']
        # rating = form.data['rating']
        # wifi = form.data['wifi']
        # power = form.data['power']
        cafe_data = []
        for k, v in form.data.items():
            cafe_data.append(v)
        with open('cafe-data.csv', "a", newline='', encoding='utf-8') as f:
            cafe_data.pop()
            cafe_data.pop()
            wr = csv.writer(f)
            wr.writerow(cafe_data)



    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # if form.validate_on_submit()

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
