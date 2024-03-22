#Slicing em textos
#O slicing segue o padrao de corte segundo um indice
#nos podemos usar o slicing em textos, ja que um texto é um elemento iteravel
#padrao [de:ate:passos]

frase = 'trabalhando com texto'
palavra = frase[0:11]
print(palavra)

palavras = frase[12:]
print(palavras)

palavras = frase[::2]
print(palavras)

print(len(frase))
palavras = frase[-10::]
print(palavras)

frase_inversa = frase[::-1]
print(frase_inversa)

palavras = frase[:9:-1]
print(palavras)

palavras = frase[-1::-1]
print(palavras)