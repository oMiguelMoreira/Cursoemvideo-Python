n = int(input('Insira um valor: '))

print('''
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

base = int(input('Qual será a base de conversão? '))

if base == 1:
    print('O número {} em BINÁRIO é {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('O número {} em OCTAL é {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('O número {} em HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!')

