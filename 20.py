inicio = int(float(input("Digite o valor inicial em Fahrenheit: ")))
fim = int(float(input("Digite o valor final em Fahrenheit: ")))
passo = 1 \
if inicio <= fim \
else -1
print(f'   {'Fahrenheit':>10} | {'Celsius':>7}')
for f in range(inicio, fim + passo, passo):
    c = 5 * (f - 32) / 9
    print(f"{f:10.1f} ºF | {c:7.3f} ºC")