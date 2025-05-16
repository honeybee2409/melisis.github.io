valor1 = float(input('Digite o primeiro valor: '))
oper = input('Digite a operação que deseja (+ - * /): ')
valor2 = float(input('Digite o segundo valor: '))
if oper == '+':
    soma = valor1 + valor2
    print('A soma é', soma)
elif oper == '-':
    sub = valor1 - valor2
    print('A subtração é', sub)
elif oper == '*':
    mult = valor1 * valor2
    print('A multiplicação é', mult)
elif oper == '/':
    divi = valor1 / valor2
    print('A divisão é', divi)
