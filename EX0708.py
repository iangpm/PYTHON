#Exercício 7
lista_num = [1, 2, 8, 102, 84, 56, 98, 6, 22, 35]
print(f'O maior número da lista é {max(lista_num)}')
print(f'O menor número da lista é {min(lista_num)}')

#Exercício 8
pal = str(input('Insira uma palavra: '))
pal2 = pal [::-1]
if pal2 == pal:
    print(f'A palavra {pal} é um palíndromo!')
else:
    print(f'A palavra {pal} não é um palíndromo.')