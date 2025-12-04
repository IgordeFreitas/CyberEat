def updateEndereco(connctionDB, id_usuarios, bairro, id_endereco):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE item_pedido SET id_usuarios = %s, bairro = %s, WHERE id_endereco = %s',
                   (id_usuarios, bairro, id_endereco))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount