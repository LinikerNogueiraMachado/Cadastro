import sqlite3 as lite

con = lite.connect('dados.db')



dados = ['José Ribeiro Lopez Cortez','4329804773','Rua Carvalho Melo n302','05/09/2022','06/09/2022','c:imagens']

# ====== inserir dados ====== #

with con:
    cur = con.cursor()
    query = "INSERT INTO cadastro(nome, rg, endereco, data_entrada, data_saida, foto) VALUES(?,?,?,?,?,?)"
    cur.execute(query,dados)

ler_dados = []

# ====== ler dados ====== #

with con:
    cur = con.cursor()
    query = "SELECT * FROM cadastro"
    cur.execute(query,dados)