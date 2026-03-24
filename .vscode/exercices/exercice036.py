valor_casa=int(input('Qual o valor da casa? R$ '))
salario=float(input('Qual é seu salario? R$ '))
tempo=int(input('Quantos anos você vai financiar?'))
p=valor_casa/(tempo*12)
maximo=salario*0.30
if p <= maximo:
    print('O emprestimo foi aprovado!')
else:
    print('O emprestimo foi negado!')