## Área destinada a locação das atividades de Python da faculdades passadas pelo Professor Antonio Barbosa
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 == r2 == r3:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segmentos acima podem formar um triângulo equilátero.')
    else:
        print('Os segmentos acima não podem formar um triângulo.')
elif r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segmentos acima podem formar um triângulo isósceles.')
    else:
        print('Os segmentos acima não podem formar um triângulo.')
elif r1 != r2 != r3:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segmentos acima podem formar um triângulo escaleno.')
    else:
        print('Os segmentos acima não podem formar um triângulo.')
