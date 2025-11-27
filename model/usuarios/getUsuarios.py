def queryUsuarios(connectionDB):
    try:
        cursor = connectionDB.cursor(dictionary = True)
        cursor.execute('SELECT nome, email, senha, telefone FROM usuarios')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    except:
        print('Deu ruim')


