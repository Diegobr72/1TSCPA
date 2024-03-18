animais_cadastrados = 0
raiva_qtd = 0
v8_qtd = 0
giardiase_qtd = 0

contagem_animais = {"Gato": 0, "Cachorro": 0}

respostas_positivas = ["sim", "s", "y", "yes"]
respostas_negativas = ["não", "n", "no", "nao"]

apelidos_gato = ["gato", "cat", "g"]
apelidos_cachorro = ["cachorro", "dog", "c", "d"]

while True:
    cadastrar = input('\nDeseja cadastrar um novo animal? Responda S (sim) ou N (não): ').lower()

    if cadastrar in respostas_negativas:
        break

    if cadastrar not in respostas_positivas:
        print('Resposta inválida. Por favor, digite uma resposta válida.')
        continue

    nome = input('\nDigite o nome do animal: ')
    tipo_animal = input('\nDigite o tipo do animal (Gato ou Cachorro): ').lower()

    if tipo_animal in apelidos_gato:
        tipo_animal = "Gato"
    elif tipo_animal in apelidos_cachorro:
        tipo_animal = "Cachorro"
    else:
        print('Resposta inválida. Por favor, digite uma resposta válida (Gato ou Cachorro).')
        continue

    contagem_animais[tipo_animal] += 1

    giardiase = input(f'\nO {nome} precisa de vacinação contra giardiase? Responda S ou N: ').lower()
    if giardiase in respostas_positivas:
        giardiase_qtd += 1

    v8 = input(f'\nO {nome} precisa de vacinação contra V8? Responda S ou N: ').lower()
    if v8 in respostas_positivas:
        v8_qtd += 1

    raiva = input(f'\nO {nome} precisa de vacinação contra raiva? Responda S ou N: ').lower()
    if raiva in respostas_positivas:
        raiva_qtd += 1

    print("\n----------------------------------------------------------------------------------")
    print(f"Status de vacinação do(a) {tipo_animal} {nome}:")
    print("\nVacina contra Giardiase:", "OK" if giardiase in respostas_positivas else "Não necessária")
    print("Vacina contra V8:", "OK" if v8 in respostas_positivas else "Não necessária")
    print("Vacina contra Raiva:", "OK" if raiva in respostas_positivas else "Não necessária")
    print("----------------------------------------------------------------------------------")

    animais_cadastrados += 1

print("----------------------------------------------------------------------------------")
print(f"A vacinação acabou por hoje, totalizando {animais_cadastrados} animais que foram vacinados.")
print(f"Número de vacinas usadas contra Giardiase: {giardiase_qtd}")
print(f"Número de vacinas usadas contra Raiva: {raiva_qtd}")
print(f"Número de vacinas usadas contra V8: {v8_qtd}")
print("\nParticipou da campanha:\n")
print(f"Número de gatos: {contagem_animais['Gato']}")
print(f"Número de cachorros: {contagem_animais['Cachorro']}")
print("----------------------------------------------------------------------------------")