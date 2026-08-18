i=0
def nota():
    nome=str(input('Qual o teu nome: '))
    nota1=float(input("Qual foi a sua primeira nota: "))
    nota2=float(input("Qual foi a sua segunda nota: "))
    result=(nota1+nota2)/2
    print(result)
    return(nota1, nota2, nome, result)
for i in range(4):
    nota()
    if 