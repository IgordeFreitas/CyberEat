def updateRestaurante(connctionDB, idUsuario, idEndereco, nome, categoria, idRestaurante): 
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE restaurantes SET id_usuarios = %s, id_endereco = %s, nome_restaurante = %s, categoria = %s WHERE id_restaurantes = %s',
                   (idUsuario, idEndereco, nome, categoria, idRestaurante))    

    cursor.fetchall()
    cursor.close()
