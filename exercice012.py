preco=float(input('me de o preço do produto: '))
desconto=preco*(5/100)
precot=preco-desconto
print('o desconto vai de R${} para R${:0.2f}'.format(preco,precot))