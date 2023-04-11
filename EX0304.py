#Exercício 3
nome = str(input('Digite seu nome completo: '))
idade = int(input('Insira sua idade: '))
if idade >= 18:
    print(f'{nome}, você pode dirigir!')
else:
    print(f'{nome}, você não pode dirigir.')

#Exercício 4
nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
nota3 = float(input('Insira sua terceira nota: '))
nota4 = float(input('Insira sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print(f'Sua média foi {media}, você passou!')
else:
    print(f'Sua média foi {media}, você não foi aprovado.')