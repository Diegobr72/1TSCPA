print("cardapio da festa")

entradas = ['Queijo Roquefort']
#entradas = []
while True:
    entrada = input("Digite uma entrada (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        break
    else:
        entradas.append(entrada)

entradaDefinidas = tuple(entradas)
print(type(entradaDefinidas))

print(entradaDefinidas)

if 'Queijo Roquefort' in entradaDefinidas:
  print('Tem Roquefort')
  localRoquefort = entradaDefinidas.index('Queijo Roquefort')
  print(localRoquefort)
else:
  entradaDefinidas = list(entradaDefinidas)
  entradaDefinidas.append('Queijo Roquefort')
  localRoquefort = len(entradaDefinidas) - 1
  entradaDefinidas = tuple(entradaDefinidas)
  print(entradaDefinidas)
  print(localRoquefort)

print("Entradas digitadas:")
for entrada in entradaDefinidas:
    print(entrada)

# Sua irmã não quer providenciar mais nada e para não chateá-la você transformou essa lista em uma coleção imutável. Apresente a coleção
# Você esqueceu das azeitonas e não tem como pedir para sua irmã providenciar mais nada. A não ser que ela não note que você colocou mais esse item na sua coleção. Para garantir isso coloque a azeitona logo após o queijo Roquefort. Continue o seu algoritmo anterior
# 0  	                  1            2
#('Queijo Roquefort', 'tremoço', 'sunomomo')
entradaDefinidas = list(entradaDefinidas)
entradaDefinidas.insert(localRoquefort+1, 'azeitonas')
entradaDefinidas = tuple(entradaDefinidas)
print(entradaDefinidas)


# A sua prima resolveu ajudar quando sua irmã já estava dando um PITI. Altere seu algoritmo para fornecer uma coleção com os 3 últimos itens da coleção da sua irmã.

 #0                    1             2         3
#('Queijo Roquefort', 'azeitonas', 'tremoco', 'sunomomo')
#descobrir o tamanho da lista e tirar um pq a lista comeca em zero
#fazer conta, seu eu quero os 3 ultimos itens, eu tenho que tirar tres do tamanho, e fazer daquela conta até o tamanho
#EX: tamanho 4 itens, 4 - 3 = 1
#slicing vai de 1 até o proprio tamanho
if len(entradaDefinidas) >= 3:
  print('Tupla Prima pelo lado positivo')
  tamanho = len(entradaDefinidas)
  inicio = tamanho -3
  tuplaPrima = entradaDefinidas[inicio:tamanho]
  print(tuplaPrima)

#    -4                    -3             -2         -1
#('Queijo Roquefort', 'azeitonas', 'tremoco', 'sunomomo')
#o slicing  funciona "sempre" no sentido da esquerda para a direita (a menos que eu diga ao contrario)
if len(entradaDefinidas) >= 3:
  print('Tupla Prima pelo lado negativo')
  tuplaPrima = entradaDefinidas[-3:]
  print(tuplaPrima)

# Sua prima é muito nova ainda e não tem noção da quantidade de cada item! Você deve ajuda-la criando pequenas listas com as quantidades dentro da coleção imutável dela.
# A sua reunião se tornou festa! Você vai ter que providenciar mais comida. Duplique todos os itens já listados.

tuplaPrima = ('azeitonas', 'temoco', 'sunomomo', 'brie')

quantidades = [500, 200, 800, 555]

listaTmp = []
for elemento in tuplaPrima:
  qtd = int(input(f'Entre com a quantidade do {elemento}:'))
  listaTmp.append([elemento, qtd])
print(listaTmp)
tuplaPrima = tuple(listaTmp)
print(tuplaPrima)
del listaTmp