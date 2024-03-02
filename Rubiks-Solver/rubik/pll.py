import cube

def permutation_last_layer(self):
        # 21 PLL cases: https://jperm.net/algs/pll
        # Cases are identified by matching all pieces of a specific color
        # Order (based on jperm.net): G - B - R - O
        def skip():
            return (self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0] and
                    self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2])

        def Aa():
            return (self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, -1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[0, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2] == self.cube[1, 1, -1].colors[0])

        def Ab():
            return (self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0])

        def caseF():
            return (self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, 1].colors[2] == self.cube[1, 1, 1].colors[0] and
                    self.cube[0, 1, -1].colors[2] == self.cube[-1, 1, 1].colors[2] == self.cube[1, 1, -1].colors[0] and
                    self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 1].colors[2] == self.cube[1, 1, 0].colors[0])

        def Ga():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[0, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0])

        def Gb():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[0, 1, -1].colors[2] == self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0])
        def Gc():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0])
        def Gd():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2])

        def Ja():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2] and
                    self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0])

        def Jb():
            return (self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0] and
                    self.cube[1, 1, -1].colors[2] == self.cube[0, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0] and
                    self.cube[1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2])

        def Ra():
            return (self.cube[-1, 1, -1].colors[0] == self.cube[0, 1, -1].colors[2] == self.cube[-1, 1, 1].colors[0] and
                    self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2])

        def Rb():
            return (self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0])

        def T():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[1, 1, 0].colors[0])

        def E():
            return (self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, -1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[2])

        def Na():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[-1, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[2] == self.cube[0, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[1, 1, 1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[-1, 1, 0].colors[0] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0])

        def Nb():
            return (self.cube[1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, -1].colors[0] and
                    self.cube[-1, 1, 1].colors[0] == self.cube[1, 1, 1].colors[0] == self.cube[1, 1, 0].colors[0])

        def V():
            return (self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[0] and
                    self.cube[-1, 1, 1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0])

        def caseY():
            return (self.cube[1, 1, -1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] and
                    self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0])

        def H():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] == self.cube[0, 1, 1].colors[2] and
                    self.cube[-1, 1, 1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0])

        def Ua():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] and
                    self.cube[-1, 1, 1].colors[2] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[1, 1, 0].colors[0] == self.cube[-1, 1, 1].colors[0])
        def Ub():
            return (self.cube[-1, 1, -1].colors[2] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] and
                    self.cube[-1, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2] == self.cube[1, 1, 0].colors[0] and
                    self.cube[1, 1, -1].colors[0] == self.cube[-1, 1, 0].colors[0] == self.cube[1, 1, 1].colors[0] and
                    self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2])
        def caseZ():
            return (self.cube[-1, 1, -1].colors[0] == self.cube[-1, 1, 1].colors[0] == self.cube[0, 1, 1].colors[2] and
                    self.cube[1, 1, -1].colors[0] == self.cube[0, 1, -1].colors[2] == self.cube[1, 1, 1].colors[0] and
                    self.cube[-1, 1, -1].colors[2] == self.cube[1, 1, -1].colors[2] == self.cube[1, 1, 0].colors[0] and
                    self.cube[-1, 1, 1].colors[2] == self.cube[1, 1, 1].colors[2] == self.cube[-1, 1, 0].colors[0])
        count = 0
        while not skip():
            if Aa():
                self.move("X L2 D2 Li Ui L D2 Li U Li Xi")
            elif Ab():
                self.move("Xi L2 D2 L U Li D2 L Ui L X")
            elif caseF():
                self.move("Ri Ui Fi R U Ri Ui Ri F R2 Ui Ri Ui R U Ri U R")
            elif Ga():
                self.move("R2 U Ri U Ri Ui R Ui R2 Ui D Ri U R Di")
            elif Gb():
                self.move("Ri Ui R U Di R2 U Ri U R Ui R Ui R2 D")
            elif Gc():
                self.move("R2 Ui R Ui R U Ri U R2 U Di R Ui Ri D")
            elif Gd():
                self.move("R U Ri Ui D R2 Ui R Ui Ri U Ri U R2 Di")
            elif Ja():
                self.move("X R2 F R Fi R U2 ri U r U2 Xi")
            elif Jb():
                self.move("R U Ri Fi R U Ri Ui Ri F R2 Ui Ri")
            elif Ra():
                self.move("R Ui Ri Ui R U R D Ri Ui R Di Ri U2 Ri")
            elif Rb():
                self.move("R2 F R U R Ui Ri Fi R U2 Ri U2 R")
            elif T():
                self.move("R U Ri Ui Ri F R2 Ui Ri Ui R U Ri Fi")
            elif E():
                self.move("Xi Li U L Di Li Ui L D Li Ui L Di Li U L D X")
            elif Na():
                self.move("R U Ri U R U Ri Fi R U Ri Ui Ri F R2 Ui Ri U2 R Ui Ri")
            elif Nb():
                self.move("Ri U R Ui Ri Fi Ui F R U Ri F Ri Fi R Ui R")
            elif V():
                self.move("Ri U Ri Ui Y Ri Fi R2 Ui Ri U Ri F R F")
            elif caseY():
                self.move("F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi")
            elif H():
                self.move("M2 U M2 U2 M2 U M2")
            elif Ua():
                self.move("M2 U M U2 Mi U M2")
            elif Ub():
                self.move("M2 U M U2 Mi U M2")
            elif caseZ():
                self.move("Mi U M2 U M2 U Mi U2 M2")
            else:
                self.move("U")
            count += 1
            if count >= self.inifinite_loop_max_iterations:
                raise Exception("Stuck in loop - unsolvable cube\n" + str(self.cube))

def adjust_U_face(self):
    count = 0
    while self.cube.is_solved() == False:
        self.move("U")
        count += 1
        if count >= self.inifinite_loop_max_iterations:
            raise Exception("Stuck in loop - unsolvable cube\n" + str(self.cube))
