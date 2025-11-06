class Theseus:
    # 0 - north
    # 1 - south
    # 2 - east
    # 3 - west
    moves = (
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    )

    #labyrinth data
    matrix = (())
    n = 0
    m = 0

    #position of theseus
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
    def solve(self, start_x, start_y):
        if start_x < 0 or start_y < 0:
                print("Starting position below bounds, exiting")
                return
        if start_x > self.m or start_y > self.n:
                print("Starting position above bounds, exiting")
                return
        #starting position is always visited
        self.update_visited()

        while self.positionX != self.n or self.positionY != self.m:
            #For selecting next direction. If at -1, then backtracks
            fdirection = -1

            for i in range(4):
                y = self.moves[i][0]
                x = self.moves[i][1]

                # move is not valid
                if not self.validate_move(y, x):
                    continue

                # makes a move
                match fdirection:
                    case -1:
                        # backtrack
                        if len(self.stack) == 0:
                            print("Nie ma rozwiązania")
                            break
                        previous_position = self.stack.pop()
                        self.positionX = previous_position[1]
                        self.positionY = previous_position[0]
                        break
                    case 0:
                        self.travel_north()
                        break
                    case 1:
                        self.travel_south()
                        break
                    case 2:
                        self.travel_east()
                        break
                    case 3:
                        self.travel_west()
                        break

            #if no moves available, backtrack and try again
            previous_position = self.stack.pop()
            self.positionX = previous_position[1]
            self.positionY = previous_position[0]

        print("Labyrinth solved")
        print(self.visited)

    #dfs with heuristic
    def solve_with_heuristic(self, start_x, start_y):
        if start_x < 0 or start_y < 0:
                print("Starting position below bounds, exiting")
                return
        if start_x > self.m or start_y > self.n:
                print("Starting position above bounds, exiting")
                return
        #starting position is always visited
        self.update_visited()
        while self.positionX != self.n or self.positionY != self.m:

            #calculates distance in tiles to finish
            distance = self.n + self.m
            #For selecting next direction. If at -1, then backtracks
            fdirection = -1

            for i in range(4):
                y = self.moves[i][0]
                x = self.moves[i][1]

                #move is not valid
                if not self.validate_move(y, x):
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
                    if len(self.stack) == 0:
                        print("Nie ma rozwiązania")
                        break
                    previous_position = self.stack.pop()
                    self.positionX = previous_position[1]
                    self.positionY = previous_position[0]
                case 0:
                    self.travel_north()
                case 1:
                    self.travel_south()
                case 2:
                    self.travel_east()
                case 3:
                    self.travel_west()

        print("Labyrinth solved")
        print(self.visited)

    def validate_move(self, y:int, x:int) -> bool:
        # if next move is below bounds
        if self.positionY + y < 0 or self.positionX + x < 0:
            return False
        # if next move is above bounds
        if self.positionY + y > self.m or self.positionX + x > self.n:
            return False
        # if has been visited
        if self.visited[self.positionY + y][self.positionX + x] == 1:
            return False
        # if there is an obstacle
        if self.matrix[self.positionY + y][self.positionX + x] == 1:
            return False
        return True

    def travel_north(self):
        self.save_position()

        #moving
        self.positionY = self.positionY - 1
        self.update_visited()

    def travel_east(self):
        self.save_position()

        #moving
        self.positionX = self.positionX + 1
        self.update_visited()

    def travel_south(self):
        self.save_position()

        #moving
        self.positionY = self.positionY + 1
        self.update_visited()

    def travel_west(self):
        self.save_position()

        #moving
        self.positionX = self.positionX -1
        self.update_visited()

    def save_position(self):
        position = (self.positionY, self.positionX)
        self.stack.append(position)

    def update_visited(self):
        self.visited[self.positionY][self.positionX] = 1