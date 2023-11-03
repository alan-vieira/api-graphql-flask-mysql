# API GraphQL com Flask e MySQL

Este é um projeto de exemplo de uma API GraphQL para gerenciar uma coleção de livros. A API permite listar livros, obter detalhes de um livro, criar um novo livro, atualizar informações de um livro e excluir um livro.

## Visão Geral

Este projeto é uma API GraphQL que fornece operações para gerenciar uma coleção de livros. Ele é construído com base no framework Flask e usa o SQLAlchemy para interagir com um banco de dados PostgreSQL.

## Estrutura de Pastas

A estrutura de pastas do projeto é organizada da seguinte forma:

  ```bash
  api-graphql-flask-mysql/
  ├── api/
  │ ├── init.py
  │ ├── models.py
  │ ├── mutations.py
  │ ├── queries.py
  │ └── mysqlpass.py
  ├── app.py
  ├── cria_tabela.py
  ├── novo_livro.py
  ├── schema.graphql
  ├── requirements.txt
  ```

- `api/`: Este diretório contém os principais componentes da aplicação, incluindo os arquivos `__init__.py`, `models.py`, `mutations.py`, `queries.py` e `mysqlpass.py`.

- `app.py`: Este é o arquivo principal da aplicação Flask, onde o aplicativo Flask é definido, o esquema GraphQL é configurado e os endpoints GraphQL são definidos.

- `cria_tabela.py`: Este arquivo é usado para criar as tabelas no banco de dados. Execute-o antes de usar a aplicação.

- `novo_livro.py`: Use este arquivo para adicionar um novo livro ao banco de dados como exemplo de como inserir dados na aplicação.

- `schema.graphql`: Contém o esquema GraphQL que define os tipos, consultas e mutações disponíveis na aplicação.

- `requirements.txt`: Lista as dependências do Python necessárias para o projeto. Use o `pip` para instalar essas dependências.

## Pré-requisitos

Antes de começar, você deve ter as seguintes dependências instaladas:

- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Ariadne

Certifique-se de ter essas dependências instaladas no seu ambiente de desenvolvimento.

## Configuração

1. Clone o repositório:

  ```bash
  git clone https://github.com/alan-vieira/api-graphql-flask-mysql.git
  cd livros-api-graphql
  ```

2. Configure a string de conexão com o banco de dados em `api/mysqlpass.py`.

  ```bash
  mysqlpass = "postgresql://postgresUser:postgresPW@localhost:5455/livros-api-graphql"
  ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script para criar a tabela no banco de dados:

   ```bash
   python cria_tabela.py
   ```
   
## Como Usar

Para executar o aplicativo, você pode usar os seguintes comandos:

- Defina a variável de ambiente FLASK_APP:

  ```bash
   export FLASK_APP=app.py
   ```
  
- Inicie o servidor de desenvolvimento Flask:

    ```bash
    flask run
    ```
    
O servidor estará disponível em http://localhost:5000/graphql.

## Operações da API

A API oferece as seguintes operações

Listar Livros:

  ```graphql
  query AllLivros {
    listLivros {
      success
      errors
      livros {
        livro_id
        autor
        titulo
      }
    }
  }
  ```

Obter Detalhes de um Livro

```graphql
  query GetLivro {
  getLivro(livro_id: "1") {
    livro {
      livro_id
      autor
      titulo
    }
    success
    errors
  }
}
  ```

Criar um Novo Livro

```graphql
  mutation CreateNovoLivro {
  createLivro(
    autor: "Greg McKeown", 
    titulo: "Essencialismo: A disciplinada busca por menos"
  ) {
    livro {
      livro_id
      autor
      titulo
    }
    success
    errors
  }
}
  ```

Atualizar Informações de um Livro

```graphql
  mutation UpdateLivro {
  updateLivro(livro_id: "5", autor: "Clarice Lispector", titulo: "Um Sopro de Vida") {
    livro {
      livro_id
      autor
      titulo
    }
    success
    errors
  }
}
  ```

Excluir um Livro

```graphql
  mutation DeleteLivro {
  deleteLivro(livro_id: "5") {
    success
    errors
    livro {
      livro_id
      autor
      titulo
    }
  }
}
  ```

## Documentação dos Resolvedores

Os resolvedores para as operações da API estão localizados nos arquivos `api/queries.py` e `api/mutations.py`. Consulte esses arquivos para obter detalhes sobre cada resolvedor, incluindo parâmetros e comportamento esperado.
  
## Modelo de Dados

O modelo de dados é definido em `api/models.py`. Ele mapeia os campos da tabela `ColecaoLivros` no banco de dados para atributos da classe `ColecaoLivros` e fornece um método `to_dict` para converter uma instância do modelo em um dicionário.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://github.com/alan-vieira/api-graphql-flask-mysql/blob/main/LICENSE) para detalhes.

## Autor

| [<img src="https://avatars.githubusercontent.com/alan-vieira" width=115><br><sub>Alan Vieira</sub>](https://github.com/alan-vieira) |
| :---: |
