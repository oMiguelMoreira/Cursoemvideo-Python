n = int(input('Digite um número: '))
p = n % 2
if p == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar'.format(n))