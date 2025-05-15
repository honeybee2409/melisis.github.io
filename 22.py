soma = 0
for i in range(1, 501, 1):
    print(i)
    if i % 2 != 0 and i % 3 == 0:
        soma = soma + i
print()
print("Soma dos números ímpares e múltiplos de 3 de 1 a 500:", soma)
