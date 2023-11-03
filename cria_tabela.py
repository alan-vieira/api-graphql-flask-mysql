"""
cria_tabela.py
"""
from app import app, db
from api.mysqlpass import mysqlpass

with app.app_context():
    db.create_all()
