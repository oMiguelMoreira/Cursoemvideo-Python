frase = str(input('Digite algo: ').upper()).strip()

print('A letra A apareceu {} vezes'.format( frase.count('A')))
print('A primeira vez q aparece é na posição de {}°'.format(frase.find('A')+1))
print('A ultima vez que aparece é na posição de {}°'.format(frase.rfind('A')+1))
