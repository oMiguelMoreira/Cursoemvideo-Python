from datetime import date
atual = date.today().year
ano = int(input('Qual o ano de nascimento? '))
idade = atual - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Categoria Mirim.')
elif idade <= 14:
    print('Categoria Infantil.')
elif idade <= 19:
    print('Categoria Junior.')
elif idade <= 25:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')
