import random
import sys

# python labyrinth_generator.py <wiersze> <kolumny> [wall_prob = 0.3]

def generate_labyrinth(n, m, wall_prob=0.3):
    """
    Generuje labirynt n x m z gwarantowaną ścieżką
    od wejścia (0,0) do wyjścia (n-1,m-1) i losowymi przeszkodami.
    wall_prob - prawdopodobieństwo, że dana komórka będzie ścianą (1)
    """
    # Najpierw cała plansza wypełniona ścianami
    maze = [[1 for _ in range(m)] for _ in range(n)]

    # Tworzymy losową ścieżkę start → finish
    x, y = 0, 0
    maze[y][x] = 0
    path = [(y, x)]
    while (y, x) != (n-1, m-1):
        moves = []
        if x < m-1: moves.append((y, x+1))
        if y < n-1: moves.append((y+1, x))
        next_cell = random.choice(moves)
        y, x = next_cell
        maze[y][x] = 0
        path.append((y, x))

    # Losowe wypełnianie pozostałych pól zgodnie z wall_prob
    for i in range(n):
        for j in range(m):
            if (i,j) not in path:  # nie zamieniamy ścieżki start→finish
                maze[i][j] = 1 if random.random() < wall_prob else 0

    return maze

def save_maze_to_file(maze, filename):
    n = len(maze)
    m = len(maze[0])
    with open(filename, "w") as f:
        f.write(f"{n} {m}\n")
        for row in maze:
            f.write(" ".join(str(cell) for cell in row) + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Użycie: python labyrinth_generator.py <wiersze> <kolumny> [wall_prob]")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    wall_prob = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3

    maze = generate_labyrinth(n, m, wall_prob)
    filename = f"data/{n}x{m}.txt"
    save_maze_to_file(maze, filename)
    print(f"Labirynt zapisano do pliku: {filename}")
