v = float(input('Qual era a velocidade no painel? '))
m = (v - 80) * 7

if v <= 80:
    print('Você não foi multado!')
else:
    print('Você foi multado em R${:.2f}'.format(m))