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
