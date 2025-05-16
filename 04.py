# Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente.
# Os valores serão fornecidos pelo usuário.
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('Os números {} e {}, em ordem crescente, é {} e {}.'.format(n1, n2, n2, n1))
elif n2 > n1:
    print('Os números {} e {}, em ordem crescente, é {} e {}.'.format(n1, n2, n1, n2))
else:
    print('Os números {} e {} têm o mesmo valor.'.format(n1, n2))
