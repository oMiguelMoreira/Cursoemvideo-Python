import math # biblioteca math
#ceil - arredonda para cima
#floor - arredonda para baixo
#trunc - arredonda para o número inteiro mais próximo
#pow - potência
#sqrt - raiz quadrada
#factorial - fatorial
#quero usar so um comando - from math import ceil, floor

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))
