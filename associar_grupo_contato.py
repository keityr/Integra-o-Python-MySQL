from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

selecionar_grupos = '''SELECT id FROM grupos WHERE descricao = %s
'''
atualizar_contato = 'UPDATE contatos SET grupo_id  =  %S WHERE nome %s'


contato_grupo = {
    'Anastacia':'Trabalho',
    'Luca':'Trabalho',
    'Maria':'Casa',
    'Leo':'Casa',
    'Lucy':'Trabalho',
    'Lucia':'Casa',
    'Luca': 'Trabalho',
    'Keity Ranna': 'Casa',
    'Leo':'Casa',
    'Lucy': 'Trabalho',

}
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupos, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato(grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'ERRO...{e.msm}')