import random
num = random.randint(0, 5)

n = int(input('Qual é o número pensado? '))
if n == num:
    print('Parabéns! Você acertou.')
else:
    print('Não foi dessa vez!')