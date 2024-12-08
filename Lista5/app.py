from flask import Flask, request, render_template, url_for, session, redirect, make_response

app =  Flask(__name__)
app.secret_key =   'SUPERMEGADIFICIL'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario', methods=['GET','POST'])
def salvar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        email = request.form['email']
        #Armazenando dados na Sessão
        session['nome'] = nome
        session['idade'] = idade
        session['email'] = email
        #Armazenando dados em um cookie com valor de um dia
        resposta = make_response(redirect(url_for('salvar_usuario')))
        resposta.set_cookie('nome', nome, max_age=60*60*24)
        resposta.set_cookie('idade', idade, max_age=60*60*24)
        resposta.set_cookie('email', email, max_age=60*60*24)
        return resposta
    #Recuperando dados da sessão ou cookies
    nome = session.get('nome') or request.cookies.get('nome')
    idade = session.get('idade') or request.cookies.get('idade')
    email = session.get('email') or request.cookies.get('email')
    return render_template('usuario.html', nome=nome, idade=idade, email=email)

@app.route('/sair')
def sair():
    session.pop('nome', None)
    session.pop('idade', None)
    session.pop('email', None)
    resposta = make_response(redirect(url_for('salvar_usuario')))
    resposta.set_cookie('nome', '', max_age=0) # Exclui o cookie
    resposta.set_cookie('idade', '', max_age=0)
    resposta.set_cookie('email', '', max_age=0)
    return resposta