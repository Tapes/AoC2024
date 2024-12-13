ficheiro = r'C:\Users\004456\Documents\Rep\Day6\AoC2024_day6_input.txt'

# Lê o conteúdo do ficheiro
with open(ficheiro) as f:
    lines = [line.rstrip() for line in f]

# Conjuntos de obstruções e locais visitados
obs_set = set()  # (x, y) coordenadas de obstrução
visited = set()  # (x, y) coordenadas de localizações visitadas
x_bound = 0
y_bound = 0
start_x, start_y = None, None
direction_set = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Direções (cima, direita, baixo, esquerda)
direction_index = 0

# Processamento do mapa
for y, line in enumerate(lines):
    if not x_bound:
        x_bound = len(line)
    for x, this_char in enumerate(line):
        if this_char == '#':
            obs_set.add((x, y))
        elif this_char == '^':
            start_x, start_y = x, y
    y_bound += 1

# Inicia a posição no mapa
curr_x, curr_y = start_x, start_y

# Parte 1 - Movimentação até encontrar obstruções
while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
    dx, dy = direction_set[direction_index]

    visited.add((curr_x, curr_y))

    if (curr_x + dx, curr_y + dy) in obs_set:
        direction_index = (direction_index + 1) % 4
    else:
        curr_x += dx
        curr_y += dy

# Agora, adicionando obstruções em locais visitados e verificando o impacto
obstructions = 0  # Contador de obstruções

for potential_obs in visited:
    temp_obstructions = obs_set.union({potential_obs})

    # Resetando a posição inicial e direção
    curr_x, curr_y = start_x, start_y
    direction_index = 0

    # Acompanhamento de onde viramos
    temp_visited = set()

    while curr_x in range(0, x_bound) and curr_y in range(0, y_bound):
        dx, dy = direction_set[direction_index]

        if (curr_x + dx, curr_y + dy) in temp_obstructions:
            if (curr_x, curr_y, dx, dy) in temp_visited:
                # Encontramos um loop, paramos de verificar
                obstructions += 1
                break
            temp_visited.add((curr_x, curr_y, dx, dy))
            direction_index = (direction_index + 1) % 4
        else:
            curr_x += dx
            curr_y += dy

# Imprime o resultado da Parte 2
print(f"Part 2: {obstructions}")