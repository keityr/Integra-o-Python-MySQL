from mysql.connector import connect

conexao = connect(
    host='localhost',
    port='3306',
    user='root',
    passwd=''
)

# Criando um banco de dados no Workbench com CREATE DATABASE IF NOT EXISTS
cursor = conexao.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')