#Exercício 4
def verifica_primos(num):
    num = int(input('Insira um número: '))
    if (num % num) == 0:
        print('True')
    elif (num % 1) == 0:
        print('True')
    else:
        print('False')