print("Progama para verificar qual seu síndico do condomínio")
CONDOMINIO = int(input("Digite qual o numero do seu condomínio: "))
if CONDOMINIO < 11:
    ADM = "José"
else:
    ADM = "Hamilton"
print("O administrador do se condomínio é",ADM,"!")
print("Em caso de duvidas estamos a disposição!")