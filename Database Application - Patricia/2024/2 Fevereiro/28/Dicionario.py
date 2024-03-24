#Dicionario
#colecoes do tipo chave:valor
#dica: para cada colecao tem um tipo de arquivo correspondente - no caso do dicionario, ele é totalmente aderente ao formato JSON
#Formulario
#Mutavel
#Exemplo
#Nome: Patricia
#Sexo: Feminino
#Idade: 54
#Chaves (Nome, Sexo, Idade)
#Valores (Patricia, Feminino, 54)

print('Colecao - Dicionario')
meuDicionario = {'nome':'Patricia','sexo':'feminino','idade':54}
print(meuDicionario)

meuDicionario = {'nome':'Patricia','sexo':'feminino','idade':'54', 'vacina_covid': True}
print(meuDicionario)

print('\nRecuperar um valor')
meuValor = meuDicionario['idade']
print(meuValor)
meuValor = meuDicionario.get('sexo')
print(meuValor)

outroDicionario = {'nome':'Patricia','sexo':'feminino',54:'idade', 'vacina_covid': True}
meuValor = outroDicionario[54]
print(meuValor)

print('\nRecuperar todos os valores de uma vez')
meusValores=meuDicionario.values()
print(meusValores)

print('\nRecuperar todos as chaves de uma vez')
minhasChaves=meuDicionario.keys()
print(minhasChaves)

print('\nRecuperar todos items de uma vez')
meusItens=meuDicionario.items()
print(meusItens)

print('\nRecuperando os itens VARRENDO a colecao')
print(meuDicionario)
#ATENCAO: se eu percorro os dicionarios, sem especificar nada, ele assume que eu estou percorrendo as chaves
print('\nVarrendo as chaves')
for chave in meuDicionario:
  print('Chave:', chave)
print('\n')
for chave in meuDicionario.keys():
  print('Chave:', chave)

print('\nVarrendo os valores')
for valor in meuDicionario.values():
  print('Valor:', valor)

print('\nVarrendo os itens')
for item in meuDicionario.items():
  print('Item:', item)

print('\nOutras maneiras de recuperacao')
print('\nRecuperando os valores atraves da chave')
for chave in meuDicionario:
  print('valor:', meuDicionario[chave])

print('\nRecuperando os itens separadamente')
for chave, valor in meuDicionario.items():
  print(f'chave:{chave}, valor:{valor}')

print('\nAdicionando Itens no dicionario')
meuDicionario['tipo sanguineo']='ORh-'
print(meuDicionario)

print('\nAlterando valores  no dicionario')
meuDicionario['idade']='53'
print(meuDicionario)

print('\nAlterando valores  no dicionario com update')
meuDicionario.update({'nome':'Patricia Maura'})
print(meuDicionario)

print('\nCriando itens  no dicionario com update')
#o update quando ele nao acha determinada chave, ele cria a chave e atribui o valor
meuDicionario.update({'estado civil':'casada'})
print(meuDicionario)

print('\nEliminando Itens')
del meuDicionario['tipo sanguineo']
print(meuDicionario)

print('\nEliminando Itens atraves do popitem - nao usa indice')
meuDicionario.popitem()
print(meuDicionario)

print('\nEliminando Itens atraves do pop, escolhendo o item que eu quero eliminar')
meuDicionario.pop('idade')
print(meuDicionario)

print('\nEliminando todos os items, dicionario vazio')
meuDicionario.clear()
print(meuDicionario)

del meuDicionario

dicVazio = {}
print(dicVazio)

meuDicionario = {'nome': 'Patricia Maura', 'sexo': 'feminino', 'idade': '53', 'vacina_covid': True, 'tipo sanguineo': 'ORh-', 'estado civil': 'casada'}
print('\nLocalizando itens')
print('Se existe uma determinada chave')
if 'tipo sanguineo' in meuDicionario:
  print('tem a chave tipo sanguineo')

if 'Patricia Maura' in meuDicionario.values():
  print('tem Patricia Maura nos valores')

#Aqui quando eu igualo os dicionarios, eu apenas estou apontando variaveis diferentes (novoDicionario e meuDicionario) para o mesmo lugar da memoria
novoDicionario = meuDicionario
print(novoDicionario)

#trocando a idade no dicionario original
meuDicionario['idade']=7
print('\nMeu Dicionario')
print(meuDicionario)

print('NOVO Dicionario')
print(novoDicionario)
#aqui quando eu troco o valor no dicionario original, automaticamente, eu também estou trocando o valor na variavel que esta apontando para a mesma area de memoria


#E como eu faço para criar realmente dois dicionarios "SEPARADOS, INDEPENDENTES"
print('\nDicionarios INDEPENDENTES')
copiaDicionario = meuDicionario.copy()
meuDicionario['nome']='Patricia M Angelini'
print('\nMeuDicionario - alterado')
print(meuDicionario)
print('\nCopia Dicionario')
print(copiaDicionario)

#CONCLUSAO o operador igual (=) nao serve para copiar dicionarios, é necessario utilizar o metodo .copy()