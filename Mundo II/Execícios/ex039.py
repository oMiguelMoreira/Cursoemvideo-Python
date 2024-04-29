ano = int(input('Qual o seu ano de nascimento? '))
atual = 2024

idade = atual - ano
idade_alistar = 18

if idade < idade_alistar:
    falta = idade_alistar - idade
    print('Você ainda se alistará!')
    print('Faltam {} anos para se alistar!'.format(falta))
elif idade == idade_alistar:
    print('Está na hora de se alistar!')
    print('Falta 0 anos para se alistar!')
else:
    passou = idade - idade_alistar
    print('O tempo para se alistar passou!')
    print('Você está atrasado em {} anos'.format(passou))