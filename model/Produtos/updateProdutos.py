def updateProdutos(connectionDB, idRestaurante, descricao, idProduto):
    cursor = connectionDB.cursor(dictionary = True)
    cursor.execute('UPDATE produtos SET id_restaurante = %s, descricao = %s WHERE id_produto = %s',
                   (idRestaurante, descricao, idProduto))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount