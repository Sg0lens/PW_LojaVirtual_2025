import sqlite3
from data.cliente_model import Cliente
from data.cliente_sql import *
from data.util import get_connection

def criar_tabela():
    """
    Cria a tabela de clientes no banco de dados.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir_cliente(cliente):
    """
    Insere um novo cliente na tabela de clientes.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_CLIENTE, (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.senha))
    conn.commit()
    conn.close()

def obter_todos():
    """
    Obtém todos os clientes da tabela de clientes.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    cliente = cursor.fetchall()
    cliente =  [Cliente(id=row[0], nome=row[1], cpf=row[2], email=row[3], telefone=row[4], senha=row[5]) for row in cliente]
    conn.close()
    return cliente