import sqlite3

def criar_banco():
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()

    cursor.execute ("""
    CREATE TABLE IF NOT EXISTS tb_usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                    )
    """)

    conexao.commit()
    conexao.close()

    print('Banco criado com sucesso.')

def inserir_usuario(username,password):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO tb_usuarios (username,password) VALUES (?,?)
    """, (username,password))
    
    conexao.commit()
    conexao.close()

def verificar_usuario(username):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM tb_usuarios WHERE username=?
    """, (username,))
    usuario = cursor.fetchone()

    conexao.close()

    if usuario:
        return True
    else:
        return False

    