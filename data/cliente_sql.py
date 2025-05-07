CRIAR_TABELA="""
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    CPF TEXT NOT NULL,
    Email TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    Senha TEXT NOT NULL)
    """

INSERIR_CLIENTE="""
INSERT INTO cliente (nome, CPF, Email, Telefone, Senha) VALUES (?, ?, ?, ?, ?)
"""
OBTER_TODOS="""
SELECT
id, nome, CPF, Email, Telefone, Senha
FROM cliente
"""