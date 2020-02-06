import flask
from flask import Flask
from flask import request, current_app
from flask import make_response
from flask import redirect, abort

# Initialization
# -- Must create an application instance
# -- WS passes requests via WSGI(Web Server Gateway Interface)

app = Flask(__name__)  # __name__ points where the project runs / main module in order to deterimne location of the app

#-------------------------------------------------------------------------------

# Routes and View Functions
# -- Flask app instance needs to know what code it needs to run for each URL requested.
# -- Route: The association between URL and function that handles it.

# 1-) Using app.route decorator
@app.route('/')
def index():  # index: View Function
    return '<h1>Hello, Flask World!</h1>'

# 2-) Traditional way - w/out decorator
@app.route('/index')
def index_traditional():  # Another view function
    return '<h1>Hello, Flask World!</h1>'

#app.add_url_rule('/index', 'index_traditional', index_traditional)

## Dynamic Component
@app.route('/user/<name>')  # here <name> is the dynamic part of URL
def user(name):
    return "<h3>Hello, {}!</h3>".format(name)


@app.route('/user/<int:age>')  # type specified dynamic content
def user_age(age):
    if age == 53:
        abort(flask.Response('OMG really?!'))
    return "<h3>You are {} years old.</h3>".format(age)

#-------------------------------------------------------------------------------

# Development Web Server
# -- flask run -> This command looks for the name of the Python script that containts app instance in the FLASK_APP env_var
# set FLASK_APP=main_file_name.py
# for DEBUG mode  set/export FLASK_DEBUG=1
# or in code, app.run(debug=True)

#-------------------------------------------------------------------------------

# Application and Request Context
# -- Request object that encapsulates HTTP request sent by the client.
# --
@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    print(current_app.app_context())
    return '<p>Your browser is {}</p>'.format(user_agent)


# Request Dispatching & Object & Hooks

#-------------------------------------------------------------------------------

@app.route('/cookie')
def cookie():
    response = make_response('<h3>This document carries a cookie!!!</h3>')
    response.set_cookie("answer", '42')
    return response


@app.route('/redirect_ex')
def redirect_ex():
    return redirect('https://google.com.tr')

#OR
if __name__ == '__main__':
    app.run(debug=True)