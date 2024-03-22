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