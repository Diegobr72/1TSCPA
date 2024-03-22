#Tupla
#coleções do tipo IMUTAVEL
#uma vez criada, não se pode alterar
#nao podemos acrescentar ou retirar elementos
#Indexável(ou seja cada elemento tem o seu lugar)
#Permitem repetidos
#Sao muito usadas no comando for
#TODA COLECAO É UM ELEMENTO ITERAVEL
#iteravel = consigo percorrer um a um

print('TUPLAS')
minhaTupla = ('sono','comida','sol','sono')
print(minhaTupla)
print(type(minhaTupla))

# 0       1        2      3
#-4      -3       -2     -1
#('sono','comida','sol','sono')
print('Primeiro elemento:', minhaTupla[0])
print('Ultimo elemento:', minhaTupla[-1])
print('Segundo elemento:', minhaTupla[-3])

#slicing
#todo elemento iteravel indexado pode ser partido, como se fosse pegar um pedaco de um chocolate

#se eu quiser uma mini tupla, eu posso usar o conceito de slice e pegar um pedaco dessa tupla para formar a mini tupla
# 0       1        2      3
#('sono','comida','sol','sono')
#formato [de:ate-1]
#[1:3]
print('Slicing - criando uma tupla menor')
pequenaTupla = minhaTupla[1:3]
print(pequenaTupla)

#se fosse uma lista de um so elemento nos fariamos essa construcao
listadeUmElemento = ['um elemento']
print(listadeUmElemento)

tuplaUmElementoFalsiane = ('um elemento')
print(tuplaUmElementoFalsiane)
print(type(tuplaUmElementoFalsiane))

tuplaUmElemento = ('um elemento',)
print(tuplaUmElemento)
print(type(tuplaUmElemento))

#sera que eu consigo ordenar uma tupla?
#nao consigo dessa maneira, pois a caracteristica da tupla é ser imutavel e portanto nao faz sentido ter esse metodo
#minhaTupla.sort()
print('\n')
print(minhaTupla)
novaColecao = sorted(minhaTupla)
print(novaColecao)
print(type(novaColecao))
novaColecao = tuple(novaColecao)
print(type(novaColecao))

print(sorted(minhaTupla))

print('\n')
#em lista é bastante comum que a gente inicie uma lista vazia e vá acrescentando elementos
listaVazia = []
print(listaVazia)

#posso fazer o mesmo com tupla
minhaTuplaVazia = ()
print(minhaTuplaVazia)
#posso criar uma tupla vazia, mas como ela é imutavel, eu nao consigo acrescentar elementos, entao é inutil

print('\n')
#operadores aritmeticos com tuplas
#combinacao de tuplas atraves do operador +
meusBrinquedos = ('patins', 'skate', 'bola')
minhasNecessidades = minhaTupla + meusBrinquedos
print(meusBrinquedos)
print(minhasNecessidades)

#posso n-plicar os elementos criando uma nova tupla a partir da multiplicacao de elementos da tupla origina
muitosBrinquedos = meusBrinquedos * 5
print(muitosBrinquedos)

#se precisarmos acrescentar um elemento na tupla
#eu nao posso pq ela é imutavel
#mas eu posso transformar numa colecao que permite acrescentar elementos e depois de acrescentado, voltar para o tipo tupla
print('\n')
print(minhaTupla)
minhaTupla = list(minhaTupla)
minhaTupla.append('praia')
print(minhaTupla)
minhaTupla = tuple(minhaTupla)
print(minhaTupla)

#tupla é indexada
#localizar um elemento
if 'sol' in minhaTupla:
  print('tem sol')
  print('o sol mora na casa:',minhaTupla.index('sol'))

print(type(minhaTupla))

#nao ha como remover elementos de uma tupla, pq ela é imutavel
#racional, transformar em lista, usar as funcoes de lista
#append -> adiciona o elemento no final
#insert -> adiciona o elemento em uma determinada posicao
#pop sem indice -> remove do final
#pop com indice -> remove de uma determinada posicao
#remove(elemento) -> remove o determinado elemento
#del -> mesmo racional do poo
#sort ou sorted -> para ordenacao

print('Quantidade de elementos: ', len(minhaTupla))

#para apagar a tupla com um todo posso usar o del
del minhaTupla