from rubik import cube
from rubik.cfop import Solver

c = cube.Cube("YYYYYYYYYRRRGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBWWWWWWWWW")
# OLL-1
c.scramble("U2 Bi R Ui R U Ri B L2 Ui B2 D L2 F2 Di L2 B2 L2 R2")
s = Solver(c)
s.solve()
print("1)\n",c)
# OLL-6
c.scramble("U2 F U R Ui Ri F Ui L2 Ui L2 U L2 Ui L2 U2 F2 U L2 U L2")
s.solve()
print("6)\n",c)
# OLL-8
c.scramble("U2 F U R Ui Ri F Ui L2 Ui L2 U L2 Ui L2 U2 F2 U L2 U L2")
s.solve()
print("8)\n",c)
# OLL-11
c.scramble("U L2 Fi D L Di Li F U L2 Ui F2 R2 Ui B2 R2 F2 U L2 Di")
s.solve()
print("11)\n",c)
# OLL-14
c.scramble("U L D R2 Di L D2 B2 L2 F2 U F2 U L2 B2 R2 L2")
s.solve()
print("14)\n",c)
# OLL-15
c.scramble("L D R2 D2 Fi D F Li B2 D F2 R2 Ui L2 B2 U2 F2 Di L2")
s.solve()
print("15)\n",c)
# OLL-20
c.scramble("Ui Li Bi R Bi R2 D2 L U2 Ri U2 B2 U B2 R2 U2 L2 D F2 D2 L2")
s.solve()
print("20)\n",c)
# OLL-24
c.scramble("U2 F2 Ri L2 Fi R L2 F L2 F R2 D R2 Ui F2 Ui R2 Di R2 U2 F2")
s.solve()
print("24)\n",c)
# OLL-25
c.scramble("B Di B2 Ri Ui R U2 B2 D B U2 L2 Ui L2 Ui B2 L2 U L2")
s.solve()
print("25)\n",c)
'''# OLL-27
c.scramble("F R U Ri F2 D F2 Ui Fi U L2 B2 Ui L2 F2 R2 D2 F2")
s.solve()
print("27)\n",c)'''
# OLL-30
c.scramble("Li Ui Bi U B L F2 Di L2 U2 B2 U L2 F2 Ui B2 Di B2 D2 R2")
s.solve()
print("30)\n",c)
# OLL-36
c.scramble("U L Bi R2 Di Fi D F2 R2 B L F2 L2 R2 B2 Ui B2 U B2 U R2")
s.solve()
print("36)\n",c)
# OLL-38
c.scramble("U R Di B2 Li Bi L Bi D R Ui F2 L2 Ui L2 Ui F2 R2 B2 D2 B2")
s.solve()
print("38)\n",c)
# OLL-39
c.scramble("L Ri B2 D2 F L Ri Ui L2 U2 B2 U R2 Di L2 F2 Di L2 D F2")
s.solve()
print("39)\n",c)
# OLL-43
c.scramble("U2 Li B Ui B U Bi L B2 U L2 U2 L2 B2 Ui L2 Ui L2")
s.solve()
print("43)\n",c)
# OLL-46
c.scramble("R2 F2 U B Ri B2 R B Ui F2 U L2 Ui R2 U2 B2 Ui B2 Ui L2")
s.solve()
print("46)\n",c)
# OLL-47
c.scramble("Ui Fi Li B Li Bi L2 F U R2 B2 F2 Ui F2 U F2 Di F2 D B2 R2")
s.solve()
print("47)\n",c)
# OLL-48
c.scramble("U2 F D Bi Di F D Bi R2 U L2 Ui R2 F2 Di L2 Ui R2 F2 L2 D2")
s.solve()
print("48)\n",c)
# OLL-50
c.scramble("B2 Ri F R Bi D B D R2 F U F2 L2 F2 R2 U D L2")
s.solve()
print("50)\n",c)
# OLL-51
c.scramble("U Li B2 D Bi Di Bi L Ui F2 L2 F2 Ui F2 L2 U B2 Di B2 Ui F2")
s.solve()
print("51)\n",c)
'''# OLL-54
c.scramble("Ui Li U2 R B Li B Ri L2 U R2 U2 B2 U R2 U2 B2 Ui R2 U2 B2")
s.solve()
print("54)\n",c)'''
# OLL-56
c.scramble("Ui L F U2 R2 F2 L Fi L2 U2 R U2 L2 U2 L2 B2 R2 D2 B2")
s.solve()
print("56)\n",c)
