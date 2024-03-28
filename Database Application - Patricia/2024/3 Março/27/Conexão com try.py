import oracledb


def obter_credenciais():
    user = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    dsn = input("Digite o DSN (host:porta/serviço): ")
    return user, password, dsn

try:
    user, password, dsn = obter_credenciais()

    conn = oracledb.connect(user=user, password=password, dsn=dsn)

except oracledb.DatabaseError as e:
    error, = e.args
    if error.code == 1017:
        print("Erro de autenticação: Nome de usuário ou senha incorretos.")
    else:
        print("Erro ao conectar ao banco de dados:", e)
    # Conexão com o banco falhou
    # Flag para não executar a aplicação
    conexao = False

except Exception as e:
    print("Erro:", e)
    # Conexão com o banco falhou
    # Flag para não executar a aplicação
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
      7-Insere dados a partir do CSV
      8-SAIR
      """)

    # Capturar a escolha do usuario
    escolha = input("Escolha -> ")
    # Verificar se é um valor numerico
    if escolha.isdigit():
        escolha = int(escolha)
    else:
        print("Digite um numero.\nReinicie a Aplicacao")
        escolha = 8  # alterando a escolha para 8 que é o sair

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

    if escolha == 4:
        print("\nAlterar um aluno")
        aluno = []
        id = int(input("Qual o número do ID do aluno que gostaria de alterar? "))
        with conn.cursor() as c_consulta:
            c_consulta.execute(f"SELECT * FROM T_PY_ALUNO WHERE id = {id}")
            aluno = list(c_consulta.fetchall())
            if len(aluno) == 0:
                print(f'Nao ha dados deste aluno de id:{id}')
            else:
                print(aluno)
                print('Dados a serem alterados')
                # solicita dados dos alunos
                nome = input("Entre com o nome: ")
                idade = int(input("Entre com a idade: "))
                endereco = input("Entre com o endereco: ")
                curso = input("Entre com o curso: ")
                # monta o comando de insercao
                cmd = f"UPDATE T_PY_ALUNO SET nome = '{nome}', idade = {idade}, endereco = '{endereco}', curso='{curso}'" \
                      f" WHERE id = {id} "
                with conn.cursor() as c_update:
                    c_update.execute(cmd)
                conn.commit()
                aluno = []
                with conn.cursor() as c_consulta:
                    cons = f"select * from T_PY_ALUNO where nome = '{nome}'"
                    c_consulta.execute(cons)
                    aluno = list(c_consulta.fetchall())
                    if len(aluno) == 0:
                        print('Aluno não se encontra na base')
                    else:
                        print(aluno)

    if escolha == 5:
        print("\nExcluindo um aluno")
        aluno = []
        id = int(input("Qual o número do ID do aluno que gostaria de excluir? "))
        with conn.cursor() as c_consulta:
            c_consulta.execute(f"SELECT * FROM T_PY_ALUNO WHERE id = {id}")
            aluno = list(c_consulta.fetchall())
            if len(aluno) == 0:
                print(f'Nao ha dados deste aluno de id:{id}')
            else:
                print(aluno)
                with conn.cursor() as c_delete:
                    cmd = "DELETE T_PY_ALUNO WHERE id = :1"
                    c_delete.execute(cmd, (id,))
                    print("aluno excluido com sucesso")
                conn.commit()

    if escolha == 6:
        print("\nExcluindo TODOS os aluno")
        cmd = "DELETE FROM T_PY_ALUNO"
        with conn.cursor() as c_delete:
            c_delete.execute(cmd)
            print("alunos excluidos com sucesso")

        conn.commit()

    if escolha == 7:
        import csv

        with open('alunos.csv', 'r', encoding='UTF-8') as arqAluno:
            csvAluno = csv.reader(arqAluno, delimiter=';')
            listaAlunos = list(csvAluno)
            print(listaAlunos)

        print('\n\nLinhas da Lista')
        print(listaAlunos[1:])
        for linha in listaAlunos[1:]:
            print(linha)
            with conn.cursor() as c_insert:
                c_insert.execute("INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES (:1, :2, :3, :4)",
                                 (linha[0], linha[1], linha[2], linha[3]))
            conn.commit()
            print("Aluno cadastrado com sucesso.")

    if escolha == 8:
        conexao = False

conn.close()