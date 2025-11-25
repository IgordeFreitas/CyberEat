def insertEntregas(conectionDB, id_endereco,data_entrega):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO entregas (id_endereco, data_entrega ) VALUES(%s)', (id_endereco, data_entrega))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
