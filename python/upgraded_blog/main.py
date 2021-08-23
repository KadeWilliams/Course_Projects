from flask import Flask, render_template
import requests

url = 'https://api.npoint.io/e4b2170430d11154fe8e'
response = requests.get(url)

app = Flask(__name__)

@app.route('/')
def home():
    posts = response.json()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def post(id):
    posts = response.json()
    return render_template('post.html', posts=posts, id=id)

if __name__ == '__main__':
    app.run(debug=True)