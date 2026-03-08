num=int(input('me de um numero:'))
m=num//1000%10
c=num//100%10
d=num//10%10
u=num %10
print('Você me deu o numero {} \n E esse é os valores \n Milhar {} \n Centena {} \n Dezena {} \n unidade {} '.format(num, m, c, d, u))