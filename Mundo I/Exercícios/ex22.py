pnome = str(input('Qual o seu nome? '))
snome = str(input('Quais são seus sobrenomes? '))
nomec = pnome + snome

print(nomec.upper())
print(nomec.lower())
print(nomec.strip(), '\ncontém ao todo {} letras'.format(len(nomec)))
print('O primeiro nome contém {} caractéres'.format(len(pnome)))


