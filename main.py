from BfsAlgorithm import BfsAlgorithm
from DfsAlgorithm import DfsAlgorithm
from Labyrinth import Labyrinth
from theseus import Theseus

labirynt1 = Labyrinth('data/3x3.txt')
print(labirynt1.n, labirynt1.m, labirynt1.matrix)

bfs_algorithm = BfsAlgorithm()
dfs_algorithm = DfsAlgorithm()

theseus = Theseus(labirynt1.matrix, labirynt1.n, labirynt1.m)
theseus.solve(0,0)

#bfs = bfs_algorithm.solve(labirynt1)
#bfs_heuristics = bfs_algorithm.heuristic(labirynt1)

#dfs = dfs_algorithm.solve(labirynt1)
#dfs_heuristics = dfs_algorithm.heuristic(labirynt1)
