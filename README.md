# Projeto de Estudo - Integração com Banco de Dados

Este é um projeto de estudo desenvolvido para implementar a integração com banco de dados em uma atividade do SENAI. O objetivo é aprender e aplicar conceitos de banco de dados, incluindo a criação, manipulação e consulta de dados, utilizando tecnologias e ferramentas adequadas.

## Objetivos

- Aprender conceitos de banco de dados
- Implementar a criação, manipulação e consulta de dados
- Utilizar tecnologias e ferramentas adequadas

## Tecnologias Utilizadas

- Banco de Dados: SQLite
- Linguagem de Programação: Python
- Framework: Django

## Estrutura do Projeto

1. Configuração do Ambiente
2. Criação do Banco de Dados
3. Desenvolvimento da Aplicação

## Como Executar

1. Clone o repositório
    ```bash
    git clone https://github.com/orangethewell/funeraria-folia.git
    ```
2. Configure o ambiente virtual
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```
4. Faz a migração do banco de dados
    ```bash
    python manage.py migrate
    ```
5. Execute a aplicação
    ```bash
    python manage.py runserver
    ```

## Licença

Este projeto não possui licença, sinta-se livre para copiá-lo e modificá-lo