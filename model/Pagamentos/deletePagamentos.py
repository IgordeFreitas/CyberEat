def deletePagamentos(conectionDB, idPagamentos):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM pagamentos WHERE id_pagamento = %s', (idPagamentos,))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
