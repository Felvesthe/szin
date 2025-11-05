def read_from_file(file_path):
    with open(file_path) as f:
        n, m = map(int, f.readline().split())
        matrix = [list(map(int, f.readline().split())) for _ in range(m)]
    return n, m, matrix

class Labyrinth:
    def __init__(self, file_path):
        self.n, self.m, self.matrix = read_from_file(file_path)

    # Zwraca True, jeśli podane pole jest w granicach labiryntu oraz nie jest przeszkodą
    def is_accessible(self, position):
        return 0 <= position.x < self.n and 0 <= position.y < self.m and self.matrix[position.x][position.y] == 0