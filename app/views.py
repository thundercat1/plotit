from app import app
import flask
import time


@app.route('/')
def index():
    return 'Index page'
