from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-Vindo ao Flask!"

@app.route('/sobre')
def about():
    return "Esta página é sobre:"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"Olá {nome} seja bem vindo(a)!"

@app.route('/contato/<nome>')
def contato(nome):
    return f"Olá {nome}, você está na página de contato. Fique a vontade para nos contatar."    