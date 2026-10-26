# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Adapte a API de livros feita com FastAPI para armazenar dados em um banco SQLite. Você praticará criação de tabelas, consultas SQL parametrizadas e persistência dos dados entre reinicializações do servidor.

## 📝 Tarefas

### 🛠️ Criar o banco de dados e a tabela de livros

#### Descrição

Use o módulo `sqlite3` da biblioteca padrão do Python para criar o arquivo do banco e preparar a tabela usada pela API.

#### Requisitos

O programa concluído deve:

- Criar o arquivo `books.db` na pasta da aplicação.
- Criar a tabela `books` com `id` como chave primária e os campos `title` e `author` como texto obrigatório.
- Criar a tabela somente se ela ainda não existir, sem apagar os registros existentes ao reiniciar o servidor.
- Fechar corretamente cada conexão com o banco de dados.

### 🛠️ Persistir o cadastro e a listagem de livros

#### Descrição

Substitua o armazenamento em memória da API anterior por operações SQLite para cadastrar e listar livros.

#### Requisitos

O programa concluído deve:

- Implementar `POST /books` para inserir um livro validado pelo modelo `Book` na tabela.
- Implementar `GET /books` para retornar todos os livros armazenados.
- Usar consultas parametrizadas com `?` em vez de concatenar valores na instrução SQL.
- Manter os livros cadastrados disponíveis após encerrar e iniciar o servidor novamente.

### 🛠️ Consultar, atualizar e remover livros persistidos

#### Descrição

Atualize as rotas por ID para ler e modificar os registros diretamente no banco SQLite.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books/{book_id}`, `PUT /books/{book_id}` e `DELETE /books/{book_id}` usando o ID recebido na rota.
- Atualizar título e autor com `PUT` e remover o registro com `DELETE`.
- Retornar uma resposta HTTP `404` quando o livro solicitado não existir.
- Verificar pela documentação em `/docs` que os dados continuam disponíveis após reiniciar o servidor.
