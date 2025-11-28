def deleteItensPedido(conectionDB, id_ItensPedido):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM itensPedido WHERE id_ItensPedido = %s', (id_ItensPedido))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
