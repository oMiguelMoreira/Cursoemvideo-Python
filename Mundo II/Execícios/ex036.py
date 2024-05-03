valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é a sua renda? R$'))
anos = int(input('Em quantos anos irá parcelar? '))

p = valor / (anos * 12)
if p > salario * 30/100:
    print('O seu empréstimo foi negado!')
    print('A prestação excedeu 30% de seu sálario!')
else:
    print('O valor da prestação mensal será de R${:.2f} por {} anos \nEmpréstimo Concedido '.format(p,anos))