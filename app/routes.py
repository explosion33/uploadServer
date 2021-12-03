from flask import render_template, flash, redirect, request, url_for, jsonify
from flask.helpers import send_from_directory
import os
from app import app
from random import randint

import time
from flask_executor import Executor

executor = Executor(app)

class File:
    def __init__(this, key):
        this.key = key
        this.lastPath = this.getPath()

    def getPath(this) -> str:
        return os.path.join(app.config['ROOT'], "files\\" + this.key)

class markedFile(File):
    def __init__(this, key, time=0):
        super().__init__(this, key)
        this.time = time

    def rmrf(this, path) -> None:
        if (os.path.isfile(path)):
            os.remove(path)
        else:
            for f in os.listdir(path):
                this.rmrf(os.path.join(path,f))
            os.rmdir(path)

    def delete(this):
        this.rmrf(this.getPath())

    def timer(this):
        time.sleep(this.time*60)
        this.delete()
        markedFiles.remove(this.key)
        files.remove(this.key)

markedFiles = {}
files = {}

def updateFiles():
    root = os.path.join(app.config['ROOT'], "files")
    for f in os.listdir(root):
        if (f != ".gitignore"):
            files[f] = File(f)

updateFiles()

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

    saveFile(file, key)

    if request.form["big"] == "true":
        f = markedFile(key, getStoreTime(request.form['size']))
        print(f.getPath() + " will be deleted after " + str(f.time) + " minutes")
        executor.submit(f.timer)
        markedFiles[key] = f
    files[key] = File(key)

    prefix = app.config["DOMAIN"]
    print(prefix, prefix != "")
    if (prefix != ""):
        prefix = "http://" + prefix
    redirect_url = prefix + "/link/" + key

    return redirect_url

def saveFile(file, key):
    root = join(app.config['ROOT'], "files", key)
    while(os.path.isdir(root)):
        root = join(app.config['ROOT'], "files", key)

    
    path = os.path.join(root, secure_filename(file.filename))

    print("saving to |", path)

    os.mkdir(root)
    file.save(path)

@app.route('/link/<key>', methods=["GET"])
def showLink(key):
    root = "http://" + request.base_url #app.config["DOMAIN"]
    link = os.path.join(root, key)

    hasTime = False
    time = 0
    if key in markedFiles.keys():
        hasTime = True
        time = markedFiles[key].time

    return render_template('link.html', link=link, time=time, hasTime=time)

@app.route('/<key>', methods=["GET"])
def showFile(key):
    root = join(app.config['ROOT'], "files", key)

    return send_from_directory(root, os.listdir(root)[0])


@app.route('/validateLinks', methods=["POST"])
def validateLinks():
    storage = request.json
    print(storage)

    newStorage = {}

    for link in storage.keys():
        #get only end of the link, link can be domain.com/key
        key = link.split("/")
        key = key[len(key)-1]

        print(key, files)

        if (key in files.keys()):
            newStorage[link] = storage[link]

    print(newStorage)

    return jsonify(newStorage)

@app.route('/mylinks', methods=["GET"])
def myLinks():
    return render_template("mylinks.html")

@app.route('/favicon.ico', methods=['GET'])
def getIcon():
    root = join(app.config['ROOT'], "app", "static", "images")
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


def getStoreTime(size) -> int:
    return 60


def join(*args) -> str:
    out = ""
    for a in args:
        out = os.path.join(out, a)
    return out