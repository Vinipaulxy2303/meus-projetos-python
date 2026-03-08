nome=str(input('Digite seu nome completo:')).title()
minu=nome.lower()
mais=nome.upper()
quan=len(nome)
xespaco=len(nome.split(' '))
total=quan-xespaco+1
primeiro=nome.split()[0]
leia=len(primeiro)
print('Você me deu o seu nome que é {} \n e esse é seu nome minusculo {} \n e o seu nome no maisculo é {} \n ele no total tem {} caracteres \n e o seu primeiro nome tem {} caracteres'.format(nome,minu,mais,total,leia))