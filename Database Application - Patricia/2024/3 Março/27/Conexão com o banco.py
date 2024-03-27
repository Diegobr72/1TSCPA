import oracledb
conn = oracledb.connect(user="RM552603", password="080396",
dsn="oracle.fiap.com.br:1521/orcl")


#recuperar dados da tabela T_PY_ALUNO COM CURSOR

with conn.cursor () as c_consulta:
    cons = "select * from T_PY_ALUNO"
    alunos = list(c_consulta.execute(cons))
    #COMANDO EQUIVALENTE
    #aluno = c_consulta.execute("select * from T_PY_ALUNO")

    print(alunos)