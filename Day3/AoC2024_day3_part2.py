import re  # Importando o módulo re para usar expressões regulares

ficheiro = r'C:\Users\004456\Documents\Rep\Day3\AoC2024_day3_input.txt'

# Passo 1: Abrir e ler o conteúdo do arquivo de texto
# Supondo que o arquivo se chame 'entrada.txt' e esteja no mesmo diretório que o script
with open(ficheiro) as arquivo:
    memoria_corrompida = arquivo.read()  # Lê o conteúdo do arquivo

# Passo 2: Inicializar variáveis
instrucoes_validas = []  # Para armazenar as instruções válidas 'mul(X,Y)'
mul_ativa = True  # Inicialmente, as instruções 'mul' estão habilitadas
soma_resultados = 0  # Para armazenar a soma dos resultados

# Passo 3: Processar o conteúdo
# Usamos uma expressão regular para identificar as instruções do tipo 'mul(X,Y)' e 'do()' / 'don't()'
for comando in re.finditer(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", memoria_corrompida):
    instrucao = comando.group(0)  # A instrução encontrada
    if instrucao.startswith("mul"):
        # Se a instrução for 'mul(X,Y)', verificamos se ela está habilitada
        if mul_ativa:
            # Se a instrução 'mul' estiver habilitada, calculamos o produto
            x = int(comando.group(2))
            y = int(comando.group(3))
            produto = x * y
            soma_resultados += produto  # Adiciona o produto à soma
    elif instrucao == "do()":
        # Se encontrar 'do()', habilitamos as instruções 'mul'
        mul_ativa = True
    elif instrucao == "don't()":
        # Se encontrar 'don't()', desabilitamos as instruções 'mul'
        mul_ativa = False

# Passo 4: Mostrar o resultado final
print(soma_resultados)  # Imprime o valor total da soma dos produtos habilitados