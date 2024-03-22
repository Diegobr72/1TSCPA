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