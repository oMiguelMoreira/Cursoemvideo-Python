n = input('Digite algo: ')
print('Qual é o tipo primitivo? ', type(n))
print('É um número: ', n.isnumeric())
print('É uma letra: ', n.isalpha())
print('É um alphanumerico:', n.isalnum())
print('Contém espaço? ', n.isspace())
print('Está em maiúsculo? ', n.isupper())
print('Está em minusculo? ', n.islower())
print('Esta dentro do padrão? ', n.isascii())
print('Está capitalizada? ',n.istitle())


