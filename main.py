from BfsAlgorithm import BfsAlgorithm
from Labyrinth import Labyrinth
from theseus import Theseus

labyrinth1 = Labyrinth('data/5x5.txt')
labyrinth2 = Labyrinth('data/256x256.txt')
labyrinth3 = Labyrinth('data/1048x1280.txt')
labyrinth4 = Labyrinth('data/2096x2560.txt')
labyrinth5 = Labyrinth('data/4096x5120.txt')

# bfs = BfsAlgorithm(labyrinth1)
# bfs.solve(heuristic=False)

# theseus = Theseus(labyrinth1)
# theseus.solve(0,0)
# theseus.solve_with_heuristic(0,0)