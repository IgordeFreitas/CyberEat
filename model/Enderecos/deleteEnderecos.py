def deleteEnderecos(conectionDB, idEnderecos):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM Enderecos WHERE id_Enderecos = %s', (idEnderecos))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
