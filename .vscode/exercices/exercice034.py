salario=float(input('Qual seu salario: '))
if salario>1250.00:
    print('O seu salario vai ser {}'.format(salario+(salario*10/100)))
else:
    print('O seu salario com aumento vai ser {}'.format(salario+(salario*15/100)))