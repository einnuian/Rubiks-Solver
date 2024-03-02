import sys
sys.path.append('../rubik')
# Look for modules in the rubik folder
import cube
from cfop import Solver
from optimize import optimize_moves

c = cube.Cube("GGRRWOGBBOWOYRYOBGYYWGOBWGRGRWOBOGBBYOBRRWOGRRYWYYYWWB")
print(c)
solver = Solver(c)
solver.solve()
solver.solution()
print(c)

a = cube.Cube("yyyyyyyyyrrrgggooobbbrrrgggooobbbrrrgggooobbbwwwwwwwww")
a.scramble("B U2 L2 F D2 Fi L2 D2 Fi L2 D2 Bi Ui L Di Fi L2 R2 U2 R Di")
s = Solver(a)
s.solve()
s.solution()
print(a)

b = cube.Cube("YYYYYYYYYRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBWWWWWWWWW")
sol = Solver(b)
sol.solve()
print(sol.moves)
sol.moves = optimize_moves(sol.moves)
print(sol.moves)

