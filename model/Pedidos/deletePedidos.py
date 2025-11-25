def deletePedidos(conectionDB, idPedidos):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM pedidos WHERE id_Pedidos = %s', (idPedidos))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
