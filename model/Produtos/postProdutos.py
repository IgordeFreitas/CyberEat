def insertProdutos(conectionDB, id_restaurantes, descricao):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO produtos (id_restaurantes, descricao) VALUES(%s, %s', (id_restaurantes, descricao ))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
