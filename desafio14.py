# For para iterar o 1 até 10. Entretanto, assim que chegar em 5, o break para a operação
print('Loop com o break:')
for num in range(1, 11):
    if num>5:
        break
    print(num)

# For para pular o número 5 com o continue        
print('\nLoop com o continue')
for num in range(1,11):
    if num==5:
        continue
    print(num)