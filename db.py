# ====== importando sqlite ====== #

import sqlite3 as lite

# ====== Criando conexão ====== #

con = lite.connect('dados.db')

# ====== Criando tabela ====== #

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, rg decimal, endereco TEXT, data_entrada DATE, data_saida DATE, foto TEXT)")
    