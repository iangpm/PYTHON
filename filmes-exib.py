import csv

def MaiorPublicoDeFilmes(filmes):
    cabecalho = next(filmes) 
    publicoTotal = 0
    nomeFilme = ''
    anoExib = ''

    for filme in filmes:
        coluna = float(filme[9])

        if coluna > publicoTotal:
            publicoTotal = coluna
            nomeFilme = filme[2]
            anoExib = filme[1]
        else:
            continue

    print(f'O filme com maior audiência é {nomeFilme}')
    print(f'Público total: {publicoTotal}')
    print(f'Ano de exibição: {anoExib}')

with open('filmes.csv', newline='', encoding='UTF-8') as filmes:

    lerFilme = csv.reader(filmes)

    MaiorPublicoDeFilmes(lerFilme)