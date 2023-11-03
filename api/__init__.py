"""
api/__init__.py
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api.mysqlpass import mysqlpass

app = Flask(__name__)
CORS(app)

# cofiguração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = mysqlpass
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    """
    Rota da página inicial.

    Esta rota lida com solicitações na página inicial do aplicativo.

    Returns:
        str: Uma mensagem de boas-vindas.
    """
    return 'Hello World!!'
