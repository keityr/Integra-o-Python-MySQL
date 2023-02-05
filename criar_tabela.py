from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = ''' CREATE TABLE IF NOT EXISTS  contatos(nome VARCHAR(50),
tel VARCHAR(40)

)
'''
tabela_email = '''
CREATE TABLE IF NOT EXISTS email (
ID int auto_increment primary key,
dono VARCHAR(50) 
)

'''

tabela_nascimento = ''' CREATE TABLE IF NOT EXISTS nascimento ( nome VARCHAR(50),
 nascimento INT
)
'''

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_email)
        cursor.execute(tabela_nascimento)
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')


