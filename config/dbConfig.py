import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

try:
    connectionPool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name = 'pool',
        pool_size = 5,
        pool_reset_session = True,
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_name")
    )
    print('Conexão criada com sucesso!')


except:
    print(f'Erro ao criar o pool de conexão')
    
def getConnection():
    if connectionPool is None:
        raise Exception('Erro! Pool de conexão nao iniciada')
    return connectionPool.get_connection()