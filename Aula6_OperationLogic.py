renda_minima_5000 = True
status_name= True


if renda_minima_5000 == True and status_name == True:
    print('Financiamento aprovado!')
elif renda_minima_5000 == True & status_name == False:
    print ('Financiamento negado!')
    print('Motivo : Nome negativado ')
elif renda_minima_5000 == False & status_name == True :
    print('Finaciamento negado !')
    print('Motivo : Renda mininam não atingida')    
else:
    print ('Financiamento reprovado!')
