import datetime
from markupsafe import escape
from flask import Flask, render_template , abort
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())
@app.route('/about/')
def about():
    return '<h3>This is a Flask Web application</h3>'
@app.route('/capitalize/<word>/')
def capitaliza(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))
@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)
@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        return '<h1>ERREUR</h1> <h3>Utilisateur non trouvé</h3>'