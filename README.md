# API Escola

A **API Escola** é uma API RESTful desenvolvida com **Django** para gerenciar informações de estudantes, cursos e professores. O projeto visa fornecer uma plataforma simples para organização e consulta de dados escolares, como matrículas de alunos, cursos oferecidos e detalhes de professores.

## Tecnologias

- **Django** - Framework Python para desenvolvimento web
- **Django REST Framework** - Para construir a API RESTful
- **SQLite** - Banco de dados padrão para o desenvolvimento

## Funcionalidades

- Cadastro de Estudantes
- Cadastro de Cursos
- Consulta de Estudantes e Cursos
- Relacionamento entre Estudantes e Cursos
- API de autenticação de usuários (login/logout)

## Instalação

### Clonando o repositório:
```bash
git clone https://github.com/wagnersantan/api_escola.git
cd api_escola

Criando o ambiente virtual:
python3 -m venv venv
source venv/bin/activate  # Para sistemas Unix/Linux
venv\Scripts\activate     # Para Windows

Instalando as dependências:
pip install -r requirements.txt

Aplicando as migrações:
python manage.py migrate

Iniciando o servidor:
python manage.py runserver