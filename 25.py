def mostrar_mensagem(mensagem, numero):
    print("Mensagem: {}".format(mensagem))
    print("Número: {}".format(numero))
if __name__ == '__main__':
    mensagem = input("Digite a mensagem: ")
    numero = int(input("Digite o número: "))
    mostrar_mensagem(mensagem, numero)
