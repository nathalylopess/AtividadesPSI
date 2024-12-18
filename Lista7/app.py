from flask import Flask, render_template, redirect, request, session, url_for, make_response

usuarios_registrados = []

app = Flask(__name__)
app.secret_key='ultramegadificil'

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for usuario in usuarios_registrados:
            if usuario['username'] == username and usuario['password'] == password:
                session['username'] = username
                resposta = make_response(redirect(url_for('dashboard')))
                resposta.set_cookie('username', username, max_age=60*60*24)
                return resposta
        
        return render_template('login.html', erro='Usuário ou senha inválidos.')

    elif 'username' in session:
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nome = request.form['nome']

        for usuario in usuarios_registrados:
            if usuario['username'] == username:
                return render_template('cadastro.html', erro='Usuário já cadastrado.')

        usuarios_registrados.append({'nome' : nome, 'username' : username , 'password' : password}) 
        return redirect(url_for('login'))
    
    return render_template('cadastro.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username') #Recupera dos dados que foram enviados para a sessão
    print(username) 
    if not username:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=username)

@app.route('/usuarios')
def listar_usuarios():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('usuarios.html', usuarios=usuarios_registrados)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None) #Altera a sessão com a chave username para None (equivalente a "vazio")
    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', max_age=0)#Substitui o cookie antigo por um vazio, com tempo maximo zero, ou seja, ele será excluído.
    return resposta