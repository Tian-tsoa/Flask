import datetime
from markupsafe import escape
from flask import Flask, render_template , abort , session , request , redirect , url_for
from flask import session
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['username'] == 'Diego' and session['password'] == 'dormircestbien':
            return redirect(url_for('hello'))
        else:
            return redirect(url_for('index'))
            
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))
@app.route('/hello/')
def hello():
    return render_template('hello.html', utc_dt=datetime.datetime.utcnow())
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/capitalize/<word>/')
def capitalize(word):
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
@app.route('/comments/')
def comments():
    comments = ['This thing is more complicated than expected...',
                'I am commenting.',
                'Uhm... well...',
                'No inspiration...'
                ]

    return render_template('comments.html', comments=comments)
if __name__ == '__main__':
    app.run()