nome = input('Digite seu nome completo: ').strip()

nomeMaisculo = nome.upper()
nomeMinusculo = nome.lower()
qntdLetras = len(nome.replace(' ', ''))
qntdPrimeiroNome = len(nome.split()[0])

print(f'Informações sobre seu nome:\nNome maisculo: {nomeMaisculo}\nNome minusculo: {nomeMinusculo}\nQuantidade de letras: {qntdLetras}\nQuantidade de letras do primeiro nome: {qntdPrimeiroNome}')