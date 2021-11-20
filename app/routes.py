from flask import render_template, flash, redirect, request, url_for
from flask.helpers import send_from_directory
import os
from app import app
from random import randint

class markedFile:
    def __init__(this, key, time=0) -> None:
        this.key = key
        this.time = time


    def getPath(this) -> str:
        return os.path.join(app.config['ROOT'], "files\\" + this.key)

    def rmrf(this, path) -> None:
        if (os.path.isfile(path)):
            os.remove(path)
        else:
            for f in os.listdir(path):
                this.rmrf(os.path.join(path,f))
            os.rmdir(path)

    def delete(this):
        this.rmrf(this.getPath())

markedFiles = []

#main page
@app.route('/', methods=['GET'])
def download_file():
    return render_template('main.html')


@app.route('/storeFile', methods=['POST'])
def storeFile():
    file = request.files['file']

    print("size", request.form['size'])
    print("big", request.form["big"])

    key = generateKey(10)
    key += "." + getExtension(file.filename).lower()

    if request.form["big"]:
        markForDeletion(key)
    return key

def saveFile(file, key):
    root = os.path.join(app.config['ROOT'], "files\\" + key)
    while(os.path.isdir(root)):
        root = os.path.join(app.config['ROOT'], "files\\" + key)

    
    path = os.path.join(root, secure_filename(file.filename))

    os.mkdir(root)
    file.save(path)

@app.route('/link/<key>', methods=["GET"])
def showLink(key):
    root = request.url_root
    link = os.path.join(root, key)
    return render_template('link.html', link=link)

@app.route('/<key>', methods=["GET"])
def showFile(key):
    root = os.path.join(app.config['ROOT'], "files\\" + key)

    return send_from_directory(root, os.listdir(root)[0])

@app.route('/favicon.ico', methods=['GET'])
def getIcon():
    root = os.path.join(app.config['ROOT'], "app")
    root = os.path.join(root, "static\\images")
    return send_from_directory(root, "favicon.ico")

def secure_filename(name) -> str:
    name = name.replace("../", "")
    name = name.replace(".." , "")
    return name

def generateKey(length) -> str:
    out = ""
    for i in range(length):
        isLetter = randint(0,1) == 0
        if isLetter:
            out += chr(randint(0,25) + 97)
        else:
            out += str(randint(0,9))
    return out

def getExtension(name) -> str:
    a = name.split(".")
    return a[len(a)-1]

def markForDeletion(key) -> None:
    markedFiles.append(markedFile(key, 60))

    