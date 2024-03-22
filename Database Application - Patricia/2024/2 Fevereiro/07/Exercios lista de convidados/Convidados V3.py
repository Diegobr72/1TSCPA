#Exercicios
# Acabou a pandemia, chegou o dia e você está ajudando a montar a lista de uma pequena reunião no seu apartamento. Conversando com o seu síndico ele proibiu que houvesse mais de 15 pessoas no seu apartamento.  Faça um algorimo que peça a quantidade de pessoas da sua reunião. E utilizando a função FOR peça o nome dos convidados um a um.  Certifique-se que seu melhor amigo João está na sua lista

# Você vai precisar dos nomes em ordem alfabética para poder enviar a portaria. Altere seu algoritmo e ordene a sua lista. Depois apresente o resultado

limite_pessoas = 15
qtd_anfitrioes = 2
qtd_convidados = 3
qtd_convidados_especiais = 1 #João


qtd_convidados = int(input('Qtos convidados vao estar festa? '))

if qtd_anfitrioes + qtd_convidados + qtd_convidados_especiais > limite_pessoas:
  print(f"Convide menos pessoas. Hoje temos {qtd_convidados} convidados", )
else:
  listaConvidados = []

  for i in range(qtd_convidados):
    convidado = input('Entre com o nome do convidado: ')
    listaConvidados.append(convidado)
  print(listaConvidados)
  if 'João' not in listaConvidados:
    print('Você esqueceu o João. Vamos acrescentar')
    listaConvidados.append('João')
  print(listaConvidados)
  #o sorted é um metodo nativo do Python portanto ele é capaz de fazer a ordenação, mas ele não altera a lista original
  print('Ordenacao com o SORTED - NAO ALTERA A LISTA ORIGINAL')
  print(sorted(listaConvidados))
  print(listaConvidados)
  #já o método .sort() da lista, acaba fazendo a ordenação e também altera para todo sempre a lista original, ou seja você perde a ordem que foi inserido os dados
  print('Ordenacao com o SORT() - ALTERA A LISTA ORIGINAL')
  listaConvidados.sort()
  print(listaConvidados)

  # Falando com a portaria,  foi pedido que adicionasse o número do RG em frente cada um dos nomes dos convidados. Altere seu algoritmo para colocar esses documentos na ordem solicitada. Exemplo ['Pat', 345453, 'Hamilton', 924504]
  listaTemporariaConvidados = []
  for elemento in listaConvidados:
    rg = int(input(f"Entre com o RG do convidado {elemento}: "))
    listaTemporariaConvidados.append(elemento)
    listaTemporariaConvidados.append(rg)
  print(listaTemporariaConvidados)
  listaConvidados = listaTemporariaConvidados



# Você percebeu que esse primeira reunião vai passar de 20 pessoas e você alugou o salão de festas do seu condomíno. Sendo assim você vai precisar alterar seu algoritmo e agora não vai mais utilizar o comando FOR, vai utilizar o comando WHILE e enquanto a resposta da pergunta “Tem mais convidados” for igual a SIM você cadastrará um novo amigo na sua lista.


listaConvidados = []
resp = 's'
while resp in ('s', 'sim', 'y', 'yes'):
  convidado = input('Entre com o nome do convidado: ')
  listaConvidados.append(convidado)
  resp = input('Ha convidados para cadastrar? ')

if 'João' not in listaConvidados:
  print('Você esqueceu o João. Vamos acrescentar')
  listaConvidados.append('João')
listaConvidados.sort()
print(listaConvidados)
