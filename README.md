# API GraphQL com Flask e MySQL

## Visão Geral

Este projeto é uma API GraphQL desenvolvida com Flask para gerenciar uma coleção de livros. Ele oferece operações básicas, como listar todos os livros, obter detalhes de um livro específico, criar um novo livro, atualizar informações de um livro existente e excluir um livro.

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

## Configuração

Certifique-se de instalar todas as dependências do projeto listadas no arquivo `requirements.txt`. Você pode fazer isso com o comando:

   ```bash
   pip install -r requirements.txt
   ```

Além disso, você deve configurar os dados de conexão com o banco de dados PostgreSQL no arquivo `api/mysqlpass.py`. Substitua a variável `mysqlpass` pelo URI do seu banco de dados PostgreSQL.

## Executando o Aplicativo

Para executar o aplicativo, você pode usar os seguintes comandos:

- Defina a variável de ambiente FLASK_APP:

  ```bash
   export FLASK_APP=app.py
   ```
  
- Inicie o servidor de desenvolvimento Flask:

    ```bash
    flask run
    ```
    
O servidor de desenvolvimento estará disponível em "http://127.0.0.1:5000/" por padrão. Você pode acessar esse URL no seu navegador para interagir com a API.

## Documentação da API

A API segue o seguinte esquema GraphQL:

```graphql
  schema {
  query: Query
  mutation: Mutation
}

type Livro {
  livro_id: ID!
  autor: String!
  titulo: String!
}

type LivroResult {
  success: Boolean!
  errors: [String]
  livro: Livro
}

type LivrosResult {
  success: Boolean!
  errors: [String]
  livros: [Livro]
}

type Query {
  listLivros: LivrosResult!
  getLivro(livro_id: ID!): LivroResult!
}

type Mutation {
  createLivro(autor: String!, titulo: String!): LivroResult!
  updateLivro(livro_id: ID!, autor: String, titulo: String): LivroResult!
  deleteLivro(livro_id: ID): LivroResult!
}
  ```

## Operações da API

A API oferece as seguintes operações:

Consulta para listar todos os livros:

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

Consulta para obter informações sobre um livro específico:

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

Mutação para criar um novo livro:

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

Mutação para atualizar informações de um livro:

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

Mutação para excluir um livro:

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

Os resolvedores para cada operação estão documentados nos códigos do projeto nos arquivos `api/mutations.py` e `api/queries.py`. As docstrings e comentários fornecem informações detalhadas sobre a implementação de cada resolvedor.
  
## Modelo de Dados

O modelo de dados para a tabela `ColecaoLivros` está definido no arquivo `api/models.py`. O modelo contém os seguintes atributos:

- `livro_id (ID)`: Chave primária da tabela para identificação única.
- `autor (String)`: O autor do livro.
- `titulo (String)`: O título do livro.

Além disso, a classe `ColecaoLivros` fornece um método `to_dict()` que permite converter uma instância do modelo em um dicionário.
