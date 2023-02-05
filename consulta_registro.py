from bd import nova_conexao


sql = 'SELECT nome, tel FROM contatos LIMIT 4 OFFSET 10'



with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())