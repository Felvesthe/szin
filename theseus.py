class Theseus:
    #TODO: usunąć walidację ruchu z metod travel
    #TODO: obsłużyć wyjątek w którym nie ma drogi do mety
    matrix = (())
    n = 0
    m = 0
    positionX:int = 0
    positionY:int = 0

    #logic matrix
    visited = [[]]
    #visited tiles for backtracking
    stack = []


    def __init__(self, matrix, n, m):
        self.matrix = matrix
        self.n = n - 1
        self.m = m - 1

        self.visited = [[0 for j in range(m)] for i in range(n)]
        print(self.visited)


    #dfs no heuristic
    # TODO: Dodać sprawdzanie czy wchodzi w krawędź
    def solve(self, startX, startY):
        if startX < 0 or startY < 0:
                print("Starting position below bounds, exiting")
                return
        if startX > self.m or startY > self.n:
                print("Starting position above bounds, exiting")
                return
        self.update_visited()
        while(self.positionX != self.n or self.positionY != self.m):
            if self.travelNorth():
                print("Idzie na północ")
                continue
            if self.travelEast():
                print("Idzie na wschód")
                continue
            if self.travelSouth():
                print("Idzie na południe")
                continue
            if self.travelWest():
                print("Idzie na zachód")
                continue

            #if no moves available, backtrack and try again
            previous_position = self.stack.pop()
            self.positionX = previous_position[1]
            self.positionY = previous_position[0]

        print("Zakonczono labiryntowanie")
        print(self.visited)

    #dfs with heuristic
    def solve_with_heuristic(self, startX, startY):
        if startX < 0 or startY < 0:
                print("Starting position below bounds, exiting")
                return
        if startX > self.m or startY > self.n:
                print("Starting position above bounds, exiting")
                return
        #starting position is always visited
        self.update_visited()
        while(self.positionX != self.n or self.positionY != self.m):
            # 0 - north
            # 1 - south
            # 2 - east
            # 3 - west
            moves = (
                (-1,0),
                (1,0),
                (0,1),
                (0,-1)
            )

            #calculates distance in tiles to finish
            distance = self.n + self.m
            #For selecting next direction. If at -1, then backtracks
            fdirection = -1

            for i in range(4):
                y = moves[i][0]
                x = moves[i][1]

                #if next move is below bounds
                if (self.positionY + y < 0 or self.positionX + x < 0):
                    continue
                #if next move is above bounds
                if (self.positionY + y > self.m or self.positionX + x > self.n):
                    continue
                #if has been visited
                if (self.visited[self.positionY + y][self.positionX + x] == 1):
                    continue
                #if there is an obstacle
                if (self.matrix[self.positionY + y][self.positionX + x] == 1):
                    continue

                #move is valid, calculate its distance to finish
                mannhatan_distance = abs((self.positionY + y) - self.m) + abs((self.positionX + x) - self.n)
                #selects move with the lowest distance
                if  mannhatan_distance < distance:
                    fdirection = i
                    distance = mannhatan_distance

            #makes a move
            match fdirection:
                case -1:
                    #backtrack
                    previous_position = self.stack.pop()
                    self.positionX = previous_position[1]
                    self.positionY = previous_position[0]
                case 0:
                    self.travelNorth()
                case 1:
                    self.travelSouth()
                case 2:
                    self.travelEast()
                case 3:
                    self.travelWest()

        print("Zakonczono labiryntowanie")
        print(self.visited)

    def travelNorth(self):
        if (self.positionY - 1 < 0):
            return 0
        if (self.visited[self.positionY - 1][self.positionX] == 1):
            return 0

        self.savePosition()

        #moving
        self.positionY = self.positionY - 1
        self.update_visited()
        return 1

    def travelEast(self):
        if (self.positionX + 1 > self.n):
            return 0
        if (self.visited[self.positionY][self.positionX + 1] == 1):
            return 0

        self.savePosition()

        #moving
        self.positionX = self.positionX + 1
        self.update_visited()
        return 1

    def travelSouth(self):
        if (self.positionY + 1 > self.m):
            return
        if (self.visited[self.positionY + 1][self.positionX] == 1):
            return 0

        self.savePosition()

        #moving
        self.positionY = self.positionY + 1
        self.update_visited()
        return 1

    def travelWest(self):
        if (self.positionX - 1 < 0):
            return
        if (self.visited[self.positionY][self.positionX - 1] == 1):
            return 0

        self.savePosition()

        #moving
        self.positionX = self.positionX -1
        self.update_visited()
        return 1

    def savePosition(self):
        position = (self.positionY, self.positionX)
        self.stack.append(position)

    def update_visited(self):
        self.visited[self.positionY][self.positionX] = 1