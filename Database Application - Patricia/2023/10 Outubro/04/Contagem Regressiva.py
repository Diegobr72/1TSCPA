#Escreva um algoritmo que simule uma contagem regressiva de 60 segundos.

import time
titulo = 'Contagem Regressiva'
print(f'{titulo:^60}')

for i in range(60, 0-1, -1):
  print(i)
  time.sleep(1)
print("Boooommm")