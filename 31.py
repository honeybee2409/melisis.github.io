def somar(a, b):
    resultado = a + b
    print("Resultado da soma: {}".format(resultado))
def subtrair(a, b):
    resultado = a - b
    print("Resultado da subtração: {}".format(resultado))
def multiplicar(a, b):
    resultado = a * b
    print("Resultado da multiplicação: {}".format(resultado))
def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        resultado = a / b
        print("Resultado da divisão: {}".format(resultado))

if __name__ == '__main__':
    operador = input("Digite a operação desejada (+, -, x, /): ")
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    if operador == '+':
        somar(valor1, valor2)
    elif operador == '-':
        subtrair(valor1, valor2)
    elif operador == 'x' or operador == 'X':
        multiplicar(valor1, valor2)
    elif operador == '/':
        dividir(valor1, valor2)
    else:
        print("Operador inválido.")
