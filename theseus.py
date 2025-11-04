class Theseus:
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