aprovados = 0
reprovados = 0
total_alunos = 0
print('Digite [0]para sair')
while True:
        nota = float(input('Digite a nota do aluno: '))
        if nota == 0:
            break
        total_alunos += 1
        if nota >= 5:
            aprovados += 1
        else:
            reprovados += 1
print('Quantidade de alunos aprovados:', aprovados)
print('Quantidade de alunos reprovados:', reprovados)
print('Quantidade total de alunos que fizeram a prova:', total_alunos)
