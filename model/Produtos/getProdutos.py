def queryProdutos(connectionDB):
    try:
        cursor = connectionDB.cursor(dictionary = True)
        cursor.execute('SELECT * FROM produtos')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    except:
        print('Deu ruim')
