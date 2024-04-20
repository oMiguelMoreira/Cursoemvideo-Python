dia = int(input('Quantos dias ficou com o carro? '))
r = float(input('Quantos KM rodados? '))

t = dia * 60 + r * 0.15

print('Você ficou com o carro por {} dias e andou {:.1f}Km. \nO custo total do aluguel é de R${:.2f}.'.format(dia, r, t))
