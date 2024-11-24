import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder=os.path.abspath('templates'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultas.db'
app.config['SECRET_KEY'] = 'chave_secreta_para_forms'

db = SQLAlchemy(app)

from app import routes
