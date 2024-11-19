from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/redirecionar')
def redirecionar():
    return redirect(url_for('home')) #Redirecionar um rota para outra

@app.route('/sobre')
def sobre():
    return "Esta é a página sobre."

@app.route('/perfil/<nome>')
def perfil(nome):
    if nome.lower() == "anônimo":
        return redirect(url_for('home')) #ISSO AQUI É PARA REDIRECIONAR DE UMA ROTA PARA OUTRA!!
    return f"Olá, {nome}! Bem-vindo(a) ao seu perfil."
