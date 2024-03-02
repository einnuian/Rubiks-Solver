import cube

def orientation_last_layer(self):

        # 57 OLL cases: https://jperm.net/algs/oll
        # all eight cubies in order of left to right, up to down except the face_piece
        def case0(): # OLL skip
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case1():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case2():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case3():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case4():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case5():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case6():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case7():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case8():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case9():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case10():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case11():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case12():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case13():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case14():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case15():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case16():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case17():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case18():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case19():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case20():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case21():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case22():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case23():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case24():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case25():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case26():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case27():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case28():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case29():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case30():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case31():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case32():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case33():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case34():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case35():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case36():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case37():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case38():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case39():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case40():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case41():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case42():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case43():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case44():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case45():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        def case46():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case47():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case48():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case49():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case50():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case51():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case52():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case53():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case54():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case55():
            return (self.cube[-1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[2] == self.cube.up_color())

        def case56():
            return (self.cube[-1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[0] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[0] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[0] == self.cube.up_color())

        def case57():
            return (self.cube[-1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, -1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, -1].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[1, 1, 0].colors[1] == self.cube.up_color() and
                    self.cube[-1, 1, 1].colors[1] == self.cube.up_color() and
                    self.cube[0, 1, 1].colors[2] == self.cube.up_color() and
                    self.cube[1, 1, 1].colors[1] == self.cube.up_color())

        count = 0
        while not case0():
            if case1():
                self.move("R U2 R2 F R Fi U2 Ri F R Fi")
            elif case2():
                self.move("r U ri U2 r U2 Ri U2 R Ui ri")
            elif case3():
                self.move("ri R2 U Ri U r U2 ri U Mi")
            elif case4():
                self.move("M Ui r U2 ri Ui R Ui Ri Mi")
            elif case5():
                self.move("li U2 L U Li U l")
            elif case6():
                self.move("r U2 Ri Ui R Ui ri")
            elif case7():
                self.move("r U Ri U R U2 ri")
            elif case8():
                self.move("li Ui L Ui Li U2 l")
            elif case9():
                self.move("R U Ri Ui Ri F R2 U Ri Ui Fi")
            elif case10():
                self.move("R U Ri U Ri F R Fi R U2 Ri")
            elif case11():
                self.move("r U Ri U Ri F R Fi R U2 ri")
            elif case12():
                self.move("Mi Ri Ui R Ui Ri U2 R Ui R ri")
            elif case13():
                self.move("F U R Ui R2 Fi R U R Ui Ri")
            elif case14():
                self.move("Ri F R U Ri Fi R F Ui Fi")
            elif case15():
                self.move("li Ui l Li Ui L U li U l")
            elif case16():
                self.move("r U ri R U Ri Ui r Ui ri")
            elif case17():
                self.move("F Ri Fi R2 ri U R Ui Ri Ui Mi")
            elif case18():
                self.move("r U Ri U R U2 r2 Ui R Ui Ri U2 r")
            elif case19():
                self.move("ri R U R U Ri Ui Mi Ri F R Fi")
            elif case20():
                self.move("r U Ri Ui M2 U R Ui Ri Ui Mi")
            elif case21():
                self.move("R U2 Ri Ui R U Ri Ui R Ui Ri")
            elif case22():
                self.move("R U2 R2 Ui R2 Ui R2 U2 R")
            elif case23():
                self.move("R2 Di R U2 Ri D R U2 R")
            elif case24():
                self.move("r U Ri Ui ri F R Fi")
            elif case25():
                self.move("Fi r U Ri Ui ri F R")
            elif case26():
                self.move("R U2 Ri Ui R Ui Ri")
            elif case27():
                self.move("R U Ri U R U2 Ri")
            elif case28():
                self.move("r U Ri Ui ri R U R Ui Ri")
            elif case29():
                self.move("R U Ri Ui R Ui Ri Fi Ui F R U Ri")
            elif case30():
                self.move("F Ri F R2 Ui Ri Ui R U Ri F2")
            elif case31():
                self.move("Ri Ui F U R Ui Ri Fi R")
            elif case32():
                self.move("L U Fi Ui Li U L F Li")
            elif case33():
                self.move("L U Fi Ui Li U L F Li")
            elif case34():
                self.move("R U R2 Ui Ri F R U R Ui Fi")
            elif case35():
                self.move("R U R2 Ui Ri F R U R Ui Fi")
            elif case36():
                self.move("Li Ui L Ui Li U L U L Fi Li F")
            elif case37():
                self.move("F Ri Fi R U R Ui Ri")
            elif case38():
                self.move("R U Ri U R Ui Ri Ui Ri F R Fi")
            elif case39():
                self.move("L Fi Li Ui L U F Ui Li")
            elif case40():
                self.move("Ri F R U Ri Ui Fi U R")
            elif case41():
                self.move("R U Ri U R U2 Ri F R U Ri Ui Fi")
            elif case42():
                self.move("Ri Ui R Ui Ri U2 R F R U Ri Ui Fi")
            elif case43():
                self.move("Fi Ui Li U L F")
            elif case44():
                self.move("F U R Ui Ri Fi")
            elif case45():
                self.move("F U R Ui Ri Fi")
            elif case46():
                self.move("Ri Ui Ri F R Fi U R")
            elif case47():
                self.move("Ri Ui Ri F R Fi U R")
            elif case48():
                self.move("F R U Ri Ui R U Ri Ui Fi")
            elif case49():
                self.move("r Ui r2 U r2 U r2 Ui r")
            elif case50():
                self.move("ri U r2 Ui r2 Ui r2 U ri")
            elif case51():
                self.move("F U R Ui Ri U R Ui Ri Fi")
            elif case52():
                self.move("R U Ri U R Ui B Ui Bi Ri")
            elif case53():
                self.move("li U2 L U Li Ui L U Li U l")
            elif case54():
                self.move("r U2 Ri Ui R U Ri Ui R Ui ri")
            elif case55():
                self.move("Ri F R U R Ui R2 Fi R2 Ui Ri U R U Ri")
            elif case56():
                self.move("ri Ui r Ui Ri U R Ui Ri U R ri U r")
            elif case57():
                self.move("R U Ri Ui Mi U R Ui ri")
            else:
                # Do U turn if none match
                self.move("U")
            count += 1
            if count >= self.inifinite_loop_max_iterations:
                raise Exception("Stuck in loop - unsolvable cube\n" + str(self.cube))
