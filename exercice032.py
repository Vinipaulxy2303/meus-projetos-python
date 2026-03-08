ano=int(input('Qual ano você quer saber: '))
if (ano%4 ==0 and ano%100 !=0) or ano%400 ==00:
    print('esse ano é bissexto!!')
else:
    print('Esse ano é normal')