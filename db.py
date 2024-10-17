import sqlite3

# Conectar ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect('dbProdutos.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT NOT NULL,
        descricao TEXT NOT NULL,
        caminho_img TEXT NOT NULL
    )
''')

# Inserir dados na tabela
cursor.execute('''
    INSERT INTO produtos (nome_produto, descricao)
    VALUES ('Pizza de Frango', 'Ingredientes: Frango, Catupury e Queijo')
''')
cursor.execute('''
    INSERT INTO produtos (nome_produto, descricao)
    VALUES ('Pizza de Queijo', 'Ingredientes: Queijo parmesão, batata palha e azeitona')
''')

# Salvar (commit) as mudanças
conn.commit()

# Consultar os dados
cursor.execute('SELECT * FROM produtos')
produtos = cursor.fetchall()

# Exibir os dados
for produto in produtos:
    print(produto)

# Fechar a conexão
conn.close()