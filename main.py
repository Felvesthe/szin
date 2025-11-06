from BfsAlgorithm import BfsAlgorithm
from Labyrinth import Labyrinth
from theseus import Theseus

labirynt1 = Labyrinth('data/5x5.txt')

bfs_algorithm = BfsAlgorithm()

#theseus = Theseus(labirynt1.matrix, labirynt1.n, labirynt1.m)
#theseus.solve(0,0)

bfs = bfs_algorithm.solve(labirynt1)
