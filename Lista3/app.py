from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulario',methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        comentario = request.form.get('comentario')
        return f'Obrigada pelo feedback, {nome}!<br><br>Seu email: {email}<br><br>Comentário recebido: {comentario}'
    return render_template('formulario.html')