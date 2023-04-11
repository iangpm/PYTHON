#Exercício 5
num = int(input('Insira um número inteiro: '))
if (num % 2) == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')

#Exercício 6
sal = float(input('Insira seu salário: '))
sal1 = (sal * 1.10)
sal2 = (sal * 1.15)
if sal > 1500.00:
    print(f'Seu salário ficou R${sal1 :.2f} após o aumento')
elif sal <= 1500.00:
    print(f'Seu salário ficou {sal2 :.2f} após o aumento')