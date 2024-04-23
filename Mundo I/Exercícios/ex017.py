import math
b = int(input('Valor do cateto oposto: '))
c = int(input('Valor do cateto adjacente: '))

a = pow(b,2) + pow(c,2)
raiz = math.sqrt(a)

print('O valor da hipotenusa é {:.2f}'.format(raiz))

