A **API Escola** é uma API RESTful desenvolvida com **Django** e **Django REST Framework** para gerenciar informações de estudantes, cursos e matrículas. O projeto foi desenvolvido para fornecer uma plataforma para organização e consulta de dados escolares.

## Tecnologias

- **Django** - Framework Python para desenvolvimento web
- **Django REST Framework** - Para construir a API RESTful
- **SQLite** - Banco de dados padrão para o desenvolvimento
- **Django Admin** - Para gerenciamento das entidades via interface administrativa

## Funcionalidades

- Cadastro de Estudantes
- Cadastro de Cursos
- Consulta de Estudantes e Cursos
- Relacionamento entre Estudantes e Cursos via Matrículas
- API para listar matrículas de estudantes e cursos
- Integração com Django Admin para gerenciamento de dados

## Instalação

### Clonando o repositório:
```bash
git clone https://github.com/wagnersantan/api_escola.git
cd api_escola

# Criando o ambiente virtual:
python3 -m venv venv
source venv/bin/activate  # Para sistemas Unix/Linux
venv\Scripts\activate     # Para Windows

# Instalando as dependências:
pip install -r requirements.txt

# Aplicando as migrações:
python manage.py migrate

# Iniciando o servidor:
python manage.py runserver

# Acesse a API pelo endereço: http://127.0.0.1:8000/

# Testes
# Para rodar os testes, execute o seguinte comando:
python manage.py test

# Contribuições
# Sinta-se à vontade para contribuir! Abra um pull request ou envie uma issue.

# Licença
# Este projeto está licenciado sob a MIT License.