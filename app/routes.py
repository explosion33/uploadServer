from flask import render_template, flash, redirect, request, url_for
from app import app


#main page
@app.route('/', methods=['GET', 'POST'])
def download_file():
    return render_template('download.html')