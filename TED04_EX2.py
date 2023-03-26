#Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se
#forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
#calcule e escreva o custo total da compra
qtd = int(input('Insira a quantidade de maçãs compradas: '))
pi1 = 1.0
pi2 = 1.3
if qtd >= 12:
    print('Você comprou {} maçãs e o custo total foi de R${}!'.format(qtd, qtd * pi1))
elif qtd < 12:
    print('Você comprou {} maçãs e o custo total foi de R${}!'.format(qtd, (qtd * pi2)))

