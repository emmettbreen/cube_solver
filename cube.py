## RUBIX SIMULATOR

# position

corner_cubies = []
corner_cubicles = ["flu", "blu", "bru", "fru", "fld", "bld", "brd", "frd"]

edge_cubies = []
edge_cubicles = ["fu", "lu", "bu", "ru", "fl", "bl", "br", "fr", "fd", "ld", "bd", "rd"]

# orientation

edge_o = []
corner_o = []


## FUNCTIONS

# returns a dictionary of colors to their desired face
# a desired face for a color is where that color is the center cubie
def color_to_face(self):
    colors = ["b", "w", "y", "g", "r", "o"]
    faces = ["f", "u", "b", "d", "l", "r"]
    translator = {}
    for c in colors:
        face = ""
        for f in faces:
            if cube[f][f] == c:
                face = f
        if face = "":
            raise Exception("Invalid Configuration: no " + c + " face found")
        translator[c] = face


# uses json input to fetch colors in each cubicle
def color_in_cubicle(self, cubicle):
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
# the desired colors are the first faces defined in the cubicle (front and back)
def corner_orientation(self, colors):
    for i in range(len(colors)):
        if colors[i] == cube["f"]["f"] || colors[i] == cube["b"]["b"]
            return i

    raise Exception("Invalid Configuration: Incorrect corner piece")

def edge_orientation(self, colors):
    


# returns cubie corresponding to input colors
def cubie_of_color(self, colors):
    cubie = []
    translator = color_to_face()
    for i in colors:
        cubie.append(translator[i])
    return cubie


## PARSE JSON FILE
import json

cube = json.load(open('solved.json',))

# Determines corner cubie positions in corner cubicles

for cubicle in corner_cubicles:
    corner_cubies.append(cubie_of_color(color_in_cubicle(cubicle)))
    corner_o.append(corner_orientation(color_in_cubicle(cubicle)))

# Determines edge cubie positions in edge cubicles
for cubicle in edge_cubicles:
    edge_cubies.append(cubie_of_color(color_in_cubicle(cubicle)))
    edge_cubies.append(edge_orientation(color_in_cubicle(cubicle)))


## TODO: VALID CONFIGURATIONS


## TODO: ROTATIONS