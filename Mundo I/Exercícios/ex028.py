from random import randint
from time import sleep
num = randint(0, 5)

n = int(input('Qual é o número pensado? '))
print('PROCESSANDO...')
sleep(3)
if n == num:
    print('Parabéns! Você me venceu!.')
else:
    print('Não foi dessa vez! Pensei no número {} e não no {}'.format(num, n))
