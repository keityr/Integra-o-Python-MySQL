from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """ 
    SELECT 
        grupos.descricao AS grupos
        contatos.nome AS nome
        FROM contatos
        INNER JOIN grupos ON contatos.grupos_id  = grupos.id
        ORDER BY grupo, nome
"""