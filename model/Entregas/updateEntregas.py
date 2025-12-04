def updateEntregas(connctionDB, id_endereco, data_entrega, id_entrega):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE entregas SET id_endereco = %s, data_entrega = %s, WHERE id_entrega = %s',
                   (id_endereco, data_entrega, id_entrega))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount