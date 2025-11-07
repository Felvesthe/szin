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

        # algorytm
        start = Position(0, 0)
        finish = Position(self.labyrinth.n - 1, self.labyrinth.m - 1)

        total_visited_nodes = 0

        if not heuristic:
            queue = deque([start]) # deque to doubly linked list,
                                   # późniejsze użycie popleft ma złożoność O(1),
                                   # gdyby to była zwykła lista to metoda pop ma złożoność O(n)
        else:
            queue = []
            counter = 0
            heappush(queue, (0, counter, start))
        visited = { Position(0, 0): None } # Position(nowe_pole): Position(pole_z_którego_tutaj_przyszliśmy)
                                           # Domyślnie ustawione na start,
                                           # aby program nie wpadał w nieskończoną pętlę
        result = [row[:] for row in self.labyrinth.matrix]

        # dopóki kolejka nie jest pusta,
        # to pętla pobiera pierwszy element z kolejki i oznacza go jako odwiedzony w tablicy wynikowej result
        while queue:
            if not heuristic:
                current_pos = queue.popleft()
            else:
                _, _, current_pos = heappop(queue)
            total_visited_nodes += 1
            result[current_pos.x][current_pos.y] = 2 # oznaczenie jako odwiedzone

            if current_pos == finish:
                break

            for neighbor in current_pos.neighbors():
                if not self.labyrinth.is_accessible(neighbor):
                    continue

                if neighbor not in visited:
                    visited[neighbor] = current_pos
                    if not heuristic:
                        queue.append(neighbor)
                    else:
                        h = abs(neighbor.x - finish.x) + abs(neighbor.y - finish.y)
                        counter += 1
                        # Greedy Best-First Search - algorytm wybiera pole, które jest najbliżej celu wg heurystyki
                        # Nie uwzględnia długości drogi od startu
                        heappush(queue, (h, counter, neighbor))

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
        logger.stop_measure()

        logger.save(
            result,
            path,
            total_visited_nodes
        )

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
