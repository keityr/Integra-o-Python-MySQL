from mysql.connector import connect
from contextlib import contextmanager

parametro = dict(
    host='localhost',
    port='3306',
    user='root',
    passwd='',
    database='agenda'

)
@contextmanager
def nova_conexao():
    conexao = connect(**parametro)
    try:
        yield conexao 
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()

