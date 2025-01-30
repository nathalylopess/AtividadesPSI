# 🚗 Sistema de Locação de Veículos

Este é um projeto Flask para gerenciar um sistema de locação de veículos. Ele permite cadastrar clientes, veículos e registrar locações, armazenando os dados em um banco de dados SQLite.

## 📌 Funcionalidades
- 📋 Cadastro de Clientes
- 🚙 Cadastro de Veículos
- 📅 Registro de Locações
- 📄 Listagem de Clientes, Veículos e Locações

## 🛠️ Tecnologias Utilizadas
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML, CSS (para os templates)

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Criar o Banco de Dados
No arquivo `app.py`, as tabelas são criadas automaticamente ao rodar a aplicação. Caso necessário, execute manualmente:
```python
from app import db
with app.app_context():
    db.create_all()
```

### 5️⃣ Executar o Servidor
```bash
python app.py
```
Acesse no navegador: `http://127.0.0.1:5000/`

## 📂 Estrutura do Projeto
```
📁 seu-repositorio/
├── 📂 templates/        # Páginas HTML
│   ├── index.html
│   ├── clientes.html
│   ├── veiculos.html
│   ├── locacoes.html
├── 📂 static/           # Arquivos CSS/JS
│   ├── style.css
├── app.py               # Código principal da aplicação
├── models.py            # Definição das tabelas do banco de dados
├── database.db          # Arquivo do banco SQLite
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
```

## 📝 Autor
Projeto desenvolvido por **Nathaly Lopes**.

## 🏷️ Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar conforme necessário.

