from BfsAlgorithm import BfsAlgorithm
from DfsAlgorithm import DfsAlgorithm
from Labyrinth import Labyrinth
from theseus import Theseus

labirynt1 = Labyrinth('data/3x3.txt')

bfs_algorithm = BfsAlgorithm()
dfs_algorithm = DfsAlgorithm()

#theseus = Theseus(labirynt1.matrix, labirynt1.n, labirynt1.m)
#theseus.solve(0,0)

bfs = bfs_algorithm.solve(labirynt1)
print(bfs)