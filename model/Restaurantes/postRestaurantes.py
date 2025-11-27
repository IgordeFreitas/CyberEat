def insertRestaurantes(conectionDB, restaurante):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute(
        'INSERT INTO restaurantes (id_usuarios, id_endereco, nome_restaurante, categoria) VALUES(%s, %s, %s, %s)', 
        (restaurante.getIdUsuario(), restaurante.getIdEndereco(), restaurante.getNome(), restaurante.getCategoria())
                )
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
