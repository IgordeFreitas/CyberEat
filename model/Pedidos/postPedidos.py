def insertPedidos(conectionDB, pedido):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute(
        'INSERT INTO pedidos (id_restaurantes, id_usuarios, id_endereco, id_pagamento, id_entrega ) VALUES(%s, %s, %s, %s, %s)', 
        (pedido.getIdRestaurantes(), pedido.getIdUsuarios(), pedido.getIdEndereco(), pedido.getIdPagamento(), pedido.getIdEntrega())
        )
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
