def insertItensPedido(conectionDB, id_pedidos , nome_item, quantidade, preco_unitario):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO ItensPedido (nome, email, senha, telefone) VALUES(%s, %s, %s)', (id_pedidos, nome_item, quantidade, preco_unitario))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
