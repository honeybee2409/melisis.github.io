# Construa o programa que calcule o peso ideal de uma pessoa. Utilize as seguintes fórmulas
# Se homem, o peso ideal é calculado assim: (72,7 x altura) - 58;
# Se mulher, o peso ideal é calculado assim: (62,1 x altura) - 44,7
h = float(input('Qual sua altura? '))
genero = input('Qual seu gênero (digite H ou M): ')
if genero == 'h':
    pih = (72.7 * h) - 58
    print('O seu peso ideal, sendo homem com a altura de {}cm, é {:.1f}kg'.format(h, pih))
else:
    pim = (62.1 * h) - 44.7
    print("O seu peso ideal, sendo mulher e com a altura de {}cm, é {:.1f}kg".format(h, pim))
