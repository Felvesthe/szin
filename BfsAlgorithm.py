from collections import deque

class BfsAlgorithm:

    def solve(self, labyrinth):
        n, m = labyrinth.n, labyrinth.m
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # północ / wschód / południe / zachód
        start = (0, 0)
        finish = (n - 1, m - 1)
        queue = deque([start]) # FIFO
        visited = { (0, 0): None } # nowe_pole: pole_z_którego_tutaj_przyszliśmy / (0, 0): None to start,
                                   # aby program nie wpadał w nieskończoną pętlę
        result = [[0 if labyrinth.matrix[i][j] == 0 else 1 for j in range(m)] for i in range(n)] # kopia labiryntu z zachowaniem układu

        # dopóki kolejka nie jest pusta,
        # to pętla pobiera pierwszy element z kolejki i oznacza go jako odwiedzony w tablicy wynikowej result
        while queue:
            x, y = queue.popleft()
            result[x][y] = 2 # oznaczenie jako odwiedzone

            if (x, y) == finish:
                break

            # iteruje w każdym kierunku na podstawie zmiennej directions, wyznacza współrzędne sąsiada
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # sprawdza czy pole mieści się w granicach labiryntu oraz czy nie jest przeszkodą
                if labyrinth.is_accessible(nx, ny):
                    # jeśli spełnia powyższy warunek, to sprawdzane jest, czy pole nie zostało już wcześniej odwiedzone
                    if (nx, ny) not in visited:
                        # do visited zostaje dodany sąsiad, wraz z informacją o polu, z którego przyszliśmy
                        # następnie pole jest wrzucane na kolejkę, dzięki czemu będzie pobrane w kolejnej iteracji
                        visited[(nx, ny)] = (x, y)
                        queue.append((nx, ny))

        # sprawdzamy, czy punkt końcowy był odwiedzony, jeśli tak, to jest zapisywana ścieżka powrotna do result,
        # na podstawie danych zapisanych w visited
        # ścieżka jest oznaczana cyfrą 3
        if finish in visited:
            x, y = finish
            while (x, y) is not None:
                result[x][y] = 3
                if visited[(x, y)] is not None:
                    x, y = visited[(x, y)]
                else:
                    break
        else:
            print('No path found')

        print(result)


    def heuristic(self):
        # Manhattan wzór: h(n) = |x_cel - x_n| + |y_cel - y_n|
        return