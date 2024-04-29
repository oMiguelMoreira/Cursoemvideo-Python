ano = int(input('Qual o ano de nascimento? '))
atual = 2024

idade = atual - ano

if idade < 9:
    print('Categoria Mirim.')
elif idade < 14:
    print('Categoria Infantil.')
elif idade < 19:
    print('Categoria Junior.')
elif idade > 20:
    print('Categoria Master.')
