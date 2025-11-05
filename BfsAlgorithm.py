import time
import tracemalloc
from collections import deque

from Position import Position

class BfsAlgorithm:

    def solve(self, labyrinth):
        # pomiar czasu i pamięci: początek
        start_time = time.perf_counter()
        tracemalloc.start()

        max_queue_size = 1 # maksymalna liczba elementów w kolejce (szerokość drzewa)
        total_visited = 0 # liczba odwiedzonych węzłów

        # algorytm
        start = Position(0, 0)
        finish = Position(labyrinth.n - 1, labyrinth.m - 1)
        queue = deque([start]) # FIFO
        visited = { Position(0, 0): None } # Position(nowe_pole): Position(pole_z_którego_tutaj_przyszliśmy)
                                           # Domyślnie ustawione na start,
                                           # aby program nie wpadał w nieskończoną pętlę
        result = [[0 if labyrinth.matrix[i][j] == 0 else 1
                   for j in range(labyrinth.m)] for i in range(labyrinth.n)] # kopia labiryntu z zachowaniem układu

        # dopóki kolejka nie jest pusta,
        # to pętla pobiera pierwszy element z kolejki i oznacza go jako odwiedzony w tablicy wynikowej result
        while queue:
            current_pos = queue.popleft()
            total_visited += 1
            result[current_pos.x][current_pos.y] = 2 # oznaczenie jako odwiedzone

            if current_pos == finish:
                break

            for neighbor in current_pos.neighbors():
                if labyrinth.is_accessible(neighbor) and neighbor not in visited:
                    visited[neighbor] = current_pos
                    queue.append(neighbor)

            # aktualizacja maksymalnej liczby węzłów w kolejce
            if len(queue) > max_queue_size:
                max_queue_size = len(queue)

        # sprawdzamy, czy punkt końcowy był odwiedzony, jeśli tak, to jest zapisywana ścieżka powrotna do result,
        # na podstawie danych zapisanych w visited
        # ścieżka jest oznaczana cyfrą 3
        if finish in visited:
            path = self.reconstruct_path(visited, finish)
            for pos in path:
                result[pos.x][pos.y] = 3
        else:
            print('No path found')
            path = []

        # pomiar czasu i pamięci: koniec
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        end_time = time.perf_counter()
        tracemalloc.stop()

        execution_time = end_time - start_time
        peak_memory_kb = peak_memory / 1024

        print(f'Czas wykonania: {execution_time:.6f} s')
        print(f'Szczytowe użycie pamięci: {peak_memory_kb:.2f} KB')
        print(f'Liczba odwiedzonych węzłów: {total_visited}')
        print(f'Maksymalna liczba węzłów w kolejce: {max_queue_size}')
        print(f'Długość znalezionej ścieżki: {len(path)}')

        return result

    # rekonstruuje ścieżkę od końca do początku wg odwiedzin
    def reconstruct_path(self, visited, end_pos):
        path = []
        current_pos = end_pos
        while current_pos is not None:
            path.append(current_pos)
            current_pos = visited[current_pos] # przypisanie poprzednika do current_pos, np. Position(2, 2): Position(1, 2)
        return path[::-1]