def deleteAvaliacoes(conectionDB, idAvaliacoes):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM avaliacoes WHERE id_avaliacoes = %s', (idAvaliacoes))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
