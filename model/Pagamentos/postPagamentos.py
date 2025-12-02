def insertPagamentos(conectionDB, tipo_pagamento, status_pagamento, valor_total):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('INSERT INTO pagamentos (tipo_pagamento, status_pagamento, valor_total) VALUES(%s, %s, %s)', (tipo_pagamento, status_pagamento, valor_total))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
