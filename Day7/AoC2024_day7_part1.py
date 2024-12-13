import itertools

# Lê o arquivo de entrada e armazena as linhas em uma lista
ficheiro = r'C:\Users\004456\Documents\Rep\Day7\AoC2024_day7_input.txt'

# Abrir o arquivo e ler cada linha
with open(ficheiro) as f:
    lines = f.readlines()  # Lê todas as linhas do arquivo

# Função que avalia uma expressão com números e operadores, sem precedência de operadores
def avaliar_expressao(nums, ops):
    # A expressão é uma lista de números e operadores
    result = int(nums[0])  # Começamos com o primeiro número

    # Itera pelos números e operadores
    for i in range(len(ops)):
        if ops[i] == '+':
            result += int(nums[i + 1])  # Soma
        elif ops[i] == '*':
            result *= int(nums[i + 1])  # Multiplicação
    
    return result

# Inicializa a soma total dos resultados válidos
soma_total = 0

# Itera por cada linha do arquivo
for line in lines:
    test_value, expr = line.split(":")  # Divide a linha em valor do teste e a expressão
    test_value = int(test_value)  # Converte o valor do teste para um inteiro
    expr = expr.strip()  # Remove espaços em branco extras

    # Converte a expressão para uma lista de números
    nums = expr.split()

    # Gerar todas as combinações possíveis de operadores (com '+' e '*')
    ops_combinations = itertools.product(['+', '*'], repeat=len(nums) - 1)

    # Verifica todas as combinações de operadores
    for ops in ops_combinations:
        resultado = avaliar_expressao(nums, ops)

        # Se o resultado da expressão for igual ao valor de teste, adiciona ao total
        if resultado == test_value:
            soma_total += test_value
            break  # Se já encontramos uma solução, podemos parar de testar outras combinações

# Imprime a soma total dos resultados válidos
print(f"Soma total: {soma_total}")