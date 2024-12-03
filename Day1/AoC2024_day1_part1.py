import pandas as pd

# Lê o arquivo de texto
ficheiro = r'C:\Users\Pepzz\Documents\Repo\Python\AoC2024\Day1\AoC2024_day1_input.txt'

try:
    # Lê o ficheiro, assumindo que os números estão separados por espaços ou tabulação
    df = pd.read_csv(ficheiro, delimiter=r'\s+', header=None)

    # Ordena cada coluna separadamente
    col1_sorted = df[0].sort_values().reset_index(drop=True)
    col2_sorted = df[1].sort_values().reset_index(drop=True)

    # Inicializa a soma total das diferenças
    soma_total = 0

    # Itera sobre os números mais pequenos e calcula a diferença
    print("Diferença entre os números mais pequenos de cada coluna:")
    for i in range(min(len(col1_sorted), len(col2_sorted))):
        min_col1 = col1_sorted[i]
        min_col2 = col2_sorted[i]
        diferenca = abs(min_col1 - min_col2)
        soma_total += diferenca
        print(f"Iteração {i + 1}: {min_col1} - {min_col2} = {diferenca}")
    
    print(soma_total)

except FileNotFoundError:
    print("O ficheiro não foi encontrado no caminho especificado.")