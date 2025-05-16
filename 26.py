from datetime import datetime
def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
if __name__ == '__main__':
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = calcula_idade(ano_nascimento)
    print("A idade da pessoa é: {} anos.".format(idade))
