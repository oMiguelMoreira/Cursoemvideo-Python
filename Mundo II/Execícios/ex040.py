n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print('REPROVADO!')
elif m < 6.9 or m > 5.0:
    print('EM RECUPERAÇÃO!')
elif m >= 7.0:
    print('APROVADO!')