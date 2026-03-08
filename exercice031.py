distancia=int(input('Quantos Km vai ter essa viagem:  '))
if distancia<=200:
    print('A passagem vai custar R${}'.format(distancia*0.50))
else:
    print('A passagem vai custar R${}'.format(distancia*0.45))