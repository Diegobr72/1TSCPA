print("Progama para verificar qual seu abastecimento!")
bloco = int(input("Digite qual o numero do seu bloco?"))
if bloco % 2 == 0:
    caixa = "A"
else:
    caixa = "B"

print("Seu abastecimento é pela caixa d' Agua",caixa,"!")
print("Em caso de duvidas estamos a disposição!")

#Pedro
bloco = int(input('Em qual bloco você mora? ').upper())
if bloco == 2 or bloco == 4:
    print('Você mora no bloco A')
elif bloco == 'BLOCO 1' or bloco == 'BLOCO 3':
    print('Você mora no bloco B')
else:
    print('Fora da pesquisa.')
