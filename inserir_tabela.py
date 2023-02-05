from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


inserir = 'INSERT INTO  contatos (nome, tel) values (%s, %s)'
arg = ('Luciano', '27995096261')


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(inserir, arg)
        conexao.commit()
    except ProgrammingError as e:
        print(f'ERRO!: {e.msg}')    
    else:
        print('1 Registro incluído, ID:', cursor.lastrowid)


