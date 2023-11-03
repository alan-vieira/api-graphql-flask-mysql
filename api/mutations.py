"""
api/mutations.py
"""
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import ColecaoLivros


@convert_kwargs_to_snake_case
def create_livro_resolver(obj, info, autor, titulo):
    """
    Cria um novo livro com os detalhes fornecidos e o adiciona ao banco de
    dados.

    Args:
        obj (Any): Não utilizado.
        info (ResolveInfo): Informações sobre a resolução GraphQL.
        autor (str): Autor do livro.
        titulo (str): Título do livro.

    Returns:
        dict: Um dicionário contendo o resultado da criação, incluindo o livro
        criado ou erros.
    """
    livro = ColecaoLivros(
        autor=autor, titulo=titulo
    )
    db.session.add(livro)
    db.session.commit()
    payload = {
        "success": True,
        "livro": livro.to_dict()
    }

    return payload


@convert_kwargs_to_snake_case
def update_livro_resolver(obj, info, livro_id, autor, titulo):
    """
    Atualiza os detalhes de um livro existente com base no ID do livro.

    Args:
        obj (Any): Não utilizado.
        info (ResolveInfo): Informações sobre a resolução GraphQL.
        livro_id (int): ID do livro a ser atualizado.
        autor (str): Novo autor do livro.
        titulo (str): Novo título do livro.

    Returns:
        dict: Um dicionário contendo o resultado da atualização, incluindo o 
        livro atualizado ou erros.
    """
    try:
        livro = ColecaoLivros.query.get(livro_id)
        if livro:
            livro.autor = autor
            livro.titulo = titulo
        db.session.add(livro)
        db.session.commit()
        payload = {
            "success": True,
            "livro": livro.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Item como o ID {livro_id} não encontrado"]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_livro_resolver(obj, info, livro_id):
    """
    Exclui um livro com base no ID do livro.

    Args:
        obj (Any): Não utilizado.
        info (ResolveInfo): Informações sobre a resolução GraphQL.
        livro_id (int): ID do livro a ser excluído.

    Returns:
        dict: Um dicionário contendo o resultado da exclusão, incluindo o livro
        excluído ou erros.
    """
    try:
        livro = ColecaoLivros.query.get(livro_id)
        db.session.delete(livro)
        db.session.commit()
        payload = {"success": True, "livro": livro.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Não encontrado"]
        }
    return payload
