quantidade = 0
soma = 0
maior_que_20 = 0
print('Digite [0] para sair)')
while True:
        valor = float(input('Digite um valor real: '))
        if valor == 0:
            break
        quantidade += 1
        soma += valor
        if valor > 20:
            maior_que_20 += 1
media = soma / quantidade
print('Quantidade de valores digitados:', quantidade)
print('Soma dos valores: {:.1f}'.format(soma))
print('Média aritmética: {:.1f}'.format(media))
print('Quantidade de valores maiores que 20:', maior_que_20)
