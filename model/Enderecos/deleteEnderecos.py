def deleteEnderecos(conectionDB, idEnderecos):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM enderecos WHERE id_Enderecos = %s', (idEnderecos))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
