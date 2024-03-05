
# RUBIK'S SOLVER
#### Video Demo: <https://youtu.be/BVVdIDyP6n4>
#### Description:

This is a web-based application that accepts your scrambled (or not!) Rubik's Cube and returns a solution following the [CFOP method](https://ruwix.com/the-rubiks-cube/advanced-cfop-fridrich/) - the favorite method of the fastest speedcubers in the world! Grab that old, dust-collecting Rubik's Cube on your bookshelf and let the magic begin!

The acronym CFOP stands for Cross - First 2 Layers - Orientation of the Last Layer - Permutation of the Last Layer. As the name suggests, a Rubik's cube at any random state can be solved by
1. Making a cross on the down face,
2. Solving the first two layers (F2L) of the cube (from the bottom up),
3. Orienting the pieces on the last layer (OLL) so that the up face has the same color, and
4. Permuting the pieces on the last layer (PLL) so that the cube is solved.

#### rubik-cube:

The python logic behind the implementation of the Rubik's cube was adapted from the python package [rubik-cube by Paul Glass](https://pypi.org/project/rubik-cube/).

1. **cube.py** together with **maths.py** defines the Classes Pieces and Cube, as well as various methods that allow manipulation of the cube, such as applying turns. Additional moves such as double moves and double-layer moves were added. A scrambler that scrambles the cube following a sequence of moves was also added.

2. **cfop.py** is a modified version of Glass's **solve.py**, which contains all the functions used to solve the Rubik's cube. All 57 OLL and 21 PLL algorithms belonging to CFOP were implemented here. The cube is fixed on the y-axis (can only rotate around the y-axis) through out the entire solve following the standard CFOP solving practice. Other modifications include checking for cases where the 2nd layer is already solved and organizing the solution moves into their respective solving stages (Cross, F2L, OLL, PLL, etc.).

3. **optimize.py** goes through the solution and removes redundant moves (e.g. a clockwise RIGHT turn followed by a counterclockwise RIGHT turn would cancel each other out). Two consecutive identical moves are condensed into one double move per speedsolving notation standards.

4. **oll.py** and **pll.py** contains OLL and PLL algs, respectively. These functions were copied into **cfop.py**. **f2l.py** is an undeveloped file that harbors the unrealized dream of implementing the prestigious and highly intuitive F2L stage.

The new CFOP solver generates solutions with an average move count of 110 moves, reduced from the original 252 moves.

#### Rubik's Solver:
The web app is fairly straightforward. You are greeted with a 2D layout of the Rubik's Cube. The six faces: UP, LEFT, FRONT, BACK, and DOWN are denoted by their initials on the layout.

Once you have a Rubik's Cube in your hand, hold it in a fixed position, where the side facing you is the FRONT face. Fill in each face of the cube on the 2D layout with their corresponding color configuration before submitting the cube. Hit Solve! and let the computer do the hard work for you!

1. **color.js** records color assignments from the user and puts them in a string, which describes the state of the cube. When the user submits the cube, the string is then sent over to the Python backend.

2. **app.py** contains the flask route **/process** which retrieves  and stores the string. When the Solve! button is clicked, **/** recieves a POST request and generates the solution.

3. The "Rubik's Cube Notation" tab takes you to Ruwix's page about Rubik's Cube notation.

