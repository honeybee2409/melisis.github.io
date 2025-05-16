h = float(input('Qual sua altura? '))
genero = input('Qual seu gênero (digite H ou M): ')
if genero == 'h':
    pih = (72.7 * h) - 58
    print('O seu peso ideal, sendo homem com a altura de {}cm, é {:.1f}kg'.format(h, pih))
else:
    pim = (62.1 * h) - 44.7
    print("O seu peso ideal, sendo mulher e com a altura de {}cm, é {:.1f}kg".format(h, pim))
