from flask import Flask, request, render_template, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'chave-secreta' #Definir uma chave é necessário para poder utilizar sessões

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sessao', methods=['POST','GET'])
def iniciar_sessao():
    if request.method == 'POST':
        session['nome'] = request.form['nome'] #Armazena o nome da sessão
        return redirect (url_for('iniciar_sessao'))
    nome =  session.get('nome')
    print(session.get('nome'))
    return render_template('sessao.html', nome=nome)

@app.route('/limpar_sessao')
def limpar_sessao():
    session.pop('nome', None) # Remover o nome da sessão
    return redirect(url_for('iniciar_sessao'))

@app.route('/cookie', methods=['GET','POST'])
def definir_cookie():
    if request.method == 'POST':
        nome = request.form['nome']
        numero = request.form['idade']
        print(numero)
        resposta = make_response(redirect(url_for('definir_cookie')))
        resposta.set_cookie('nome', nome, max_age=60*60*40)
        resposta.set_cookie('numero', numero, max_age=60*60*40) #Cookie válido por um dia
        return resposta
    nome = request.cookies.get('nome')
    numero = request.cookies.get('numero')
    print(nome)
    print(numero)
    return render_template('cookie.html', nome=nome, numero=numero)