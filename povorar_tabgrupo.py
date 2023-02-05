from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = ' INSERT INTO grupos (descricao) VALUES (%s)'
arg = (
    ('Casa',),
    ('Trabalho',),
    ('Academia',),
    ('Auto Escola',),
    ('Hospital',),
) 
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, arg)
        conexao.commit()
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
