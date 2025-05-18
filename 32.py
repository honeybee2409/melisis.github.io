def fatorial(n):
    resultado = 1
    for i in range(1, n + 1, 1):
        resultado *= i
    return resultado

if __name__ == '__main__':
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    if numero < 0:
        print("Fatorial não definido para números negativos.")
    else:
        resulta = fatorial(numero)
        print("O fatorial de {} é: {}".format(numero, resulta))
