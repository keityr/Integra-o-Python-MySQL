from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'SELECT * FROM contatos LIMIT 4 OFFSET 0'


with nova_conexao( ) as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print('ERRO!...{e.msg}')
    else:
        for c in contatos:
            print(f'{c[0]:2d} - {c[1]:10s} Telefone: {c[2]:2s}')

