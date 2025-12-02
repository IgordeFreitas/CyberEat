def deleteProdutos(conectionDB, idProduto):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM produtos WHERE id_produto = %s', (idProduto,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
