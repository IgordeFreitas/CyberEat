def deletePagamentos(conectionDB, idPagamentos):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM pagamentos WHERE id_pagamentos = %s', (idPagamentos))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
