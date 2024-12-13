def load_input(file_path):
    """
    Carrega as regras de ordenação e os updates a partir de um ficheiro de entrada.

    :param file_path: Caminho para o ficheiro de entrada.
    :return: Uma tupla com as regras de ordenação (lista de tuplas) e os updates (lista de listas).
    """
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()  # Lê todas as linhas do ficheiro e remove quebras de linha

    # Separar regras de ordenação e updates
    split_index = lines.index('')  # Encontra a linha vazia que separa regras dos updates
    ordering_rules = [tuple(map(int, line.split('|'))) for line in lines[:split_index]]  # Processa as regras como tuplas de inteiros
    updates = [list(map(int, line.split(','))) for line in lines[split_index + 1:]]  # Processa os updates como listas de inteiros

    return ordering_rules, updates

def is_update_ordered(update, rules):
    """
    Verifica se um update está na ordem correta de acordo com as regras fornecidas.

    :param update: Lista de páginas do update.
    :param rules: Lista de regras de ordenação como tuplas (X, Y), onde X deve preceder Y.
    :return: True se o update está na ordem correta, False caso contrário.
    """
    position = {page: idx for idx, page in enumerate(update)}  # Mapeia cada página para sua posição no update

    for x, y in rules:
        # Verifica se ambas as páginas estão no update e se a ordem está errada
        if x in position and y in position and position[x] > position[y]:
            return False

    return True

def find_middle_page(update):
    """
    Encontra a página central de um update.

    :param update: Lista de páginas do update.
    :return: O valor da página central.
    """
    middle_index = len(update) // 2  # Calcula o índice do meio
    return update[middle_index]  # Retorna a página correspondente ao índice do meio

def order_update(update, rules):
    """
    Ordena um update incorreto de acordo com as regras fornecidas.

    :param update: Lista de páginas do update.
    :param rules: Lista de regras de ordenação como tuplas (X, Y).
    :return: Uma nova lista com as páginas ordenadas corretamente.
    """
    dependencies = {page: set() for page in update}  # Inicializa dependências para cada página no update
    
    for x, y in rules:
        # Adiciona dependências apenas para páginas presentes no update
        if x in dependencies and y in dependencies:
            dependencies[y].add(x)

    ordered = []  # Lista para armazenar as páginas ordenadas
    while dependencies:  # Enquanto houver páginas com dependências
        for page, deps in list(dependencies.items()):
            if not deps:  # Se a página não tiver dependências
                ordered.append(page)  # Adiciona ao resultado ordenado
                del dependencies[page]  # Remove a página processada
                for remaining in dependencies.values():
                    remaining.discard(page)  # Remove a página das dependências restantes

    return ordered

if __name__ == "__main__":
    # Caminho para o ficheiro de entrada
    input_file = r'C:\Users\Pepzz\Documents\Repo\Python\AoC2024\Day5\AoC2024_day5_input.txt'

    # Carregar regras e updates
    ordering_rules, updates = load_input(input_file)

    # Processar updates
    correctly_ordered_updates = []  # Lista de updates na ordem correta
    incorrectly_ordered_updates = []  # Lista de updates fora de ordem
    middle_pages_sum_correct = 0  # Soma das páginas centrais dos updates corretos
    middle_pages_sum_incorrect = 0  # Soma das páginas centrais dos updates corrigidos

    for update in updates:
        if is_update_ordered(update, ordering_rules):
            correctly_ordered_updates.append(update)  # Adiciona à lista de updates corretos
            middle_pages_sum_correct += find_middle_page(update)  # Calcula e adiciona a página central
        else:
            incorrectly_ordered_updates.append(update)  # Adiciona à lista de updates incorretos

    # Ordenar updates incorretos e calcular soma das páginas centrais
    for update in incorrectly_ordered_updates:
        ordered_update = order_update(update, ordering_rules)  # Ordena o update incorreto
        middle_pages_sum_incorrect += find_middle_page(ordered_update)  # Calcula e adiciona a página central

    # Exibir resultados
    #print(f"Soma das páginas centrais dos updates ordenados corretamente: {middle_pages_sum_correct}")
    print(f"Soma das páginas centrais dos updates corrigidos: {middle_pages_sum_incorrect}")