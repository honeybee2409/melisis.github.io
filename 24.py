numero = int(input('Digite um número inteiro para ver a sua tabuada: '))
print('Tabuada de {}:'.format(numero))
print('')
for i in range(1, 11, 1):
    print('{} x {} = {}'.format(i, numero, i * numero))
