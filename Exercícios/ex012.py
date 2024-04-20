P = float(input('Qual o preço do produto? R$'))

np = P * (5/100)
nt = (P - np)


print('O produto com 5% de desconto é R${:.2f}'.format(nt))
