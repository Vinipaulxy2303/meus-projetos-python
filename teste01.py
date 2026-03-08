name=str(input('Qual vai ser seu nome:')).title()
sim=1
nao=0
d=3 #direita
e=4 #esquerda
n=5 #meio
print('olá {}, tudo bem!! vamos começar o jogo?'.format(name))
comecar=str(input('então? '))
if comecar == 'sim':
    print('Então vamos começar!!!!')
    print('carregando......')
    f1=str(input('qual lado você vai escolher ? direita ou esquerda!!!'))
    if f1=='d':
        print('Você morreu!!!')
    else:
         print('Você sobreviveu!!!!')
         print('Agora apareceu mais dois caminhos!!! ')
         f2=str(input('Qual você vai escolher? direita ou esquerda...'))
         if f2=='e':
             print('Você sobreviveu!!!')
             print('Agora chegamos na fase final!!!')
             f3=str(input('Qual dos caminhos você vai ?direita, meio ou esquerda'))
             if f3=='d':
                 print('Você ganhou!!!')
             else:
                 print('perdeu!!!')
         else:
             print('Você morreu!!!')



else:
    print('TCHAU!!!')