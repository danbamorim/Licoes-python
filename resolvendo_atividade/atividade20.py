maior = -999
menor = 999
soma = 0 

for i in range(1,11): 
    valor = int(input("Informe o valor: "))
if valor > 0 :
    maior = valor
if valor < menor : 
    menor = valor 
    soma = soma + valor
else : 
    valor = int(input("Informe o valor: "))
media =  soma / 10
print("Maior:{0}".format(maior))
print("Menor:{0}".format(menor))
print("Média:{0}".format(media))

