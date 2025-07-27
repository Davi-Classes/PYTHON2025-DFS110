from db import get_db
from datetime import datetime, date


def buscar_clientes():
    # Connectando no Banco de Dados
    db = get_db() 

    # Criando o Cursor
    cursor = db.cursor()

    # Script SQL
    sql = '''
        SELECT id, nome, email, data_nascimento, fl_ativo
        FROM clientes
    '''

    # Executando SQL
    cursor.execute(sql)

    # Buscando dados resultantes
    clientes = cursor.fetchall()

    cursor.close()
    db.close()

    return clientes

def criar_cliente(nome: str, email: str, data_nascimento: date, fl_ativo: bool = True):
    # Connectando no Banco de Dados
    db = get_db() 

    # Criando o Cursor
    cursor = db.cursor()

    # Script SQL
    sql = '''
        INSERT INTO clientes (nome, email, data_nascimento, fl_ativo)
        VALUES (?, ?, ?, ?)
    '''

    cursor.execute(sql, (nome, email, data_nascimento.isoformat(), fl_ativo))

    db.commit()

    cursor.close()
    db.close()


# Teste com o Input
# nome = input('Digite o nome do cliente: ')
# email = input('Digite o email do cliente: ')
# data_nascimento = input('Digite a data de nascimento do cliente (YYYY-MM-DD): ')
# data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()

# criar_cliente(nome, email, data_nascimento)

# Teste fixo
# criar_cliente('Moreira', 'moreira@email.com', date(1982, 8, 6), False)


# Buscar Clientes
clientes = buscar_clientes()
print(clientes)