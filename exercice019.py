import random
nomes=input('me de o nome dos alunos: ').title()
listas_nomes=nomes.split(',')
print('O aluno que vai apagar o quadro é {}'.format(random.choice(listas_nomes)))