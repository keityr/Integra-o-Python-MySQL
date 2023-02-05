from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

alterar = '''ALTER TABLE contatos ADD COLUMN IF NOT EXISTS(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY)

'''

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(alterar)
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')