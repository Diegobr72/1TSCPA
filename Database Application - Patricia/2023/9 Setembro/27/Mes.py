print("Programa que fala o número por extenso")
mes = int(input("Qual o número do mês que você está?"))

if 1 <= mes <= 12: 
  if mes == 1:
      mes_extenso = "Janeiro"
  elif mes == 2:
      mes_extenso = "Fevereiro"
  elif mes == 3:
      mes_extenso = "Março"
  elif mes == 4:
      mes_extenso = "Abril"
  elif mes == 5:
      mes_extenso = "Maio"
  elif mes == 6:
      mes_extenso = "Junho"
  elif mes == 7:
      mes_extenso = "Julho"
  elif mes == 8:
      mes_extenso = "Agosto"
  elif mes == 9:
      mes_extenso = "Setembro"
  elif mes == 10:
      mes_extenso = "Outubro"
  elif mes == 11:
      mes_extenso = "Novembro"
  elif mes == 12:
      mes_extenso = "Dezembro"

  print("Você está no mês", mes_extenso, "!")
else:
    print("Mês inválido")