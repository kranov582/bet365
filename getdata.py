import pandas as pd
from PrettyColorPrinter import add_printer

add_printer(1)
df = pd.read_excel('dados_teams.xlsx')['aa_innerText']

print(df)


liga = []
for i in range(len(df)):
    liga.append(df[i].split('\n')[0])

lista = []
for i in range(len(df)):
    elementos = df.iloc[i].split('\n')  # Dividir a linha em elementos
    elementos_apos_quarto = elementos[4:]  # Pegar elementos a partir do quinto elemento (índice 4 em Python)
    lista.extend(elementos_apos_quarto)  # Adicionar os elementos à lista

print(lista)

lista = [texto for texto in lista if not texto.startswith(("Para Marcar o", "Sem Gol", "("))]

n = 9  # Número de elementos em cada sublista
nova_lista = []

for i in range(0, len(lista), n):
    sublista = lista[i:i+n]  # Pegar 9 elementos em sequência
    nova_lista.append(sublista)

print(nova_lista)


dados_finais = pd.DataFrame(nova_lista, columns = ['Time 1', 'Time 2', 'Tempo de jogo','numero', 'Gols time 1', 'Gols time 2', '1', 'x', '2'])

print(dados_finais)



