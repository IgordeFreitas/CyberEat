def updatePagamento(connectionDB, tipo_pagamento, status_pagamento, valor_total, id_pagamento):
    cursor = connectionDB.cursor(dictionary = True)
    cursor.execute('UPDATE pagamentos SET tipo_pagamento = %s, status_pagamento = %s, valor_total = %s WHERE id_pagamento = %s',
                   (tipo_pagamento, status_pagamento, valor_total, id_pagamento))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount