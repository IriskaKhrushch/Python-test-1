from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
def valid_login(name,password):
    return name==password
def log_the_user_in(name):
    return "Hello, you are an authorized user "+name
def log_the_user_notin(name):
    return "Hello, you are not an authorized user "+name

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
            #return log_the_user_notin(request.form['username'])
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)




