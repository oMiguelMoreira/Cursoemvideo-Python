from math import sin, cos, tan, radians
angulo = int(input('Digite o valor de um ângulo: '))

r = radians(angulo)
s = sin(r)
c = cos(r)
t = tan(r)

print('O Seno de {}° é {:.2f} \nO Cosseno de {}° é {:.2f} \nA Tangente de {}° é {:.2f}'.format(angulo, s, angulo, c, angulo, t))
