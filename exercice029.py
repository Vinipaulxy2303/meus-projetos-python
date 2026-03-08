velocidade=int(input('Qual a velocidade que o carro passou: '))
if velocidade < 80:
    print('Você não foi mulatdo, parabens!!!')
else:
    print('vc foi multado, e tera que pagar R${}'.format((velocidade-80)*7.00))