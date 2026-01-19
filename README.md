# 📝 My Blog in Python

Um blog simples desenvolvido com **Python** e **Flask**, com sistema de autenticação, posts e comentários.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-06B6D4)

## 🚀 Funcionalidades

- ✅ Cadastro e login de usuários
- ✅ Criar, visualizar posts
- ✅ Sistema de comentários
- ✅ Interface responsiva com Tailwind CSS
- ✅ Banco de dados SQLite

## 📁 Estrutura do Projeto

```
PythonProject/
├── main.py              # Configuração principal do Flask
├── routes.py            # Rotas da aplicação
├── models.py            # Modelos do banco de dados
├── instance/
│   └── blog.db          # Banco de dados SQLite
└── templates/
    ├── base.html        # Template base
    ├── header.html      # Cabeçalho
    ├── index.html       # Página inicial
    ├── post.html        # Página do post
    ├── login.html       # Página de login
    ├── register.html    # Página de cadastro
    ├── add_post.html    # Formulário de post
    └── add_comment.html # Formulário de comentário
```

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python, Flask
- **Banco de Dados:** SQLite, Flask-SQLAlchemy
- **Autenticação:** Flask-Login
- **Front-end:** HTML, Tailwind CSS

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ViniciusN12/MyBlogInPython.git
cd MyBlogInPython
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install flask flask-sqlalchemy flask-login
```

4. Execute a aplicação:
```bash
python main.py
```

5. Acesse no navegador:
```
http://localhost:5000
```

## 📸 Screenshots

| Home | Post | Login |
|------|------|-------|
| Lista de posts | Post com comentários | Formulário de login |

## 🔧 Configuração

O arquivo `main.py` contém as configurações principais:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'minha_chave_secreta'
```

> ⚠️ **Importante:** Altere a `SECRET_KEY` em produção!

## 📝 Rotas da API

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial com posts |
| `/post/<id>` | GET | Visualizar post |
| `/add_post` | GET, POST | Criar novo post |
| `/post/<id>/add_comment` | GET, POST | Adicionar comentário |
| `/login` | GET, POST | Login de usuário |
| `/register` | GET, POST | Cadastro de usuário |
| `/logout` | GET | Logout |

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Desenvolvido por **Vinicius Nunes Santa Catarina**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/viniciussantacatarina)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/ViniciusN12)
