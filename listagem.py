i=0
def nota():
    nome=str(input('Qual o teu nome: '))
    nota1=float(input("Qual foi a sua primeira nota: "))
    nota2=float(input("Qual foi a sua segunda nota: "))
    result=(nota1+nota2)/2
    ficha=(f"Nome:{nome} , Np1={nota1}, Np2={nota2}, Media final={result}")
    print(ficha)
    return(ficha) 
podio=[]
for i in range(3):
    podio.append(nota())
    x=podio[0]
    z=podio[1]
    y=podio[2]
    if x<z and x<y:
        print(x)
    elif z>x and z>y:
        print(z)
    else:
        print(y)

    