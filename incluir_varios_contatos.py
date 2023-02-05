from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


inserir = 'INSERT INTO  contatos (nome, tel) values (%s, %s)'
arg = (
('Ana', '279956-5261'),
('Lucia', '279998-6241'),
('Luca', '2799541-6235'),
('Lu', '2799552-9845'),
('Leo', '2799562-6416'),
('Lucy', '2799509-6120'),
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(inserir, arg)
    except ProgrammingError as e:
        print(f'ERRO!: {e.msg}')    
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')