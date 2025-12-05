def updateItensPedido(connctionDB, id_pedidos, nome_item, quantidade, preco_unitario, id_item_pedido):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE itens_pedido SET id_pedidos = %s, nome_item = %s, quantidade = %s, preco_unitario = %s WHERE id_item_pedido = %s',
                   (id_pedidos, nome_item, quantidade, preco_unitario, id_item_pedido))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount