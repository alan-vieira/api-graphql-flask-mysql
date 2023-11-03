# API GraphQL com Flask e MySQL

Este é um exemplo de uma aplicação API GraphQL que utiliza Flask como framework web e MySQL como banco de dados. A aplicação permite listar, criar, atualizar e excluir informações sobre livros.

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

## Executando o Projeto

1. Clone o repositório para o seu ambiente de desenvolvimento.

2. Instale as dependências do projeto executando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie as tabelas no banco de dados executando o seguinte comando:

   ```bash
   python cria_tabela.py
   ```

4.  Adicione um novo livro ao banco de dados executando o seguinte comando:

  ```bash
   python novo_livro.py
   ```
5.  Inicie o servidor da aplicação com o seguinte comando:

    ```bash
    python app.py
    ```
## Exemplos de Consultas e Mutações

Aqui estão alguns exemplos de consultas e mutações que você pode executar:

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

  
