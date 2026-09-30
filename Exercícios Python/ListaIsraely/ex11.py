qntdTermos = int(input('Digite a quantidade de termos da Sequência de Fibonacci desejada: \n'))

sequenciaFibonacci = [0, 1]

for i in range(qntdTermos - 2):
    sequenciaFibonacci.append(
        sequenciaFibonacci[-1] + sequenciaFibonacci[-2]
        )

print(sequenciaFibonacci)