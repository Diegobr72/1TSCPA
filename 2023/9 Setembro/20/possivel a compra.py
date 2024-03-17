print("Progama para verificar se possivel a compra ")
preco = float(input("Digite qual o valor do produto? "))
dinheiro = float(input("Qual o valor que você possui? "))
if preco <= dinheiro:
    dinheiro= dinheiro - preco
    print("você comprou o produto, e agora tem", dinheiro,"!")
else:
    print("você não tem valor sufiencte para compra o produto")