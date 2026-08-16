def calculadora():
    n1=0
    n2=0
    result=0
# 1 Para editar salve localmente ctrl+S
# 2 Abra o terminal 
# 3 e no terminal escreva (1. git add . , 2. git commit 'Descreva oque vc mudou', 3. git push )
    print('Olá, você quer fazer qual conta agora? ')
    conta=input('Qual a conta vc deseja fazer +, -, /, *, **  ? ')
    if conta == '+':
        n1=int(input('Qual é o numero desejado ? '))
        n2=int(input('Qual é o numero você quer somar ? '))
        result=n1+n2
        print(f'O resultado da conta é {result}')
    elif conta == '-':
        n1=int(input('Qual é o numero desejado ? '))
        n2=int(input('Qual o numero você quer subtrarir ? '))
        result=n1-n2
        if result == 0:
            print('Error')
        else:
            print(f'O resultado da conta é {result}')
    elif conta == '/':
        n1=int(input('Qual é o numero desejado ? '))
        n2=int(input('Qual é o numero para ser dividido ? '))
        result=n1/n2
        print(result)
    elif conta == '*':
        n1=int(input('Qual é o numero desejado ? '))
        n2=int(input('Qual é o  numero desejado para multiplicar ? '))
        result=n1*n2
        print(result)
    else:
        n1=float(input('Qual numero desejado ? lembrendo que pode fazer raiz quadrada , quadrado , ao cubo etc....'))
        n2=float(input('Qual é o numero desejado ? '))
        result=n1**n2
        print(result)
    return(result , n1 , n2)

calculadora()