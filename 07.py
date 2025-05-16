valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
if valor1 > valor2 > valor3:
    print('O valor {} é maior que os valores {} e {}.'.format(valor1, valor2, valor3))
elif valor2 > valor1 > valor3:
    print('O valor {} é maior que os valores {} e {}.'.format(valor2, valor1, valor3))
else:
    print('O valor {} é maior que os valores {} e {}.'.format(valor3, valor1, valor2))
