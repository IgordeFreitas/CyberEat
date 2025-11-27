def queryEntregas(connectionDB):
    try:
        cursor = connectionDB.cursor(dictionary = True)
        cursor.execute('SELECT * FROM entregas')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    except:
        print('Deu ruim')
