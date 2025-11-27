def deleteRestaurantes(conectionDB, idRestaurantes):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM restaurantes WHERE id_Restaurantes = %s', (idRestaurantes, ))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
