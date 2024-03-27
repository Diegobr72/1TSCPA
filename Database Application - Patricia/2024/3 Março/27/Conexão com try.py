import oracledb

try:
    conn = oracledb.connect(user="rm552603", password="080396", dsn="oracle.fiap.com.br:1521/orcl")
except Exception as e:
    print("Erro:", e)
    # Conexao com o banco falhou
    # Flag para não executar a aplicacao
    conexao = False
else:
    # Flag para executar a aplicacao
    conexao = True

while conexao:
    # Apresentando o menu
    print("------ ALUNO -------")
    print("""
    1-Recuperar todos os alunos
    2-Listar o aluno pelo id
    3-Cadastrar um aluno
    4-Alterar um aluno
    5-Excluir um aluno
    6-Excluir todos os alunos
    7-SAIR
    """)
    # Capturar a escolha do usuario
    escolha = input("Escolha ->")
    # Verificar se é um valor numerico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        print("Digite um numero.\nReinicie a Aplicacao")
        escolha = 7  # alterando a escolha para 7 que é o sair

    if escolha == 7:
        conexao = False

    if escolha == 1:
        # recuperar dados da tabela T_PY_ALUNO COM CURSOR
        with conn.cursor() as c_consulta:
            cons = "select * from T_PY_ALUNO"
            print('Recuperando todos os alunos da tabela')
            c_consulta.execute(cons)
            alunos = list(c_consulta.fetchall())

            if len(alunos) == 0:
                print("Nenhum aluno na tabela")
            else:
                print(alunos)

    if escolha == 2:
        # Recuperando um aluno da lista
        with conn.cursor() as c_consulta:
            id_aluno = int(input("Qual o número do ID do aluno que gostaria de recuperar? "))
            print(f'Recuperando o ID {id_aluno} do aluno da tabela')
            c_consulta.execute(f"SELECT * FROM T_PY_ALUNO WHERE id = {id_aluno}")
            aluno = c_consulta.fetchone()

            if aluno is None:
                print("Nenhum aluno encontrado com o ID fornecido.")
            else:
                print(aluno)

    if escolha == 3:
        print("\nCadastrar um aluno")
        nome = input("Qual o nome do aluno? ")
        idade = int(input("Qual a idade do aluno? "))
        endereco = input("Qual o endereço do aluno? ")
        curso = input("Qual o curso desse aluno? ")

        with conn.cursor() as c_insert:
            try:
                c_insert.execute("INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES (:1, :2, :3, :4)",
                                 (nome, idade, endereco, curso))
                print("Aluno cadastrado com sucesso.")
            except Exception as e:
                print("Erro ao cadastrar aluno:", e)

conn.close()
