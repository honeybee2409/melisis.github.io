ct = 0
num = int(input('Digite o número inicial da sequência: '))
for i in range(num, -1, -1):
    print(i)
    ct = ct + 1
print('Quantidade de valores gerados: {}'.format(ct))
