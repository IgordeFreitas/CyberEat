def insertEntregas(conectionDB, entrega):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO entregas (id_endereco, data_entrega ) VALUES(%s, %s)', (entrega.getIdEndereco(), entrega.getDataEntrega()))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
