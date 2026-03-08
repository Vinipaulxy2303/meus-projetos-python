import random

num=random.randint(0, 5)
escolha=int(input('me fale um numero entre 0 e 5:'))
if escolha==num:
    print('Parabens você acertou!!')
    print(num)
else:
    print('Não foi dessa vez!!')
    print(num)