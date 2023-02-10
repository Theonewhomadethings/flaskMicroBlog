from flask import render_template
from app import app

#decorators modify the function that follow it
#app.route decorator creates an association between the URL given as and arguement and the function
#When a web browser requests either of the 2 URLS, flask is going to invoke this function and pass the 
#return value of it back to the browser as a response

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