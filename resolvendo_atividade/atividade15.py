poluicao=float(input("Informe o indice de poluição: "))

if poluicao >= 0.3 and poluicao < 0.4 : 
    print("Grupo 1 suspender atividades")
elif poluicao >= 0.4 and poluicao < 0.5 :  
    print("Grupo 1 e grupo 2 suspender atividades")
elif poluicao >= 0.5 : 
    print("Todos os grupos suspender atividades")
else : 
    print("Niveis aceitaveis")