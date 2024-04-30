p = float(input('Qual o seu peso? '))
a = float(input('Qual a sua altura? '))

altura = a / 100
imc = p / pow(a,2)

if imc < 18.5:
    print('Você está a baixo do peso! Seu IMC é de: {:.6f}kg/m²'.format(imc))
elif 18.5 < imc < 25:
    print('Você está no peso ideal! Seu IMC é de {:.6f}kg/m²'.format(imc))
elif 25 < imc < 30:
    print('Você está com sobrepeso! Seu IMC é de {:.6f}kg/m²'.format(imc))
elif 30 < imc < 40:
    print('Você está Obeso! O seu IMC é de {:.6f}kg/m²'.format(imc))
elif imc > 40:
    print('Você está com Obesidade Mórbia! O seu IMC é de {:.6f}kg/m²'.format(imc))