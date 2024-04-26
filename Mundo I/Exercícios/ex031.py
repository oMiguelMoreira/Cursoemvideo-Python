d = float(input('Qual é a distância total da sua viagem? '))

ma = d * 0.45
me = d * 0.50

if d >= 200:
    print('O preço da passagem é de R${:.2f}'.format(ma))
else:
    print('O preço da passagem é de R${:.2f}'.format(me))