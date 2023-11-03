"""
api/models.py
"""
from app import db


class ColecaoLivros(db.Model):
    """
    Modelo de dados para a tabela ColecaoLivros.

    Esta classe define a estrutura do modelo de dados para a tabela ColecaoLivros
    no banco de dados. Ela mapeia os campos da tabela para atributos da classe e
    fornece um método 'to_dict' para converter uma instância do modelo em um dicionário.

    Atributos:
        livro_id (db.Integer): Chave primária da tabela para identificação única.
        autor (db.String): O autor do livro.
        titulo (db.String): O título do livro.

    Métodos:
        to_dict(): Converte a instância do modelo em um dicionário.

    """
    livro_id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String)
    titulo = db.Column(db.String)

    def to_dict(self):
        """
        Converte a instância do modelo em um dicionário.

        Returns:
            dict: Um dicionário representando os atributos do modelo.
        """
        return {
            "livro_id": self.livro_id,
            "autor": self.autor,
            "titulo": self.titulo
        }
