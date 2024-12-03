# Nome do ficheiro
ficheiro = r'C:\Users\Pepzz\Documents\Repo\Python\AoC2024\Day1\AoC2024_day1_input.txt'

# Lê o ficheiro e processa as listas esquerda e direita
lista_esquerda = []
lista_direita = []

with open(ficheiro, 'r') as f:
    for linha in f:
        esquerda, direita = map(int, linha.strip().split())
        lista_esquerda.append(esquerda)
        lista_direita.append(direita)

# Calcula o score de similaridade
score_total = 0
for numero in lista_esquerda:
    contagem = lista_direita.count(numero)
    score_total += numero * contagem

# Exibe o score total
print(f"Score de Similaridade Total: {score_total}")
