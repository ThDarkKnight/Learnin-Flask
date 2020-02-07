from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user_info.html',  name=name)

# VARIABLES - Jinja2 -> Template
users = {'Onurhan': 27, 'Dark Knight': 35}
movie = 'The Lord of The Rings'
snacks = ['popcorn', 'bagels', 'cookie']

@app.route('/variables')
def variables():
    return render_template('variables.html', users=users, movie=movie, snacks=snacks)
    

if __name__ == "__main__":
    app.run(debug=True)