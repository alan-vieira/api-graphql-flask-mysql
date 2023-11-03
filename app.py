"""
app.py
"""
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listLivros_resolver, getLivro_resolver
from api.mutations import create_livro_resolver, update_livro_resolver, \
    delete_livro_resolver
from api import app, db
from api.mysqlpass import mysqlpass

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listLivros", listLivros_resolver)
query.set_field("getLivro", getLivro_resolver)

mutation.set_field("createLivro", create_livro_resolver)
mutation.set_field("updateLivro", update_livro_resolver)
mutation.set_field("deleteLivro", delete_livro_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    """Rota para a interface playground GraphQL.

    Esta rota fornece uma interface de playground para testar consultas
    GraphQL.
    Pode ser acessada por um navegador da web.

    Returns:
        str: HTML da interface playground GraphQL.
    """
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    """Endpoint para o servidor GraphQL.

    Este endpoint processa as solicitações GraphQL, incluindo consultas e
    mutações, e retorna as respostas em formato JSON.

    Returns:
        json: Resposta JSON da consulta GraphQL.
    """
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
