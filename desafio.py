from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql =  "UPDATE contatos SET nome = %s WHERE id = %s"

with nova_conexao() as conexao:
    try:
        nome = (input('Digite novo nome: '))
        id = (input('Digite o Id desejado: '))
        arg = (f'{nome}', f'{id}')
        cursor = conexao.cursor()
        cursor.execute(sql, arg)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro!...{e.msg}')
    else:
        print(f'{cursor.rowcount} registros foram alterado(s)')

