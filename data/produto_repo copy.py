import sqlite3
from data.cliente_model import Cliente
from data.cliente_sql import *
from data.util import get_connection

def criar_tabela():
    """
    Cria a tabela de produtos no banco de dados.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir_produto(cliente):
    """
    Insere um novo produto na tabela de produtos.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_CLIENTE, (cliente.nome, cliente.CPF, cliente.Email, cliente.Telefone, cliente.Senha))
    conn.commit()
    conn.close()

def obter_todos():
    """
    Obtém todos os produtos da tabela de produtos.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    produtos = cursor.fetchall()
    produtos =  [Cliente(id) for row in produtos]
    conn.close()
    return produtos