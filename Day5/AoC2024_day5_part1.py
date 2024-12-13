def load_input(file_path):
    """
    Carrega as regras de ordenação e os updates a partir de um ficheiro de entrada.

    :param file_path: Caminho para o ficheiro de entrada.
    :return: Uma tupla com as regras de ordenação (lista de tuplas) e os updates (lista de listas).
    """
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    # Separar regras de ordenação e updates
    split_index = lines.index('')
    ordering_rules = [tuple(map(int, line.split('|'))) for line in lines[:split_index]]
    updates = [list(map(int, line.split(','))) for line in lines[split_index + 1:]]

    return ordering_rules, updates

def is_update_ordered(update, rules):
    """
    Verifica se um update está na ordem correta de acordo com as regras fornecidas.

    :param update: Lista de páginas do update.
    :param rules: Lista de regras de ordenação como tuplas (X, Y), onde X deve preceder Y.
    :return: True se o update está na ordem correta, False caso contrário.
    """
    position = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position and position[x] > position[y]:
            return False

    return True

def find_middle_page(update):
    """
    Encontra a página central de um update.

    :param update: Lista de páginas do update.
    :return: O valor da página central.
    """
    middle_index = len(update) // 2
    return update[middle_index]

if __name__ == "__main__":
    # Caminho para o ficheiro de entrada
    input_file = r'C:\Users\Pepzz\Documents\Repo\Python\AoC2024\Day5\AoC2024_day5_input.txt'

    # Carregar regras e updates
    ordering_rules, updates = load_input(input_file)

    # Filtrar updates ordenados corretamente e calcular a soma das páginas centrais
    correctly_ordered_updates = []
    middle_pages_sum = 0

    for update in updates:
        if is_update_ordered(update, ordering_rules):
            correctly_ordered_updates.append(update)
            middle_pages_sum += find_middle_page(update)

    # Exibir resultados
    #print(f"Updates ordenados corretamente: {len(correctly_ordered_updates)}")
    print(f"Soma das páginas centrais dos updates ordenados corretamente: {middle_pages_sum}")