"""
novo_livro.py
"""
from api.models import ColecaoLivros
from app import app, db

novo_livro = ColecaoLivros(
    autor="Carol S. Dweck",
    titulo="Mindset: A nova psicologia do sucesso"
    )

with app.app_context():
    db.session.add(novo_livro)
    db.session.commit()
