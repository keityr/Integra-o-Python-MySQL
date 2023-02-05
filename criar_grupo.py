from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_grupo = ''' 
    CREATE TABLE IF NOT EXISTS grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)

)
'''
alterando_tabela_contato = ''' ALTER TABLE contatos ADD grupo_id INT'''

alterando_tabela_contato2 = '''
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES  grupos(id) 
    )

'''
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_grupo)
        cursor.execute(alterando_tabela_contato)
        cursor.execute(alterando_tabela_contato2)

    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')