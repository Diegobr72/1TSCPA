import oracledb

try:
    conn = oracledb.connect(user="RM552603", password="080396",
dsn="oracle.fiap.com.br:1521/orcl")

except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True

while conexao:

    print("_____ALUNO_____")
    print("""
    1-Recuperar todos os Alunos
    2-Listar o aluno pelo ID
    3-Cadastrar um Aluno
    4-Alterar um Aluno
    5-Excluir um Aluno
    6-Excluir todos os Alunos
    7-Sair do Programa
    """)

    escolha = input("Escolha ->")

    #recuperar dados da tabela T_PY_ALUNO COM CURSOR

    with conn.cursor () as c_consulta:
        cons = "select * from T_PY_ALUNO"
        c_consulta.execute(cons)
        #COMANDO EQUIVALENTE
        #aluno = c_consulta.execute("select * from T_PY_ALUNO")

        alunos = list(c_consulta.fetchall())
        print(alunos)

        #Reculperando um aluno da lista
        print('Recuperando um aluno da tabela')
        c_consulta.execute(cons)
        aluno=list(c_consulta.fetchone())
        print(aluno)