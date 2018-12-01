#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

form_class_button = {'class': 'btn btn-outline-dark', 'type': 'submit'}


class SearchForm(FlaskForm):
    search = StringField('search', [validators.DataRequired()])
    submit = SubmitField('filter', render_kw=form_class_button, validators=[validators.DataRequired()])
