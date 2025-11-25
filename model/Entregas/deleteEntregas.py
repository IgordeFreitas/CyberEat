def deleteEntregas(conectionDB, idEntregas):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM Entregas WHERE id_Entregas = %s', (idEntregas))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
