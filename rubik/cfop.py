import cube
from maths import Point
from optimize import optimize_moves

DEBUG = False


class Solver:

    def __init__(self, c):
        self.cube = c
        self.colors = c.colors()
        self.moves = []

        # These four attributes are used for the cross only
        self.left_piece  = self.cube.find_piece(self.cube.left_color())
        self.right_piece = self.cube.find_piece(self.cube.right_color())
        self.front_piece = self.cube.find_piece(self.cube.front_color())
        self.back_piece  = self.cube.find_piece(self.cube.back_color())

        self.inifinite_loop_max_iterations = 12

    def solve(self):
        self.moves.extend("0")
        if DEBUG: print(self.cube)
        self.cross()
        self.moves.extend("1")
        if DEBUG: print('Cross:\n', self.cube)
        self.cross_corners()
        self.moves.extend("2")
        if DEBUG: print('Corners:\n', self.cube)
        self.second_layer()
        self.moves.extend("3")
        if DEBUG: print('Second layer:\n', self.cube)
        self.orientation_last_layer()
        self.moves.extend("4")
        if DEBUG: print('Last layer orientation:\n', self.cube)
        self.permutation_last_layer()
        self.moves.extend("5")
        if DEBUG: print('Last layer permutation:\n', self.cube)
        self.adjust_U_face()
        self.moves.extend("6")
        if DEBUG: print('Adjust U face:\n', self.cube)
        #self.solution() # this line prints out the solution and the move count

    def move(self, move_str):
        # extend() is similar to append()? Add move_str to self.moves
        # each time that the method move() is called, the moves will be append to self.moves
        # while sequence() will apply the moves to the cube
        self.moves.extend(move_str.split())
        self.cube.sequence(move_str)

    def solution(self):
        steps = ("Cross:", "Cross corners:", "2nd Layer:", "OLL:", "PLL:", "AUF:")
        self.moves = optimize_moves(self.moves)
        for i in range(6):
            a = self.moves.index(str(i))
            b = self.moves.index(str(i+1))
            s = ""
            for item in self.moves[a+1:b]:
                s = s + item + " "
            print(steps[i], s)
        print("Total move count:", len(self.moves)-7)

    # Solving cross
    # Put cross in the DOWN face (rotate the cube X')
    # Apply X' to all moves in the code below (modifying the original code)
    def cross(self):
        if DEBUG: print("cross")
        # place the UP-LEFT piece
        # Find the positions of the four cross pieces by passing in the two colors of each piece
        l_piece = self.cube.find_piece(self.cube.down_color(), self.cube.left_color())
        r_piece = self.cube.find_piece(self.cube.down_color(), self.cube.right_color())
        b_piece = self.cube.find_piece(self.cube.down_color(), self.cube.back_color())
        f_piece = self.cube.find_piece(self.cube.down_color(), self.cube.front_color())

        # The way this work, example l_piece:
        # align l_piece so it is LEFT + UP, which is 180 degree (L2) away from self.left_piece (the correct position)
        # if the orientation is correct, do move_1 ("L L"), if not, do move_2 ("Si L S Li")
        self._cross_left_or_right(l_piece, self.left_piece, self.cube.left_color(), "L L", "Si L S Li")
        self._cross_left_or_right(r_piece, self.right_piece, self.cube.right_color(), "R R", "S R Si Ri")

        # Rotate the cube clockwise along the z-axis to solve the remaining two cross pieces
        self.move("Yi")
        self._cross_left_or_right(b_piece, self.back_piece, self.cube.left_color(), "L L", "Si L S Li")
        self._cross_left_or_right(f_piece, self.front_piece, self.cube.right_color(), "R R", "S R Si Ri")
        # Undo rotation
        self.move("Y")
        # Copy the moves so far into self.cross_moves?
        self.cross_moves = self.moves

    def _cross_left_or_right(self, edge_piece, face_piece, face_color, move_1, move_2):
        # don't do anything if piece is in correct place: the piece is in the correct plane and correct color
        if (edge_piece.pos == (face_piece.pos.x, -1, face_piece.pos.z)
                and edge_piece.colors[1] == self.cube.down_color()):
            return

        # ensure piece is at y = 1
        undo_move = None
        if edge_piece.pos.y == 0: # Cross piece in E slice
            pos = Point(edge_piece.pos)
            pos.x = 0  # pick the FRONT or BACK face
            # When x = 0 and y = 0, POINT(0, 0, z) = FRONT or BACK (see line 9 in cube.py)
            # The purpose of assigning pos.x = 0 is so when pos is passed
            # get_rot_from_face() returns the pair of CW and CC moves (ie. 'L', 'Li' where cw = L & cc = Li)
            cw, cc = cube.get_rot_from_face(pos)

            if edge_piece.pos in (cube.LEFT + cube.FRONT, cube.RIGHT + cube.BACK):
                # cube.LEFT + cube. FRONT would give POINT(-1, 0, 1)
                self.move(cw) # This move would bring the piece to y = 1 (UP face)
                undo_move = cc
            else:
                self.move(cc)
                undo_move = cw
        elif edge_piece.pos.y == -1: # Cross piece in the 1st layer
            pos = Point(edge_piece.pos)
            pos.y = 0 # RIGHT or LEFT or FRONT or BACK. ie. if edge_piece.pos is FRONT+DOWN, setting pos.y to 0 means pos = FRONT
            cw, cc = cube.get_rot_from_face(pos)
            # "{0} {0}".format("L") = "L L" -> do the move twice to bring the piece to y = 1
            self.move("{0} {0}".format(cc))
            # don't set the undo move if the piece starts out in the right position
            # (with wrong orientation) or we'll screw up the remainder of the algorithm
            if edge_piece.pos.x != face_piece.pos.x:
                undo_move = "{0} {0}".format(cw)

        assert edge_piece.pos.y == 1

        # piece is at y = 1, do U turns until piece is aligned with either LEFT or RIGHT
        # set up for move_1/move_2 later on
        count = 0
        while (edge_piece.pos.x, edge_piece.pos.z) != (face_piece.pos.x, face_piece.pos.z):
            self.move("U")
            count += 1
            if count >= self.inifinite_loop_max_iterations:
                raise Exception("Stuck in loop - unsolvable cube?\n" + str(self.cube))

        # if we moved a correctly-placed piece, restore it
        if undo_move:
            self.move(undo_move)

        # the piece is on the correct face on plane y = 1, but has two orientations
        if edge_piece.colors[0] == face_color:
            # the cross piece is correctly oriented so L2 or R2
            self.move(move_1)
        else:
            # move_2 does the same thing as move_1 but for flipped pieces (incorrect orientation)
            self.move(move_2)

    def cross_corners(self):
        if DEBUG: print("cross_corners")
        dlb_piece = self.cube.find_piece(self.cube.down_color(), self.cube.left_color(), self.cube.back_color())
        dlf_piece = self.cube.find_piece(self.cube.down_color(), self.cube.left_color(), self.cube.front_color())
        drb_piece = self.cube.find_piece(self.cube.down_color(), self.cube.right_color(), self.cube.back_color())
        drf_piece = self.cube.find_piece(self.cube.down_color(), self.cube.right_color(), self.cube.front_color())

        self.place_drb_corner(drb_piece, self.right_piece, self.back_piece, self.cube.down_color())
        self.move("Yi")
        self.place_drb_corner(drf_piece, self.front_piece, self.right_piece, self.cube.down_color())
        self.move("Yi")
        self.place_drb_corner(dlf_piece, self.left_piece, self.front_piece, self.cube.down_color())
        self.move("Yi")
        self.place_drb_corner(dlb_piece, self.back_piece, self.left_piece, self.cube.down_color())
        self.move("Yi")

    def place_drb_corner(self, corner_piece, right_piece, back_piece, down_color):
        # rotate to y = 1
        if corner_piece.pos.y == -1: # corner piece on the DOWN FACE
            pos = Point(corner_piece.pos)
            pos.x = pos.y = 0 # set up to get F or B rotation (z can only be -1 or 1)
            cw, cc = cube.get_rot_from_face(pos)

            # be careful not to screw up other pieces on the down face
            count = 0
            undo_move = cc
            while corner_piece.pos.y != 1:
                self.move(cw)
                count += 1

            if count > 1:
                # undo moves and turn the other direction
                # so that the cross pieces and other correct corners don't end up on the UP face (y = 1)
                # similar to what I call "if the piece is wrong, take it out" when solving first layer
                for _ in range(count):
                    self.move(cc) # undo moves

                # now turn the other direction
                count = 0
                while corner_piece.pos.y != 1:
                    self.move(cc)
                    count += 1
                undo_move = cw
            # do U turn to move the piece out of the first layer
            # then undo the set up move (that was executed above)
            self.move("U")
            for _ in range(count):
                self.move(undo_move)

        # rotate piece to be directly above its destination
        while (corner_piece.pos.x, corner_piece.pos.z) != (right_piece.pos.x, back_piece.pos.z):
            self.move("U")

        # there are three possible orientations for a corner
        if corner_piece.colors[0] == down_color:
            self.move("U B Ui Bi")
        elif corner_piece.colors[2] == down_color:
            self.move("Ui Ri U R")
        else:
            self.move("Ri U2 R Ui Ui B Ui Bi")

    def second_layer(self):
        rb_piece = self.cube.find_piece(self.cube.right_color(), self.cube.back_color())
        rf_piece = self.cube.find_piece(self.cube.right_color(), self.cube.front_color())
        lb_piece = self.cube.find_piece(self.cube.left_color(), self.cube.back_color())
        lf_piece = self.cube.find_piece(self.cube.left_color(), self.cube.front_color())

        self.place_middle_layer_lb_edge(lb_piece, self.cube.left_color(), self.cube.back_color())
        self.move("Yi")
        self.place_middle_layer_lb_edge(rb_piece, self.cube.left_color(), self.cube.back_color())
        self.move("Yi")
        self.place_middle_layer_lb_edge(rf_piece, self.cube.left_color(), self.cube.back_color())
        self.move("Yi")
        self.place_middle_layer_lb_edge(lf_piece, self.cube.left_color(), self.cube.back_color())
        self.move("Yi")

    def place_middle_layer_lb_edge(self, lb_piece, left_color, back_color):
        # move to y == 1
        if lb_piece.pos.y == 0: # edge piece on E slice
            count = 0
            # Rotate cube so that the edge piece ends up on BACK + LEFT
            while (lb_piece.pos.x, lb_piece.pos.z) != (-1, -1):
                self.move("Yi")
                count += 1

            # Check if the piece is in the correct slot with the correct orientation
            if (lb_piece.colors[0] == self.cube.left_color() and
               lb_piece.colors[2] == self.cube.back_color()):
               return
            else:
            # Take the edge piece out of the second layer
            # After this alg, the piece ends up at UP + FRONT
                self.move("U L Ui Li Ui Bi U B")
                for _ in range(count):
                    self.move("Y")

        assert lb_piece.pos.y == 1

        # Two orientations of the edge piece
        if lb_piece.colors[1] == left_color:
            # left_color is on the up face, U turn to move piece to back face
            while lb_piece.pos.z != -1:
                self.move("U")
            self.move("U L Ui Li Ui Bi U B")
        elif lb_piece.colors[1] == back_color:
            # back_color is on the up face, U turn to move to left face
            while lb_piece.pos.x != -1:
                self.move("U")
            self.move("Ui Bi U B U L Ui Li")
        else:
            raise Exception("BUG!!")

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
if __name__ == '__main__':
    DEBUG = True
    c = cube.Cube("DLURRDFFUBBLDDRBRBLDLRBFRUULFBDDUFBRBBRFUDFLUDLUULFLFR")
    print("Solving:\n", c)
    orig = cube.Cube(c)
    solver = Solver(c)
    solver.solve()

    print(f"{len(solver.moves)} moves: {' '.join(solver.moves)}")

    check = cube.Cube(orig)
    check.sequence(" ".join(solver.moves))
    assert check.is_solved()
