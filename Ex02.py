#Exercício 2
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2

print('Sua média foi {}'.format(media))
if media >= 6:
    print('Você foi aprovado!')
else:
    print('Você não foi aprovado!')
