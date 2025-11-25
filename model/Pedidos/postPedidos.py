def insertPedidos(conectionDB, id_restaurantes , id_usuarios , id_endereco , id_pagamento, id_entrega ):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO Pedidos (id_restaurantes, id_usuarios, id_endereco, id_pagamento, id_entrega ) VALUES(%s, %s, %s, %s)', (id_restaurantes, id_usuarios, id_endereco, id_pagamento, id_entrega))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
