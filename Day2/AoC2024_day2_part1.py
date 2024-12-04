ficheiro = r'C:\Users\004456\Documents\Rep\Day2\AoC2024_day2_input.txt'

# Função que verifica se uma sequência de números é segura
def seguro(linha):
    # Calcula as diferenças entre números consecutivos
    inc = [linha[i + 1] - linha[i] for i in range(len(linha) - 1)]
    
    # Verifica se as diferenças são apenas 1, 2 ou 3 (crescente) 
    # ou se as diferenças são -1, -2 ou -3 (decrescente)
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True  # Se for seguro, retorna True
    return False  # Caso contrário, retorna False

# Lê o arquivo de texto, separando os números por espaços, e converte cada linha em uma lista de inteiros
data = [[int(y) for y in x.split(' ')] for x in open(ficheiro).read().split('\n')]

# Conta quantos relatórios (linhas) são seguros usando a função is_safe
safe_count = sum([seguro(linha) for linha in data])
print(safe_count)  # Exibe o número de relatórios seguros