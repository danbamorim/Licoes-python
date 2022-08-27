e = 0 
m = 0
 
peso = float(input("informe seu peso : ")) 

if peso > 50: 
    e = peso - 50 
    m = e * 4
    print("Pagar:{0:.2f}".format(m))
else: 
    e = 0
    m = 0 
print("Multas : {0}".format(m)) 
print("Excesso: {0}".format(e))
