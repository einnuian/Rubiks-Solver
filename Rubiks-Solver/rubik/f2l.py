from rubik import cube

'''Unfinished'''

def first_2_layers(self):
    corner = self.cube.find_piece(self.cube.down_color(), self.cube.left_color(), self.cube.front_color())
    edge = self.cube.find_piece(self.cube.left_color(), self.cube.front_color())

    self._insert_pair(corner, edge)
    self.move("Y")
    self._insert_pair(corner, edge)
    self.move("Y")
    self._insert_pair(corner, edge)
    self.move("Y")
    self._insert_pair(corner, edge)

def _insert_pair(self, corner_piece, edge_piece):
    # 41 Basic cases
    # All F2L pairs will be insert into the FRONT + RIGHT slot (1, 1, 1)
    def correct():
        return (corner_piece.colors[0] == self.cube.right_color() and
            corner_piece.colors[1] == self.cube.down_color() and
            corner_piece.colors[2] == self.cube.front_color() and
            edge_piece.colors[0] == self.cube.right_color() and
            edge_piece.colors[2] == self.cube.front_color())
    
    # Check for correct pair
    if correct():
        return
    
    # Corner piece at y = -1
    if corner_piece.pos.y == -1:
        # Corner piece in correct slot (regardless of orientation)
        if corner_piece.pos == (1, -1, 1):
            # Edge piece on U face
            return
            # Edge piece on E slice
        # Corner piece in incorrect slot (bring piece to (1, 1, 1))
        if corner_piece.pos != (1, -1, 1):
            # BACK + RIGHT slot
            if (corner_piece.pos.x == 1 and corner_piece.pos.z == -1):
                self.move("Ri Ui R U2")
            # FRONT + LEFT slot
            elif (corner_piece.pos.x == -1 and corner_piece.pos.z == 1):
                self.move("Li Ui L")
            # BACK + LEFT slot
            else:
                self.move("L U Li U")
    # Corner piece at y = 1