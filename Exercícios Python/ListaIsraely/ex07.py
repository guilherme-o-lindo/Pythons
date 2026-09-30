num = int(input('Digite um número para saber sua tabuada (soma, subtração, multiplicação e divisão): \n'))

operacoes = {
    'soma': [], 
    'subtração': [], 
    'multiplicação': [], 
    'divisão': []}

for i in range(1, 11):
    operacoes['soma'].append(num + i)
    
    operacoes['subtração'].append(num - i)

    operacoes['multiplicação'].append(num * i)

    operacoes['divisão'].append(round(num / i, 2))

for operacao, valores in operacoes.items():
    print(f'A tabuada da {operacao} do número {num} é: {valores}')