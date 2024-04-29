from datetime import date
ano = int(input('Em que ano você nasceu? '))

b = ano % 4
if ano == 0:
    ano = date.today().year

if ano == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Você nasceu em um ano Bissexto!')
else:
    print('Você não nasceu em um ano Bissexto!')