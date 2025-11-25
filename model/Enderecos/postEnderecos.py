def insertEnderecos(conectionDB, , bairro):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO Enderecos ( , bairo) VALUES(%s, %s, %s, %s)', ( ,bairro ))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
