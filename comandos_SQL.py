import pyodbc

dados_conexao = ("Driver={SQL Server};"
                 "Server=Seu_Servidor;"
                 "Database=BancoDeDados")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

valor_coluna1 = "qualquer valor"
valor_coluna2 = "outro valor"
valor_coluna3 = 1000
valor_coluna4 = 1000

# Adicionar
comando = f"""INSERT INTO Tabela(coluna1, coluna2, coluna3, coluna4)
    VALUES
        ('{valor_coluna1}', '{valor_coluna2}', '{valor_coluna3}', '{valor_coluna4}')"""
cursor.execute()
cursor.commit()


# Atualizar
comando = comando = f"""UPDATE Tabela
        SET coluna3 = coluna3 + {valor_coluna3}
        WHERE coluna1 = '{valor_coluna1}';
        """
cursor.execute()
cursor.commit()


# Deletar
comando = f"""DELETE from Tabela
            WHERE coluna1 = '{valor_coluna1}';
            """
cursor.execute()
cursor.commit()


# Ler
comando = comando = f"""SELECT * from Tabela
            WHERE coluna1 = '{valor_coluna1}';
            """
cursor.execute()
for row in cursor.fetchall():
    texto = f"Item: {row.coluna1}; Quantidade: {row.coluna2}; Lote:{row.coluna3}; Validade:{row.coluna4}"
    print(texto)
