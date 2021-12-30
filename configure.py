## Rubix cube is represented as 8 corner cubies with 3 colors and 12 edge cubies with 2 colors

# position

corner_cubies = []
corner_cubicles = ["ufl", "urf", "ubr", "ulb", "dbl", "dlf", "dfr", "drb"]

edge_cubies = []
edge_cubicles = ["ub", "ur", "uf", "ul", "lb", "rb", "rf", "lf", "db", "dr", "df", "dl"]

# orientation

corner_o = []
edge_o = []

# accpeted colors of cubies

possible_corner_cubies = ["yog","ybo", "yrb", "ygr", "wbr", "wob", "wgo", "wrg"]
possible_edge_cubies = ["wr", "wb", "wo", "wg", "yr", "yb", "yo", "yg", "gr", "rb", "bo", "og"]



## FUNCTIONS


# returns a dictionary of colors to their desired face
# a desired face for a color is where that color is the center cubie
def color_to_face():
    colors = ["b", "w", "y", "g", "r", "o"]
    faces = ["f", "u", "b", "d", "l", "r"]
    translator = {}
    for c in colors:
        face = ""
        for f in faces:
            if cube[f][f] == c:
                face = face + f
        if face == "":
            raise Exception("Invalid Configuration: no " + c + " face")
        elif len(face) > 1:
            raise Exception("Invalid Configuration: multiple " + c + " faces")
        translator[c] = face
    return translator


# uses json input to fetch colors in each cubicle
def color_in_cubicle(cubicle):
    # Returns a list of faces for the current cubicle
    # Example: returns [f, l, u]
    faces = []
    for i in cubicle:
        faces.append(i)

    # Returns a list of colors for the current cubicle
    # Example : returns [w, b, r]
    colors = []
    for i in cubicle:   
        colors.append(cube[i][cubicle])
    return colors


# returns 0 if first face of cubie (defined by the cubicle) has a desired color
# returns 1 if second face of cubie (defined by cubicle) has a desired color
# returns 2 if third face of cubie (defined by cubicle) has a desired color
# the desired colors are the first faces defined in the cubicle (up and down)
# AF: returns number of clockwise twists from having orientation of 0
# AF2: returns the number shown on the "numbered face" of the corner cubie
# Requires: len(colors) = 3
def corner_orientation(colors):
    for i in range(len(colors)):
        if colors[i] == cube["u"]["u"] or colors[i] == cube["d"]["d"]:
            return i

    raise Exception("Invalid Configuration: Incorrect corner piece")


# Requires: len(colors) = 2
def edge_orientation(colors):
    if colors[0] == cube["u"]["u"] or colors[0] == cube["d"]["d"] or colors[1] == cube["b"]["b"] or  colors[1] == cube["f"]["f"] :
      return 0
    return 1


# returns cubie corresponding to input colors
def cubie_of_color(colors):
    cubie = []
    translator = color_to_face()
    for i in colors:
        cubie.append(translator[i])
    return cubie



## PARSE JSON FILE
import json

cube = json.load(open('input.json',))

# Determine corner cubies
for cubicle in corner_cubicles:
    colors = color_in_cubicle(cubicle)
    colors_1 = colors[0] + colors[1] + colors[2]
    colors_2 = colors[1] + colors[2] + colors[0]
    colors_3 = colors[2] + colors[0] + colors[1]

    removed = False
    for i in range(len(possible_corner_cubies)):
        if removed:
            i -= 1
        if possible_corner_cubies[i] == colors_1 or possible_corner_cubies[i] == colors_2 or possible_corner_cubies[i] == colors_3:
            if removed: 
                raise Exception("Invalid Configuration: invalid corner piece")
            possible_corner_cubies.pop(i)
            removed = True
    if not removed:
        raise Exception("Invalid Configuration: corner piece " + colors_1 + " in cubicle " + cubicle + " is not valid")

    corner_cubies.append(cubie_of_color(colors))
    corner_o.append(corner_orientation(colors))

# Determine edge cubies
for cubicle in edge_cubicles:
    colors = color_in_cubicle(cubicle)
    colors_1 = colors[0] + colors[1]
    colors_2 = colors[1] + colors[0]

    removed = False
    for i in range(len(possible_edge_cubies)):
        if removed:
            i -= 1
        if possible_edge_cubies[i] == colors_1 or possible_edge_cubies[i] == colors_2:
            if removed:
                raise Exception("Invalid configuration: Incorrect edge piece")
            possible_edge_cubies.pop(i)
            removed = True
    if not removed:
        raise Exception("Invalid Configuration: invlaid corner piece")

    edge_cubies.append(cubie_of_color(colors))
    edge_cubies.append(edge_orientation(colors))

# Check validity of cubies
if possible_corner_cubies != [] or possible_edge_cubies != []:
    raise Exception("Invalid Configuration: this error should never be thrown")

x = 0
for i in corner_o:
    x += i
if x % 3 != 0:
    raise Exception("Invalid Configuration: The pieces are are valid but the corners are not oriented correctly")

y = 0
for j in edge_o:
    x += j
if y % 2 != 0:
    raise Exception("Invalid Configuration: The pieces are are valid but the edges are not oriented correctly")



## ROTATIONS

# Requires: len(affected_c) == len(affected_e) == 4
# Requires: len(corner_cubies) == len(corner_cubicles) == len(corner_o)
# Requires: len(edge_cubies) == len(edge_cubicles) == len(edge_o)
def rotate(affected_c, affected_e):

    # rotate corner cubie positions and orientations
    temp_c_p = corner_cubies[affected_c[3]]
    temo_c_o = corner_o[affected_c[3]]
    for i in range(len(affected_c) - 2):
        corner_cubies[affected_c[i + 1]] = corner_cubies[affected_c[i]]
        corner_o[affected_c[i + 1]] = corner_o[affected_c[i]]
    corner_cubies[affected_c[0]] = temp_c_p
    corner_o[affected_c[0]] = temp_c_o

    # rotate edge cubie positions and orientations
    temp_e_p = edge_cubies[affected_e[3]]
    temp_e_o = edge_o[affected_e[3]]
    for i in range(len(affected_e) - 2):
        edge_cubies[affected_e[i + 1]] = edge_cubies[affected_e[i]]
        edge_o[affected_e[i + 1]] = edge_o[affected_e[i]]
    edge_cubies[affected_e[0]] = temp_e_p
    edge_o[affected_e[0]] = temp_e_o


def R():
    rotate([6,1,2,7],[1,5,9,6])

def R_pr():
    rotate([7,2,1,6],[6,9,5,1])

def F():
    rotate([0,1,6,5],[2,6,10,7])

def F_pr():
    rotate([5,6,1,0],[7,10,6,2])

def L():
    rotate([0,5,4,3],[3,7,11,4])

def L_pr():
    rotate([3,4,5,0],[4,11,7,3])

def U():
    rotate([0,3,2,1],[0,1,2,3])

def U_pr():
    rotate([1,2,3,0],[3,2,1,0])

def B():
    rotate([3,4,7,2],[0,4,8,5])

def B_pr():
    rotate([2,7,4,3],[5,8,4,0])

def D():
    rotate([6,7,4,5],[11,10,9,8])

def D_pr():
    rotate([5,4,7,6],[8,9,10,11])

