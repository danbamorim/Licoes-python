necessita_de_contador = 0
necessita_de_limpeza1 = 0
necessita_de_limpeza2 = 0
necessita_de_limpeza3 = 0
necessita_de_limpeza4 = 0

indentificacao = int(input("Informe a indentificação: "))

while indentificacao != 0: 
    print("1 = necessita da esfera")
    print("2 = necessita da limpeza")
    print("3 = necessita da troca do cabo ou conector")
    print("4 = quebrado ou inutilizado")
    
    defeito = int(input("Digite o defeito: "))

    if defeito == 1: 
        necessita_de_limpeza1 = necessita_de_limpeza1 + 1 
    elif defeito == 2: 
        necessita_de_limpeza2 = necessita_de_limpeza2 + 1 
    elif defeito == 3: 
        necessita_de_limpeza3 = necessita_de_limpeza3 + 1 
    elif defeito == 4: 
        necessita_de_limpeza4 = necessita_de_limpeza4 + 1 
    necessita_de_contador = necessita_de_contador + 1 
indentificacao= int(input("Informe a indentificação: "))

perc_esfera = (necessita_de_limpeza1 * 100) / necessita_de_contador
perc_limpeza = (necessita_de_limpeza2 * 100) / necessita_de_contador
perc_cabo = (necessita_de_limpeza3 * 100) / necessita_de_contador
perc_quebrado= (necessita_de_limpeza4 * 100) / necessita_de_contador

print("Quantidade de mouse:{0} ".format(necessita_de_contador))
print("Situação:                 Quantidade                   Poncetual")
print("1 = necessita de esfera  {0}                            {1:.2.f}%".format(necessita_de_limpeza1,perc_esfera))
print("2 = necessita de esfera  {0}                            {1:.2.f}%".format(necessita_de_limpeza2,perc_limpeza))
print("3 = necessita de esfera  {0}                            {1:.2.f}%".format(necessita_de_limpeza3,perc_cabo))
print("4 = necessita de esfera  {0}                            {1:.2.f}%".format(necessita_de_limpeza4,perc_quebrado))
