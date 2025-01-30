from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locadora.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(10), nullable=False, unique=True)

class Locacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'), nullable=False)
    data_locacao = db.Column(db.String(20), nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('locacoes', lazy=True))
    veiculo = db.relationship('Veiculo', backref=db.backref('locacoes', lazy=True))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        novo_cliente = Cliente(nome=nome, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('clientes'))
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@app.route('/veiculos', methods=['GET', 'POST'])
def veiculos():
    if request.method == 'POST':
        modelo = request.form['modelo']
        placa = request.form['placa']
        novo_veiculo = Veiculo(modelo=modelo, placa=placa)
        db.session.add(novo_veiculo)
        db.session.commit()
        return redirect(url_for('veiculos'))
    veiculos = Veiculo.query.all()
    return render_template('veiculos.html', veiculos=veiculos)

@app.route('/locacoes', methods=['GET', 'POST'])
def locacoes():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        veiculo_id = request.form['veiculo_id']
        data_locacao = request.form['data_locacao']
        nova_locacao = Locacao(cliente_id=cliente_id, veiculo_id=veiculo_id, data_locacao=data_locacao)
        db.session.add(nova_locacao)
        db.session.commit()
        return redirect(url_for('locacoes'))
    locacoes = Locacao.query.all()
    clientes = Cliente.query.all()
    veiculos = Veiculo.query.all()
    return render_template('locacoes.html', locacoes=locacoes, clientes=clientes, veiculos=veiculos)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
