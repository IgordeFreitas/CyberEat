def loginUsuario(connectionDB, nome, senha):
    try:
        cursor = connectionDB.cursor(dictionary = True)
        cursor.execute('SELECT nome, email, telefone FROM usuarios WHERE nome = %s AND senha = %s', 
                       (nome, senha,))
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios
    except:
        print('Deu ruim')