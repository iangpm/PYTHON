#Exercício 5
num_conta = int(input('Insira o número da sua conta: '))
saldo = float(input('Insira seu saldo: R$'))
debito = float(input('Insira seu débito: R$'))
credito = float(input('Insira seu crédito: R$'))

saldoa = saldo - debito + credito
print('Seu saldo atual é R${}'.format(saldoa))
if saldoa >= 0:
    print('Saldo Positivo')
else:
    print('Saldo negativo')