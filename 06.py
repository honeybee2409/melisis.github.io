num1 = int(input('Qual o primeiro número? '))
num2 = int(input('Qual o segundo número? '))
if num1 > num2:
    print('A ordem crescente dos números {} e {} é: {} e {}.'.format(num1, num2, num1, num2))
else:
    print('A ordem crescente dos números {} e {} é: {} e {}.'.format(num1, num2, num2, num1))
