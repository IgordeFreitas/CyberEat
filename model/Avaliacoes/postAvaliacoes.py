def insertAvaliacoes(conectionDB, id_pedidos, nota, comentario):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO avaliacoes (id_pedidos, nota, comentario) VALUES(%s, %s, %s)', (id_pedidos, nota, comentario))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
