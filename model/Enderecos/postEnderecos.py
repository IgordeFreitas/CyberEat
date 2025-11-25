def insertEnderecos(conectionDB, id_usuarios, bairro):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO Enderecos (id_usuarios, bairo) VALUES(%s, %s)', (id_usuarios, bairro ))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
