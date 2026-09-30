texto = input("Digite uma palavra: ").lower()

vogais = []

for letra in texto:
    if letra in 'aeiouáéíóúâêôãõà':
        vogais.append(letra)



print(f"Há {len(vogais)} vogais e elas são: {vogais}")