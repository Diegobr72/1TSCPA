#Coleções
#Sao variáveis que armazenam mais de um valor
#elas podem ser de um mesmo tipo ou podem ser de tipos diferentes
#toda coleçõa é um elemento ITERAVEL (posso percorrer)

#A primeira coleão que vamos ver é a LISTA
#É A MAIS PODEROSA e FLEXIVEL das coleções
#permitindo varias operacoes
#Caracteristicas
#mutaveis, expansiveis, ordenadas, permitem duplicados,
#acomodam diferentes tipos de dados, são acessadas por indices

print('Listas\n')
minhaLista = ['cafe', 'acucar','agua']
print(minhaLista)
                #0      #1      #2    #3      #4
minhaLista = ['cafe', 'acucar','agua','cafe','cafe']
print(minhaLista)

print('Criando listas a partir de outra lista')
                #zero:até-1

#Slicing
pequenaLista = minhaLista[0:2]
print(pequenaLista)

print('Acessando Elementos')
print('Elemento 0:', minhaLista[0])
print('Elemento 3:', minhaLista[3])

print('Substituindo Elementos')
    #0      #1      #2    #3      #4
    #-5     #-4      #-3    #-2      #-1
#['cafe', 'acucar','agua','cafe','cafe']
print('antes', minhaLista)
minhaLista[3:4+1] = ['canela', 'chantilly']
print('depois', minhaLista)
print('primeiro elemento do lado positivo', minhaLista[0])
print('primeiro elemento do lado negativo', minhaLista[-5])

print('ultimo elemento do lado positivo', minhaLista[4])
print('ultimo elemento do lado negativo', minhaLista[-1])

print('Slicing')
  #-5     #-4      #-3      #-2      #-1
  #0      #1      #2        #3      #4
#['cafe', 'acucar','agua','canela', 'chantilly']
print('Parte da lista:', minhaLista[1:2])
print('Parte da lista:', minhaLista[1:3])
print('Parte da lista:', minhaLista[-4:-2+1])
              # 0123
minhaPalavra = 'Lais'
print('Parte da Lais', minhaPalavra[1:2+1])

print('Acrescentar um elemento no final da lista')
minhaLista.append('baunilha')
print(minhaLista)
print('Acrescentar um elemento numa determinada posicao')
minhaLista.insert(3, 'nibs de cacau')
print(minhaLista)

print('Removendo elementos')
#['cafe', 'acucar', 'agua', 'nibs de cacau', 'canela', 'chantilly', 'baunilha']
print('Elimando o ultimo')
minhaLista.pop()
print(minhaLista)
print('Elimando um item especifico - nibs de cacau no indice 3')
minhaLista.pop(3)
print(minhaLista)
del minhaLista[-1]
print(minhaLista)
print('Elimando um item atraves do seu nome')
minhaLista.remove('canela')
print(minhaLista)

# minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
# print(minhaLista)
# minhaLista.remove('cafe')
# print(minhaLista)


print('Removendo TODOS elementos de uma lista')
minhaLista.clear()
print(minhaLista)

del minhaLista
print('Apagou minhaLista')
#print(minhaLista)

#Construtores
print('Outra Lista')
outraLista = []
print(outraLista)
outraLista = list(('chantilly', 'baunilha'))
print(outraLista)


print('Extendendo uma lista')
minhaLista = ['cafe', 'acucar','agua']
print(minhaLista)
minhaLista.extend(outraLista)
print(minhaLista)

print('Criando uma lista a partir de dua outras')
pequenosMimos=['raspas de limao', 'flor de sal']
minhaListaComplementos = outraLista + pequenosMimos
print('outra lista', outraLista)
print('pequenos mimos', pequenosMimos)
print('minha lista complementos', minhaListaComplementos)

print('Achar um item dentro da lista')
print('Descobrindo a localizacao')
onde = minhaLista.index('acucar')
print(minhaLista)
print('Onde esta o acucar', onde)

print('Localizacao com elementos repetidos na lista')
minhaLista = ['cafe', 'acucar', 'agua', 'cafe', 'cafe']
print(minhaLista)
onde = minhaLista.index('cafe')
print('Ele mostra onde esta a primeira ocorrencia do elemento')
print('Onde esta o cafe', onde)

if 'chantilly' in minhaLista:
  print('tem Chantilly')

print('percorrendo toda a lista e imprimindo os elementos um a um')
for elemento in minhaLista:
  print(elemento)

print('Ordenar')
print(minhaLista)
minhaLista.sort()
print(minhaLista)
#atencao - soh consigo ordernar listas com elementos do mesmo tipo
listaNAOOrdenavel = [3, 1, 'Patricia', 98, 'Antonia']
print(listaNAOOrdenavel)
# listaNAOOrdenavel.sort()
# print(listaNAOOrdenavel)
                #zero:até-1