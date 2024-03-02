import cube
from cfop import Solver

# PLL-F
c = cube.Cube("YYYYYYYYYRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBWWWWWWWWW")
c.scramble("U R Li F2 R Li Ui R2 Ui R2 L2 F2 U L2 Di B2 D L2 F2")
s = Solver(c)
s.solve()
print("F)\n",c,"\n")
# PLL-Aa
c.scramble("Ui R L U2 R L F2 U L2 B2 D R2 Ui L2 F2 Di F2 R2 L2")
s.solve()
print("Aa)\n",c)
# PLL-Gb
c.scramble("U F B U2 F Bi Ui R2 F2 Ui F2 U F2 R2 D R2 Di")
s.solve()
print("Gb)\n",c)
# PLL-Gd
c.scramble("U2 B F U2 B Fi R2 U R2 Ui F2 U B2 F2 L2 B2 D L2")
s.solve()
print("Gd)\n",c)
# PLL-Ab
c.scramble("F B U2 Fi B L2 U R2 Ui F2 U2 F2 R2 B2 D R2 D R2")
s.solve()
print("Ab)\n",c)
# PLL-Gc
c.scramble("Ui R L U2 R Li B2 U R2 F2 L2 B2 U B2 Ui L2 D F2")
s.solve()
print("Gc)\n",c)
# PLL-Ga
c.scramble("U R L U2 R Li Ui R2 B2 Ui B2 U L2 Ui R2 U L2 B2 R2")
s.solve()
print("Ga)\n",c)
# PLL-H
c.scramble("U F B D2 F B D2 F2 R2 D2 R2 B2 L2 U2 F2 L2")
s.solve()
print("H)\n",c)
# PLL-Na
c.scramble("B Fi U2 Bi F U2 R2 F2 Ui F2 U2 R2 U F2 U2 F2 R2")
s.solve()
print("Na)\n",c)
# PLL-V
c.scramble("B Fi U2 Bi F U2 R2 F2 Ui F2 U2 R2 U F2 U2 F2 R2")
s.solve()
print("V)\n",c)
# PLL-Ja
c.scramble("Ui F B U2 Fi B L2 U F2 Ui B2 U B2 R2 D R2 F2 B2")
s.solve()
print("Ja)\n",c)
# PLL-Ua
c.scramble("F2 D F2 R2 F2 D R2 F2 D2 F2 B2 L2 B2 R2 D2 R2")
s.solve()
print("Ua)\n",c)
# PLL-Ub
c.scramble("L2 U B2 L2 B2 U B2 U2 B2 U2 L2 B2 L2 U2 L2")
s.solve()
print("Ub)\n",c)
# PLL-E
c.scramble("R L F2 Ri Li F2 U B2 Di F2 L2 F2 D B2 U R2 U2 F2")
s.solve()
print("E)\n",c)
# PLL-T
c.scramble("B F R2 B F U B2 Ui F2 R2 Ui R2 U R2 B2 Ui B2 R2")
s.solve()
print("T)\n",c)
# PLL-Z
c.scramble("U F B U2 F Bi Ui F2 Ui F2 Ui F2 Ui F2 Ui F2 R2 F2 R2")
s.solve()
print("Z)\n",c)
# PLL-Y
c.scramble("U2 F B R2 Fi Bi Ui B2 Ui B2 U R2 D R2 Di F2 U F2")
s.solve()
print("Y)\n",c)
# PLL-Ra
c.scramble("U2 R L U2 R L U B2 Ui F2 U R2 Ui F2 D L2 Di R2 L2")
s.solve()
print("Ra)\n",c)
# PLL-Jb
c.scramble("U2 B F U2 B F U Di L2 Ui L2 D F2 Di L2 D B2")
s.solve()
print("Jb)\n",c)
# PLL-Nb
c.scramble("B Fi U2 Bi F U2 R2 B2 U B2 U2 R2 Ui B2 U2 B2 R2")
s.solve()
print("Nb)\n",c)
# PLL-Rb
c.scramble("U2 L R U2 L Ri U R2 Ui R2 D B2 Di B2 L2 R2 B2 R2")
s.solve()
print("Rb)\n",c)
