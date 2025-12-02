def insertProdutos(conectionDB, produtos):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO produtos (id_restaurante, descricao) VALUES(%s, %s)', (produtos.getIdRestaurante(), produtos.getDescricaoProduto()))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount