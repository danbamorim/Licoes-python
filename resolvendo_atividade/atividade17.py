maior = 0 
numero = int(input("Informe um número:  "))

while numero != 0: 
    if numero > maior:
     maior = numero
    numero= int(input("Informe um numero: "))
print("Maior valor:{0} ".format(maior))