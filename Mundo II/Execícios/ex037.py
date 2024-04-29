n = int(input('Insira um valor: '))
base = str(input('Qual será a base de conversão? '))

if base == '1':
    b = bin(n)[2:]
    print('O número {} em BINÁRIO é {}'.format(n, bin(n)))
elif base == '2':
    o = oct(n)[2:]
    print('O número {} em OCTAL é {}'.format(n, oct(n)))
elif base == '3':
    h = hex(n)[2:]
    print('O número {} em HEXADECIMAL é {}'.format(n, hex(n)))

