from ..controller.testeController import TesteController

tc = TesteController()

sql = "SELECT * FROM usuarios"

def queryUsuarios(connectionDB):
    try:
        query = connectionDB.cursor(dictionary = True)
        query.execute(sql)

        usuarios =  query.fetchAll()
        query.close

    except:
        ...