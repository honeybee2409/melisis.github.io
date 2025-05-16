def maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False

if __name__ == '__main__':
    pessoa = int(input("Digite a idade da pessoa: "))
    if maioridade(pessoa):
        print("A pessoa é maior de idade.")
    else:
        print("A pessoa é menor de idade.")
