# Implemente o programa que calcule o volume de um esfera de raio R. O usuário fornecerá o dado necessario.
# Onde   volume = 4/3pir^3
raio = float(input('Digite o valor do raio: '))
volume = (4/3) * 3.14 * raio ** 3
print('Arredondando o pi para 3,14, o volume de uma esfera de raio {} é igual à {:.2f}cm³.'.format(raio, volume))
