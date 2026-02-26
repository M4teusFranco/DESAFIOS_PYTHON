frutas = ['Maçã', 'Maçã', 'Maçã', 'Melancia', 'Tomate', 'Melão'] # Declaração de valores do array 'frutas'
contador = 0 # Declara o valor do contador

# For iterando a contagem de repetição da palavra 'Maçã'
for fruta in frutas:
    if fruta == 'Maçã':
        contador +=1

# Exibe a quantidade da repetição da palavra 'Maçã'
print(f'Número de Maçãs no array: {contador}')