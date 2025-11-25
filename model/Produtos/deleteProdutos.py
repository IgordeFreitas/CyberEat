def deleteProdutos(conectionDB, idUsuario):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM Produtos WHERE id_Produtos = %s', (idProdutos))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
