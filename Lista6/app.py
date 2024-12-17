from flask import Flask, render_template, redirect, request, session, url_for, make_response
from init_db import criar_banco, inserir_usuario, verificar_usuario

app = Flask(__name__)
app.secret_key='ultramegadificil'

criar_banco()

@app.route('/', methods=['POST', 'GET'])
def cadastro():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        inserir_usuario(username,password)

        session['username'] = username
        print(session['username'])
        resposta = make_response(redirect(url_for('dashboard')))
        resposta.set_cookie('username', username, max_age=60*60*24)
        print('Cadastrado com sucesso!')
        return resposta

    else:
        return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if verificar_usuario(username) == True:
            session['username'] = username
            """
            Esse trecho de código cria uma sessão no servidor com os dados do usuário fornecidos
            e envia ao cliente um cookie contendo uma chave criptografada que identifica essa sessão.
            Se fosse possível ver, nesse caso, como os dados são fixos, a sessão seria assim:
            {'username': "admin"}"""
            print(session['username'])

            resposta = make_response(redirect(url_for('dashboard')))
            """
            Caminho que será o usuário será redirecionado após a criação do cookie,
            que é no passo abaixo (acima)."""

            resposta.set_cookie('username', username, max_age=60*60*24)
            """
            Cria um cookie chamado 'username' com o valor da váriavel username (acima)"""

            return resposta
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos.')
    
    elif 'username' in session:
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username') #Recupera dos dados que foram enviados para a sessão
    print(username) 
    if not username:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=username)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None) #Altera a sessão com a chave username para None (equivalente a "vazio")
    resposta = make_response(redirect(url_for('cadastro')))
    resposta.set_cookie('username', '', max_age=0)#Substitui o cookie antigo por um vazio, com tempo maximo zero, ou seja, ele será excluído.
    return resposta

# Ver se minhas observações estão corretas.