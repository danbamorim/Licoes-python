numero=int(input("Informe o valor: "))

while numero < 1 or numero > 10: 
    numero=int(input("Informe o valor: "))
print("Tabuada de {0}".format(numero))
for i in range(1,11):
    print("{0} x {1} = {2}".format(numero,i,(numero * i)))