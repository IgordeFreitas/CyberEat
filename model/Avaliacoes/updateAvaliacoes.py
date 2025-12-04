def updateAvaliacoes(connctionDB, id_pedidos, nota, comentario, id_avaliacao):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE item_pedido SET id_pedidos = %s, nota = %s, comentario = %s, WHERE id_avaliacao = %s',
                   (id_pedidos, nota, comentario, id_avaliacao,))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount