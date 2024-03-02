import os, sys
# Relative path to current directory
sys.path.append(os.path.join(os.path.dirname(__file__), "rubik"))
#sys.path.insert(0, <path>)

from flask import Flask, render_template, request, redirect
import cube
from cfop import Solver
from optimize import optimize_moves

from helpers import apology

# Configure application
app = Flask(__name__)

list=[] # Global list to store state of cube

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        print(list)
        cube_str = list[0] # Assign the state of cube to cube_str
        if len(cube_str) != 54: #Check for invalid input
            return apology("Can't solve cube")

        c = cube.Cube(cube_str) #Generate the cube
        solver = Solver(c) # Create solver class
        try:
            solver.solve() # Solve the cube
        except Exception:
            return apology("Can't solve cube")
        solver.moves = optimize_moves(solver.moves) # Optimize the solution
        SOL = {} # empty dictionary to store solution by step
        steps = ("Cross", "Cross corners", "2nd Layer", "OLL", "PLL", "AUF")
        for i in range(6):
            a = solver.moves.index(str(i))
            b = solver.moves.index(str(i+1))
            s = ""
            for item in solver.moves[a+1:b]:
                s = s + item + " "
            SOL[steps[i]] = s
        count = len(solver.moves)-7 # total move count
        return render_template("solution.html", cube_str = cube_str, sol = SOL, count = count)
    else:
        return render_template("index.html")

# Function to process ajax post request from javascript
@app.route("/process", methods=["POST"])
def process():
    if request.method == 'POST':
        print(request.form)
        cube=request.form.get('value')
        del list[:] # Clear list before appending the new cube
        list.append(cube)
        print(list)
        return ('', 204) # Mark an http success code response, stay on the same page

# Information regarding cube notation
@app.route("/notation", methods=["GET"])
def notation():
    # Redirect to Ruwix site for cube notation
    return redirect("https://ruwix.com/the-rubiks-cube/notation/", code=302)

