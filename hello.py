import os
from flask import Flask
import parseBurn

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/goodbye')
def goodbye():
    return 'Goodbye World!'

@app.route('/burn')
def burn():
	return parseBurn.parseBurn('http://isjitaburning.com/kills.php')