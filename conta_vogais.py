def conta_vogais(string):
    vogais = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count
string = 'O rato roeu a roupa do rei de Roma'
print(f'A frase tem {conta_vogais(string)} vogais')