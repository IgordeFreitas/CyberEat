def insertUsuarios(conectionDB, user):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute(
        'INSERT INTO usuarios (nome, email, senha, telefone) VALUES(%s, %s, %s, %s)',
        (user.getNome(), user.getEmail(), user.getSenha(), user.getTelefone())
                    )
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount