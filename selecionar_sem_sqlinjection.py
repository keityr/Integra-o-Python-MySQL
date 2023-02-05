from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome LIKE %s"


with nova_conexao() as conexao:
    nome = input('Contato localizar: ')
    arg = (f'{nome}', )
    cursor = conexao.cursor()
    cursor.execute(sql, arg)
    for x in cursor:
        print(x)