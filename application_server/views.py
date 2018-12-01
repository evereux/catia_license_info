#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

from flask import redirect, render_template, request, url_for

from application_server import SearchForm
from application_server import app
from application_server.main import main


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():

    search = request.args.get('search')
    form = SearchForm()

    if form.validate_on_submit():

        search = form.search.data

        return redirect(url_for('index', search=search))

    form.search.data = search
    data = main('config.json', search=search)

    return render_template('index.html', data=data, form=form)
