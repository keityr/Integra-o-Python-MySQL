from bd import nova_conexao


sql = 'SELECT nome FROM contatos ORDER BY nome'


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(str(registro[0] )for registro in cursor))


