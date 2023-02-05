from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

modif = '''ALTER TABLE agenda.contatos MODIFY COLUMN ID INT AUTO_INCREMENT FIRST'''



with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(modif)
    except ProgrammingError as e:
        print(f'ERRO! {e.msg}')
