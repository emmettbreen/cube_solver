## Rubix cube is represented as 8 corner cubies with 3 colors and 12 edge cubies with 2 colors

# position

corner_cubies = []
corner_cubicles = ["ufl", "urf", "ubr", "ulb", "dbl", "dlf", "dfr", "drb"]

edge_cubies = []
edge_cubicles = ["ub", "ur", "uf", "ul", "lb", "rb", "rf", "lf", "db", "dr", "df", "dl"]

# orientation

corner_o = []
edge_o = []

# accepted colors of cubies

possible_corner_cubies = ["yog","ybo", "yrb", "ygr", "wbr", "wob", "wgo", "wrg"]
possible_edge_cubies = ["wr", "wb", "wo", "wg", "yr", "yb", "yo", "yg", "gr", "rb", "bo", "og"]

# parse json file

import json
cube = json.load(open('input.json',))


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
def corner_cubie_of_color(colors):
    translator = color_to_face()
    cubies = ["ufl", "urf", "ubr", "ulb", "dbl", "dlf", "dfr", "drb"]
    for c in colors:
        face = translator[c]
        removed = 0
        for i in range(len(cubies)):
            i -= removed
            if cubies[i][0] != face and cubies[i][1] != face and cubies[i][2] != face:
                removed += 1
                cubies.pop(i)
    return cubies[0]

def edge_cubie_of_color(colors):
    translator = color_to_face()
    cubies = ["ub", "ur", "uf", "ul", "lb", "rb", "rf", "lf", "db", "dr", "df", "dl"]
    for c in colors:
        face = translator[c]
        removed = 0
        for i in range(len(cubies)):
            i -= removed
            if cubies[i][0] != face and cubies[i][1] != face:
                removed += 1
                cubies.pop(i)
    return cubies[0]


def configure ():
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

        corner_cubies.append(corner_cubie_of_color(colors))
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
            raise Exception("Invalid Configuration: invalid corner piece")

        edge_cubies.append(edge_cubie_of_color(colors))
        edge_o.append(edge_orientation(colors))

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


# Requires: len(affected_c) == len(affected_e) == 4
# Requires: len(corners) == len(corner_cubicles) == len(corner_o)
# Requires: len(edge_cubies) == len(edge_cubicles) == len(edge_o)
def rotate(affected_c, affected_e, c, e, co, eo):
    # rotate corner cubie positions and orientations
    temp_c_p = c[affected_c[3]]
    temp_c_o = co[affected_c[3]]
    for i in range(len(affected_c) - 1):
        c[affected_c[3-i]] = c[affected_c[2-i]]
        co[affected_c[3-i]] = co[affected_c[2-i]]
    c[affected_c[0]] = temp_c_p
    co[affected_c[0]] = temp_c_o

    # rotate edge cubie positions and orientations
    temp_e_p = e[affected_e[3]]
    temp_e_o = eo[affected_e[3]]
    for i in range(len(affected_e) - 1):
        e[affected_e[3-i]] = e[affected_e[2-i]]
        eo[affected_e[3-i]] = eo[affected_e[2-i]]
    e[affected_e[0]] = temp_e_p
    eo[affected_e[0]] = temp_e_o

    return [c, e, co, eo]

# a cube is a list of [corners, edges, corner_o, edge_o, moves] which are all lists
# all moves return a new cube with specified rotation
def R(c):
    c[4].append("R")
    newcube = rotate([6,1,2,7],[1,5,9,6], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def R_pr(c):
    c[4].append("R'")
    newcube = rotate([6,7,2,1],[1,6,9,5], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def F(c):
    c[4].append("F")
    newcube = rotate([0,1,6,5],[2,6,10,7], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def F_pr(c):
    c[4].append("F'")
    newcube = rotate([0,5,6,1],[2,7,10,6], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def L(c):
    c[4].append("L")
    newcube = rotate([0,5,4,3],[3,7,11,4], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def L_pr(c):
    c[4].append("L'")
    newcube = rotate([0,3,4,5],[3,4,11,7], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def U(c):
    c[4].append("U")
    newcube = rotate([0,3,2,1],[0,1,2,3], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def U_pr(c):
    c[4].append("U'")
    newcube = rotate([0,1,2,3],[0,3,2,1], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def B(c):
    c[4].append("B")
    newcube = rotate([3,4,7,2],[0,4,8,5], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def B_pr(c):
    c[4].append("B'")
    newcube = rotate([3,2,7,4],[0,5,8,4], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def D(c):
    c[4].append("D")
    newcube = rotate([6,7,4,5],[11,10,9,8], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def D_pr(c):
    c[4].append("D'")    
    newcube = rotate([6,5,4,7],[11,8,9,10], c[0], c[1], c[2], c[3])
    newcube.append(c[4])
    return newcube

def is_solved(corners, edges):
    #print(corners)
    #print(corner_cubicles)
    for i in range(len(corner_cubicles)):
        #print(corners[i] + " " + corner_cubicles[i])
        if corners[i] != corner_cubicles[i]:
            return False
    for j in range(len(edge_cubicles)):
        #print(edges[j] + " " + edge_cubicles[j])
        if edges[j] != edge_cubicles[j]:
            return False
    return True

def copy(st):
    c = st[0].copy()
    e = st[1].copy()
    co = st[2].copy()
    eo = st[3].copy()
    m = st[4].copy()
    return [c,e,co,eo,m]


## SOLVE

# a state is a list of [corners, edges, corner_o, edge_o, moves] which are all lists
# the queue is a list of states
queue = []
def solve(c):
    queue.append(c)

    while len(queue) > 0 and len(queue[0][4]) <= 20:
        state = queue.pop(0)
        #print(state[4])
        if is_solved(state[0], state[1]):
            return state[4]

        r = R(copy(state))
        queue.append(r)

        r_pr = R_pr(copy(state))
        queue.append(r_pr)

        u = U(copy(state))
        queue.append(u)

        u_pr = U_pr(copy(state))
        queue.append(u_pr)

        f = F(copy(state))
        queue.append(f)

        f_pr = F_pr(copy(state))
        queue.append(f_pr)

        b = B(copy(state))
        queue.append(b)

        b_pr = B_pr(copy(state))
        queue.append(b_pr)

        d = D(copy(state))
        queue.append(d)

        d_pr = D_pr(copy(state))
        queue.append(d_pr)

        l = L(copy(state))
        queue.append(l)

        l_pr = L_pr(copy(state))
        queue.append(l_pr)

    return ["a problem occured"]


## run functions

valid = True
try:
    print("configuring cube...\n")
    configure()
except Exception as message:
    valid = False
    print(message.args)

if valid:
    print("Beginning solve....\n")
    #print(corner_cubies)
    #print(edge_cubies)
    solution = solve([corner_cubies, edge_cubies, corner_o, edge_o, []])
    print("Solution found with " + (str)(len(solution)) + " moves!\n")
    for i in solution:
        print(i)

