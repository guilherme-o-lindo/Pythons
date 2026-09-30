intervalo = int(input('Digite um número para saber quantos números pares tem do 1 até esse número:\n'))

pares = []

for i in range(1, intervalo + 1):
    if i % 2 == 0:
        pares.append(i)

print(f'Há {len(pares)} números pares entre 1 e {intervalo} sendo eles:\n{pares}')