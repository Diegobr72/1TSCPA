print('Campanha de Vacinacao da Puppy Bel')
resp = input('Ha animais a serem vacinados?').lower()
ng, nc, n = 0, 0, 0
#while resp == 's' or resp =='sim' or resp =='yes':
while resp in ('s','y','sim','yes'):
  #n = n + 1
  n += 1
  especie = input('Qual especie de animal sera cadastrado? ')
  if especie in ('gato', 'cat'):
    ng += 1
  elif especie in ('cao', 'cachorro', 'dog'):
    nc += 1
  else:
    print('Animal invalido')
  for i in range(1,4,1):
    print(f'Vacina {i} OK')
  resp = input('Ha animais a serem vacinados?').lower()
print(f'Total de gatos vacinados:{ng}')
print(f'Total de cachorros vacinados:{nc}')
print(f'Total de animais vacinados:{n}')


#Assuntos diversos
#pulos do range
for i in range(1,41,5):
  #print(f'Vacina {i} OK')
  print('Vacina', i, 'OK')
