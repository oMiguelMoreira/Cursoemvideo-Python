print('{:=^40}'.format('CHIQUINHO AUTO PEÇAS'))
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = p - (p * 10/ 100)
elif opção == 2:
    total = p - (p * 5 / 100)
elif opção == 3:
    total = p
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = p + (p * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA  de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2F} no final.'.format(p, total))

