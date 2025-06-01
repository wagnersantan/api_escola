# API Escola

A **API Escola** é uma API RESTful desenvolvida com **Django** e **Django REST Framework** para gerenciar informações de estudantes, cursos e matrículas. O projeto foi criado para fornecer uma plataforma eficiente de organização, validação e consulta de dados escolares.

---

## 🛠️ Tecnologias Utilizadas

- **Django** – Framework Python para desenvolvimento web.
- **Django REST Framework** – Para construção da API RESTful.
- **SQLite** – Banco de dados padrão para desenvolvimento.
- **Django Admin** – Interface administrativa para gerenciamento de dados.

---

## ✅ Funcionalidades

- Cadastro, listagem e gerenciamento de **Estudantes** e **Cursos**.
- Relacionamento entre Estudantes e Cursos via **Matrículas**.
- API para listar **todas as matrículas** de um estudante ou curso.
- **Validações personalizadas** com `validators.py` para garantir integridade e consistência dos dados.
- **Scripts utilitários** para popular rapidamente o banco de dados com estudantes e cursos fictícios.
- Integração com o **Django Admin** para gestão via interface web.
- Estrutura modular e extensível para crescimento futuro.
- **Testes automatizados** organizados por funcionalidades.

---

Estrutura do Projeto:

├── LICENSE  
├── README.md  
├── api_escola  
│   ├── admin             # Configurações administrativas do Django.  
│   ├── apps.py           # Configurações do app 'api_escola'.  
│   ├── migrations        # Controle de versões e alterações no banco de dados.  
│   ├── models            # Definições das classes Estudante, Curso, Matrícula.  
│   ├── routers           # Definições de rotas e ViewSets da API.  
│   ├── serializers       # Serialização e validação dos dados da API.  
│   ├── tests             # Testes automatizados organizados por funcionalidade.  
│   ├── throttles.py      # Controle de limite de requisições.  
│   └── validators.py     # Validações personalizadas.  
├── db.sqlite3            # Banco de dados SQLite.  
├── manage.py             # Script principal de gerenciamento do Django.  
├── popular_banco_cursos.py      # Script para popular cursos fictícios.  
├── popular_banco_estudantes.py  # Script para popular estudantes fictícios.  
├── requirements.txt      # Arquivo com as dependências do projeto.  
├── setup  
│   ├── asgi.py           # Configuração para ASGI.  
│   ├── settings.py       # Configurações principais do Django.  
│   ├── urls.py           # Definições das URLs principais.  
│   └── wsgi.py           # Configuração para WSGI.  
└── venv                  # Ambiente virtual.

📌 Descrição das principais pastas e arquivos  
api_escola/: Código principal da API, incluindo models, serializers, rotas e testes.  

models/: Define as entidades Estudante, Curso e Matrícula.  

serializers/: Define como os modelos são convertidos para JSON e vice-versa.  

routers/: Organização das rotas e ViewSets para os endpoints.  

tests/: Testes unitários e de integração, organizados por funcionalidade.  

validators.py: Contém regras de validação personalizadas para dados.  

throttles.py: Gerencia limites de requisições para evitar abusos.  

setup/: Arquivos de configuração do Django.  

popular_banco_*.py: Scripts utilitários para popular rapidamente o banco de dados.

---

## 🚀 Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/wagnersantan/api_escola.git
cd api_escola

 ### 2.Crie o ambiente virtual:

 ```bash
python3 -m venv venv
source venv/bin/activate  # Para sistemas Unix/Linux
venv\Scripts\activate     # Para Windows

### 3.Instale as dependências:

```bash
pip install -r requirements.txt

### 4.Aplique as migrações
```bash
python manage.py migrate




 

