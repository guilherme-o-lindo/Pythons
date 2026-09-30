from random import randint

numEscolhido = randint(0, 5)
numUsuario = int(input('Adivinhe o número entre 0 e 5 que estou pensando: '))

while numUsuario != numEscolhido:
    print('Que pena, você errou. Tente novamente.')
    numUsuario = int(input('Digite outro número: '))

print(f'Você acertou! Eu estava pensando no {numEscolhido}')