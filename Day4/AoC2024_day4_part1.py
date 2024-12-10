# Função para verificar a ocorrência da palavra XMAS em todas as direções possíveis
def contar_ocorrencias(matriz, palavra="XMAS"):
    # Obtém o tamanho da matriz
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    # Variável para contar o número de ocorrências
    ocorrencias = 0
    
    # Função auxiliar para verificar uma palavra em uma direção específica
    def verificar_direcao(x, y, dx, dy):
        for i in range(len(palavra)):
            # Verifica se a posição está fora dos limites da matriz
            if not (0 <= x < linhas and 0 <= y < colunas):
                return False
            if matriz[x][y] != palavra[i]:
                return False
            x += dx
            y += dy
        return True

    # Verifica todas as possíveis direções para todas as posições
    for i in range(linhas):
        for j in range(colunas):
            # Verifica em 8 direções (4 principais e as inversas)
            # Direções: horizontal, vertical e diagonal
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if verificar_direcao(i, j, dx, dy):
                    ocorrencias += 1

    return ocorrencias

# Função para ler o conteúdo do arquivo de texto
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        # Lê todas as linhas do arquivo e as transforma em uma lista de listas de caracteres
        return [list(linha.strip()) for linha in arquivo.readlines()]

# Função principal que executa a busca no caça-palavras
def main():
    # Nome do arquivo que contém a matriz do caça-palavras
    nome_arquivo = r'C:\Users\004456\Documents\Rep\Day4\AoC2024_day4_input.txt'
    
    # Lê a matriz do arquivo
    matriz = ler_arquivo(nome_arquivo)
    
    # Conta as ocorrências da palavra "XMAS"
    total_ocorrencias = contar_ocorrencias(matriz, palavra="XMAS")
    
    # Exibe o resultado
    print(f"A palavra 'XMAS' aparece {total_ocorrencias} vezes no caça-palavras.")

# Executa a função principal
if __name__ == "__main__":
    main()