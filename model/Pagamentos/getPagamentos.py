def queryPagamentos(connectionDB):
    try:
        cursor = connectionDB.cursor(dictionary = True)
        cursor.execute('SELECT * FROM pagamentos')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    except:
        print('Deu ruim')
