def insertAvaliacoes(conectionDB, nome, email, senha, telefone):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO usuarios (nome, email, senha, telefone) VALUES(%s, %s, %s, %s)', (nome, email, senha, telefone))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
