import re  # Importando o módulo re para usar expressões regulares

ficheiro = r'C:\Users\004456\Documents\Rep\Day3\AoC2024_day3_input.txt'

# Passo 1: Abrir e ler o conteúdo do arquivo de texto
# Supondo que o arquivo se chame 'entrada.txt' e esteja no mesmo diretório que o script
with open(ficheiro) as arquivo:
    memoria_corrompida = arquivo.read()  # Lê o conteúdo do arquivo

# Passo 2: Encontrar todas as instruções válidas 'mul(X,Y)' usando expressão regular
# A expressão regular abaixo procura por qualquer ocorrência de mul(x,y) onde x e y são números
instrucoes_validas = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memoria_corrompida)

# Passo 3: Inicializar uma variável para somar os resultados
soma_resultados = 0

# Passo 4: Calcular o produto para cada instrução válida
for instrucao in instrucoes_validas:
    x = int(instrucao[0])  # Primeiro número
    y = int(instrucao[1])  # Segundo número
    produto = x * y  # Multiplicação
    soma_resultados += produto  # Adiciona o produto à soma total

# Passo 5: Mostrar o resultado final
print(soma_resultados)  # Imprime o valor total da soma dos produtos