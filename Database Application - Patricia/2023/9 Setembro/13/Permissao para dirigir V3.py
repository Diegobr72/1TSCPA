#versao 3: com desvio condicional simples e operadores logicos

print("Permissao para dirigir")

idade = int(input("Qual sua idade? "))
cnh = input("Você possui CNH? ")
if idade >= 18 and cnh == 'sim':
  print("Voce pode dirigir")
print("Obrigada por participar")