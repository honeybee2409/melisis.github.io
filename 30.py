def valor_absoluto(numero):
    if numero < 0:
        return numero * -1
    else:
        return numero

if __name__ == '__main__':
    valor = float(input("Digite um número: "))
    resultado = valor_absoluto(valor)
    print("O valor absoluto é: {}".format(resultado))
