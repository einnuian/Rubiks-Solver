from rubik import cube
from rubik.cfop import Solver

# PLL-F
c = cube.Cube("YYYYYYYYYRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBWWWWWWWWW")
c.scramble("U R Li F2 R Li Ui R2 Ui R2 L2 F2 U L2 Di B2 D L2 F2")
print(c)
s = Solver(c)
s.solve()
print(s.moves)
print("F)\n",c,"\n")
