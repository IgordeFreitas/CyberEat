def insertAvaliacoes(conectionDB, id_pedidos, nota, comentario):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO avaliacoes (nota, comentario) VALUES(%s, %s)', (nota, comentario))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
