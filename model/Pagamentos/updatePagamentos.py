def updatePagamentos(connctionDB, tipo_pagamento, status_pagamento, valor_total, idPagamentos):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE pagamentos SET tipo_pagamento = %s, status_pagamento = %s, valor_total = %s WHERE id_pagamento = %s',
                   (tipo_pagamento, status_pagamento, valor_total, idPagamentos))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount