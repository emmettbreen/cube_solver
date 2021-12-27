## RUBIX SIMULATOR

corner_cubies = []
corner_cubicles = ["flu", "blu", "bru", "fru", "fld", "bld", "brd", "frd"]

edge_cubies = []
edge_cubicles = ["fu", "lu", "bu", "ru", "fl", "bl", "br", "fr", "fd", "ld", "bd", "rd"]

## FUNCTIONS

# rotates cube such that the blue center is in the front
# convention : blue is front, yellow is up, green is back, white is down, left is orange, right is red
def rotate_to_f_b(self):
    if cube['f']['f'] == 'b':
        return cube

# returns cubie corresponding to input colors
# Requires convention: cube['f']['f'] == "b"
def cubie_of_color(self, colors):
    cubie = []
    translator = {"b" : "f", "y" : "u", "g" : "b", "w" : "d", "r" : "r", "o" : "l"}
    for i in colors:
        cubie.append(translator[i])
    return cubie
    
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


## PARSE json file
import json

cube = json.load(open('solved.json',))

# Determines corner cubies in corner cubicles
for cubicle in corner_cubicles:
    corner_cubies.append(cubie_of_color(color_in_cubicle))

# Determines edge cubies in edge cubicles
for cubicle in edge_cubicles:
    edge_cubies.append(cubie_of_color(color_in_cubicle))
