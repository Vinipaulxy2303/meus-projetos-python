import random
n1=str(input('Me de um nome:'))
n2=str(input('me de outro nome:'))
n3=str(input('me de outro nome: '))
n4=str(input('me de mais um nome'))
lista=[n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem de apresentação é')
print(lista)