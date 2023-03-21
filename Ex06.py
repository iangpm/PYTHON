#Exercício 6
qtd_at = input('Insira a quantidade atual: ')
qtd_max = input('Insira a quantidade máxima: ')
qtd_min = input('Insira a quantidade mínima: ')
qtd_med = qtd_max + qtd_min
print('A quantidade atual em estoque é {}'.format(qtd_at))
if qtd_at >= qtd_med:
    print('Não efetuar compra')
else:
    print('Efetuar compra!')