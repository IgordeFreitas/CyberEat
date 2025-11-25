def insertRestaurantes(conectionDB , id_usuarios , id_endereco , nome_restaurante, categoria ):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO restaurantes (id_produto , id_usuarios , id_endereco , nome_restaurante, categoria ) VALUES(%s, %s, %s, %s)', (id_usuarios, id_endereco, nome_restaurante, categoria ))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
