s = float(input('Qual o salário do funcionário? R$'))

sma = s + 150
sme = s + 500

if s <= 1.250:
    print('O seu novo salário é de R${}'.format(sme))
else:
    print('O seu novo salário é de R${}'.format(sma))