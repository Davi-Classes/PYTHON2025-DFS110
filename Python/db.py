import os
import sqlite3


DATABASE_URL = './sql/loja.db'


# Função para criar a conexão
def get_db():
    return sqlite3.connect(DATABASE_URL)


# Se esse arquivo for executado diretamente
if __name__ == '__main__':
    # Exclui o Banco de Dados
    try: 
        os.remove(DATABASE_URL)
        print('Banco de Dados Excluído')
    except FileNotFoundError:
        pass
    
    # Cria a Conexão
    conn = get_db()
    print('Banco de Dados Criado com Sucesso')
    
    # Abrindo o cursor para executar SQL
    cursor = conn.cursor()

    # Script SQL
    with open('./sql/dump.sql', 'r') as file:
        sql = file.read()

    # Executando SQL
    cursor.executescript(sql)

    # Fechando o Cursor
    cursor.close()