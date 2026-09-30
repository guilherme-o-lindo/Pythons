import random

alunos = []

for i in range(4):
    aluno = input(f'Digite o nome do {i+1}º aluno: ')
    alunos.append(aluno)

alunoEscolhido = random.choice(alunos)

random.shuffle(alunos)

print(f"O aluno escolhido foi {alunoEscolhido} e a ordem de apresentação será {', '.join(alunos)}")