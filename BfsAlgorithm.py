from collections import deque
from heapq import heappush, heappop

from AlgorithmLogger import AlgorithmLogger
from Position import Position

class BfsAlgorithm:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def solve(self, heuristic = False):
        # pomiar czasu i pamięci: początek
        logger = self.create_logger_instance(heuristic)

        logger.start_measure()

        max_queue_size = 1 # maksymalna liczba elementów w kolejce (szerokość drzewa)
        total_visited = 0 # liczba odwiedzonych węzłów

        # algorytm
        start = Position(0, 0)
        finish = Position(self.labyrinth.n - 1, self.labyrinth.m - 1)

        logger.log(f'Start: {start}, Finish: {finish}')

        queue = []
        if not heuristic:
            queue = deque([start]) # FIFO
        else:
            counter = 0
            heappush(queue, (0, counter, start))
        visited = { Position(0, 0): None } # Position(nowe_pole): Position(pole_z_którego_tutaj_przyszliśmy)
                                           # Domyślnie ustawione na start,
                                           # aby program nie wpadał w nieskończoną pętlę
        result = [[0 if self.labyrinth.matrix[i][j] == 0 else 1
                   for j in range(self.labyrinth.m)] for i in range(self.labyrinth.n)] # kopia labiryntu z zachowaniem układu

        # dopóki kolejka nie jest pusta,
        # to pętla pobiera pierwszy element z kolejki i oznacza go jako odwiedzony w tablicy wynikowej result
        while queue:
            if not heuristic:
                current_pos = queue.popleft()
            else:
                _, _, current_pos = heappop(queue)
            total_visited += 1
            result[current_pos.x][current_pos.y] = 2 # oznaczenie jako odwiedzone

            if current_pos == finish:
                logger.log('Finish reached')
                break

            for neighbor in current_pos.neighbors():
                if not self.labyrinth.is_accessible(neighbor):
                    logger.log(f'Encountered a wall near {current_pos} -> {neighbor}')
                    continue

                if neighbor not in visited:
                    visited[neighbor] = current_pos
                    if not heuristic:
                        logger.log(f'Moving {self.direction(current_pos, neighbor)} from {current_pos} to {neighbor}')
                        queue.append(neighbor)
                    else:
                        h = abs(neighbor.x - finish.x) + abs(neighbor.y - finish.y)
                        logger.log(
                            f'Moving {self.direction(current_pos, neighbor)} from {current_pos} to {neighbor} with heuristic = {h}')
                        counter += 1
                        heappush(queue, (h, counter, neighbor))
                else:
                    logger.log(f'Backtracking {self.direction(current_pos, neighbor)} from {current_pos} to {neighbor}')

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
            logger.log('No path found')
            path = []

        # pomiar czasu i pamięci: koniec
        execution_time, peak_memory_kb = logger.stop_measure()

        logger.save(
            result,
            path,
            execution_time,
            peak_memory_kb,
            total_visited,
            max_frontier_size=max_queue_size
        )

        return result

    def create_logger_instance(self, heuristic = False):
        return AlgorithmLogger('bfs_with_heuristic' if heuristic else 'bfs', self.labyrinth.n, self.labyrinth.m)

    # rekonstruuje ścieżkę od końca do początku wg odwiedzin
    def reconstruct_path(self, visited, end_pos):
        path = []
        current_pos = end_pos
        while current_pos is not None:
            path.append(current_pos)
            current_pos = visited[current_pos] # przypisanie poprzednika do current_pos, np. Position(2, 2): Position(1, 2)
        return path[::-1]

    # potrzebne do logowania kroków
    def direction(self, a, b):
        dx = b.x - a.x
        dy = b.y - a.y
        if dx == 1: return 'South'
        if dx == -1: return 'North'
        if dy == 1: return 'East'
        if dy == -1: return 'West'
        return 'Unknown'
