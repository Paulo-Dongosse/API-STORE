# 🛒 API Store

Uma API RESTful desenvolvida com **FastAPI**, **MongoDB** e **Test-Driven Development (TDD)** para o gerenciamento de produtos em uma loja virtual.

> Projeto criado como exercício prático para consolidar conhecimentos em arquitetura de software, testes automatizados e desenvolvimento backend com Python moderno.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10**
- **FastAPI** – Framework leve, rápido e moderno
- **MongoDB** – Banco NoSQL para armazenar os dados
- **Motor** – Driver assíncrono para MongoDB
- **Pydantic** – Validação e serialização de dados
- **HTTPX + Pytest** – Para testes de ponta a ponta
- **Uvicorn** – Servidor ASGI para rodar a API

---

## 🧪 Metodologia TDD

A construção da API seguiu o ciclo do TDD:

1. Escrevi os testes primeiro (cenários reais de uso)
2. Desenvolvi o código necessário para passar nos testes
3. Refatorei e mantive a cobertura de testes

Esse processo garantiu segurança no código e facilitou mudanças.

---

## 📦 Funcionalidades

- ✅ Criar produto
- 🔍 Listar todos os produtos
- 📄 Consultar produto por ID
- ✏️ Atualizar produto
- ❌ Deletar produto

Todas as rotas possuem validações e retornos apropriados.

---

## 🧭 Como rodar localmente

1. Clone o repositório:
```bash
git clone https://
cd api-tdd-store
