from bd import nova_conexao


with nova_conexao() as conexao:
    if conexao.is_connected():
        print('Conectado ao banco de dados agenda')

print('FIM')