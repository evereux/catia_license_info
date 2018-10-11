#! python3
# -*- coding: utf-8 -*-

from flask import render_template

from main import main
from application_server import app



@app.route('/')
def index():

    data = main('config.json')

    return render_template('index.html', data=data)