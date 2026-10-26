# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para cadastrar e consultar livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas adequadas para recursos inexistentes.

## 📝 Tarefas

### 🛠️ Inicializar a API e criar uma rota de saúde

#### Descrição

Complete a aplicação inicial e execute o servidor local para confirmar que a API está disponível.

#### Requisitos

O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi uvicorn`.
- Criar uma aplicação FastAPI com o título `Library API`.
- Implementar `GET /health` para responder com o JSON `{"status": "ok"}`.
- Iniciar o servidor executando `python starter-code.py` e permitir acesso à documentação interativa em `/docs`.

### 🛠️ Cadastrar e listar livros

#### Descrição

Crie um modelo Pydantic para representar um livro e implemente as rotas para cadastrar livros e consultar a coleção armazenada em memória.

#### Requisitos

O programa concluído deve:

- Definir um modelo `Book` com os campos `id` (inteiro), `title` (texto) e `author` (texto).
- Implementar `POST /books` para validar os dados recebidos e adicionar o livro à coleção.
- Implementar `GET /books` para retornar a lista de livros cadastrados.
- Retornar o livro criado após uma requisição `POST /books`.

Exemplo de corpo para `POST /books`:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Consultar, atualizar e remover livros

#### Descrição

Adicione operações para acessar um livro pelo ID, substituir seus dados e removê-lo da coleção.

#### Requisitos

O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar o livro correspondente ao ID.
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor do livro correspondente.
- Implementar `DELETE /books/{book_id}` para remover o livro correspondente.
- Retornar uma resposta HTTP `404` quando o ID solicitado não existir.
- Permitir testar todas as rotas pela documentação interativa em `/docs`.
