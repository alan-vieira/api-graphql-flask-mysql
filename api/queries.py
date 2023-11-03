"""
api/queries.py
"""
from ariadne import convert_kwargs_to_snake_case
from .models import ColecaoLivros

def listLivros_resolver(obj, info):
    """
    Retorna a lista de todos os livros do banco de dados.

    Args:
        obj (Any): Não utilizado.
        info (ResolveInfo): Informações sobre a resolução GraphQL.

    Returns:
        dict: Um dicionário contendo a lista de livros ou erros.
    """
    try:
        livros = [livro.to_dict() for livro in ColecaoLivros.query.all()]
        print(livros)
        payload = {
            "success": True,
            "livros": livros
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getLivro_resolver(obj, info, livro_id):
    """
    Retorna os detalhes de um livro com base no ID do livro.

    Args:
        obj (Any): Não utilizado.
        info (ResolveInfo): Informações sobre a resolução GraphQL.
        livro_id (int): ID do livro a ser recuperado.

    Returns:
        dict: Um dicionário contendo os detalhes do livro ou erros, incluindo
        se o livro não for encontrado.
    """
    try:
        livro = ColecaoLivros.query.get(livro_id)
        payload = {
            "success": True,
            "livro": livro.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Item com o ID {livro_id} não encontrado"]
        }

    return payload
