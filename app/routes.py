from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')  #associates the URLS / 
@app.route('/index') #associates the /index to the function

def index():
    user = {'username': 'Abdullah'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
#note to self about get post stuff
#HTTP protocol states that GET requests return information ot the clien (web browser in this case)
#POST requests are when the browser submits form data to the server
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me = {}".format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form=form)