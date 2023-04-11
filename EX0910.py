#Exercício 9
tabuada = int(input('A tabuada do número: '))
for count in range(10):
    print('%d x %d = %d' % (tabuada, count + 1, tabuada * (count + 1)))

#Exercício 10
lista_nomes = ['Laura', 'Laura', 'Francisco', 'Mateus', 'Jonathan', 'Francisco']
print(f'A lista original é {lista_nomes}')
print(f'A lista sem duplicatas é {sorted(set(lista_nomes))}')