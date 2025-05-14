# API Escola

A **API Escola** é uma API RESTful desenvolvida com **Django** e **Django REST Framework** para gerenciar informações de estudantes, cursos e matrículas. O projeto foi desenvolvido para fornecer uma plataforma para organização, validação e consulta de dados escolares.

## 🛠️ Tecnologias

- **Django** – Framework Python para desenvolvimento web  
- **Django REST Framework** – Para construção da API RESTful  
- **SQLite** – Banco de dados padrão para desenvolvimento  
- **Django Admin** – Interface administrativa para gerenciamento de dados

## ✅ Funcionalidades

- Cadastro, listagem e gerenciamento de **Estudantes** e **Cursos**
- Relacionamento entre Estudantes e Cursos via **Matrículas**
- API para listar **todas as matrículas** de um estudante ou curso
- **Validações personalizadas** com uso de `validators.py` para garantir integridade e consistência dos dados
- **Scripts utilitários** para popular rapidamente o banco de dados com estudantes e cursos fictícios
- Integração com o **Django Admin** para gestão via interface web
- Estrutura modular e extensível para crescimento futuro

## 🚀 Instalação

### Clonando o repositório:
```bash
git clone https://github.com/wagnersantan/api_escola.git
cd api_escola

### Criando o ambiente virtual:
python3 -m venv venv
source venv/bin/activate  # Para sistemas Unix/Linux
venv\Scripts\activate     # Para Windows

### Instalando as dependências:
pip install -r requirements.txt

### Aplicando as migrações:
python manage.py migrate

### Acesse a API pelo endereço::
 http://127.0.0.1:8000/

 ### 📦 Scripts para popular o banco de dados
python popular_banco_estudantes.py
python popular_banco_cursos.py

### Para rodar os testes automatizados do projeto:
python manage.py test


