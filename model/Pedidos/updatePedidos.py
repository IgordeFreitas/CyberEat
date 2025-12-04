def updatePedidos(connctionDB, id_restaurante, id_usuarios, id_endereco, id_pagamento, id_entrega, idPedido):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE pedidos SET id_restaurantes = %s, id_usuarios = %s, id_endereco = %s, id_pagamento = %s, id_entrega = %s WHERE id_pedidos = %s',
                   (id_restaurante, id_usuarios, id_endereco, id_pagamento, id_entrega, idPedido))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount