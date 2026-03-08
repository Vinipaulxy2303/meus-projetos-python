RS=float(input('Quantos reais você tem: '))
URSS=RS/5.23
Euro=RS/6.10
Peso=RS*270.72
print('Você tem R${}\n Isso dá ${:0.2f}\n Isso tambem dá ¢{:0.2f}\n Isso dá {:0.2f} peso argentino'.format(RS,URSS,Euro,Peso))