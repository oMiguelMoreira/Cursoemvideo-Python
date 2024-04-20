r = float(input('Qual o valor em reais? '))

dolar = r / 5.20
euro = r / 5.53
libra = r / 6.42

print('Com R${:.2f} você pode comprar US${:.2f} \nCom R${:.2f} você pode comprar €{:.2f}'.format(r, dolar, r, euro))
print('Com R${:.2f} você pode comprar £{:.2f}'.format(r, libra))
