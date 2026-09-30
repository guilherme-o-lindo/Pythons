obj = input('Digite algo: ')

print(f'O tipo primitivo de {obj} é {type(obj)}')
print(f'É alfabético? {obj.isalpha()}')
print(f'É númerico? {obj.isnumeric()}')
print(f'É alfanúmerico? {obj.isalnum()}')
print(f'Está em maisculuas? {obj.isupper()}')
print(f'Está em minusculas? {obj.islower()}')