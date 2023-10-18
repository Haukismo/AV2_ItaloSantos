import mysql.connector


conn = mysql.connector.connect(
    host='seu_host',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)
cursor = conn.cursor()

# Inserir um novo usuário na tabela USUARIOS
id_usuario = 1
nome_usuario = 'Usuario1'
console_usuario = 'PS4'
sql = "INSERT INTO USUARIOS (id, nome, console) VALUES (%s, %s, %s)"
val = (id_usuario, nome_usuario, console_usuario)
cursor.execute(sql, val)
conn.commit()
print("Usuário inserido com sucesso!")

# Remover um usuário da tabela USUARIOS
id_usuario_remover = 2
sql = "DELETE FROM USUARIOS WHERE id = %s"
val = (id_usuario_remover,)
cursor.execute(sql, val)
conn.commit()
print("Usuário removido com sucesso!")

# Consultar todos os usuários da tabela USUARIOS
consultar_usuario = (lambda: (lambda conn: (
    (lambda cursor: (lambda rows: [row for row in rows])(cursor.fetchall()))(
        conn.cursor())
))(conn))

# Inserir um novo jogo na tabela JOGOS
id_jogo = 1
nome_jogo = 'Jogo1'
data_lancamento = '2023-01-15'
sql = "INSERT INTO JOGOS (id, nome, data_lancamento) VALUES (%s, %s, %s)"
val = (id_jogo, nome_jogo, data_lancamento)
cursor.execute(sql, val)
conn.commit()
print("Jogo inserido com sucesso!")

# Remover um jogo da tabela JOGOS
id_jogo_remover = 2
sql = "DELETE FROM JOGOS WHERE id = %s"
val = (id_jogo_remover,)
cursor.execute(sql, val)
conn.commit()
print("Jogo removido com sucesso!")

# Consultar todos os jogos da tabela JOGOS
consultar_jogos = consultar_jogos = (lambda: (lambda conn: (
    (lambda cursor: (lambda rows: [row for row in rows])(cursor.fetchall()))(
        conn.cursor())
))(conn))

# Fechar a conexão com o banco de dados
conn.close()