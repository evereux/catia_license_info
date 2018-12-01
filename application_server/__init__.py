#! python3
# -*- coding: utf-8 -*-


from flask import Flask
from .forms import SearchForm

app = Flask(__name__)
app.secret_key = 'po9ivf9jl23k49mv'

from application_server.views import index
