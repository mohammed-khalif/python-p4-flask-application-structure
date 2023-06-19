#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# append to app/app.py

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

# append to app/app.py

@app.route('/<username>')
def users(username):
    return f'<h1>Profile for {username}</h1>'

# modify user() in app/app.py

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'
