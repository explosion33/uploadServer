from flask import render_template, flash, redirect, request, url_for
from flask.helpers import send_from_directory
import os
from app import app
from random import randint


#main page
@app.route('/', methods=['GET'])
def download_file():
    return render_template('main.html')

@app.route('/storeFile', methods=['POST'])
def storeFile():
    file = request.files['file']

    key = generateKey()

    root = os.path.join(app.config['ROOT'], "files\\" + key)
    while(os.path.isdir(root)):
        root = os.path.join(app.config['ROOT'], "files\\" + key)

    path = os.path.join(root, secure_filename(file.filename))

    os.mkdir(root)
    file.save(path)

    return key

@app.route('/link/<key>', methods=["GET"])
def showLink(key):
    return "showing " + key 

@app.route('/<key>', methods=["GET"])
def showFile(key):
    root = os.path.join(app.config['ROOT'], "files\\" + key)

    return send_from_directory(root, os.listdir(root)[0])


def secure_filename(name) -> str:
    name = name.replace("../", "")
    return name

def generateKey() -> str:
    return "keytest" + str(randint(0,100))