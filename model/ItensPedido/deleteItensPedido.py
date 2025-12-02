def deleteItensPedido(conectionDB, id_ItensPedido):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM itens_pedido WHERE id_item_pedido = %s', (id_ItensPedido,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
