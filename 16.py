ct = 0
soma = 0
print('Dobro dos números naturais na vertical')
for num in range(2, 11, 2):
    print(num)
    ct = ct + 1
    soma = soma + num
media = soma / ct
print('Soma: {}'.format(soma))
print('Média: {}'.format(media))
print('Encerrou o programa')
