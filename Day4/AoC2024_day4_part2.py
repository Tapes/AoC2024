ficheiro = r'C:\Users\Pepzz\Documents\Repo\Python\AoC2024\Day4\AoC2024_day4_input.txt'

# Parse the grid into a dictionary of (y,x):c 
data = open(ficheiro).readlines()
H, W = len(data), len(data[0])-1
grid = {(y, x): data[y][x] for y in range(H) for x in range(W)}

# Parte 2 - Encontrar um padrão "MAS" em forma de "X"
count = 0
for y, x in grid:
    if grid[y, x] == "A":
        # Verificar diagonais superior esquerda / inferior direita e superior direita / inferior esquerda
        lr = grid.get((y - 1, x - 1), "") + grid.get((y + 1, x + 1), "")  # Diagonal principal
        rl = grid.get((y - 1, x + 1), "") + grid.get((y + 1, x - 1), "")  # Diagonal secundária
        # Incrementa o contador se ambas as diagonais forem combinações válidas de "MAS"
        count += {lr, rl} <= {"MS", "SM"}
print(count)