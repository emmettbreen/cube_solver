# Cube Solver

Phase: In development

This project is capable of solving any traditional 3x3 rubix cube. It is currently a purely backend piece of code that uses jsons as input and the terminal as output. As-is, the Python code:

- takes in a json file with specified colors on each face
- configures a backend model that translates the color inputs to a functional rubix cube
- confirms whether the configuration is valid
- (currently) uses a brute force algorithm in a breadth-first-search style to return the needed rotations to solve the cube
  - due to the exponential nature of rubix cube configurations, the algorithm is only quick at solving scrambles of < 5 moves


My main takeaways from this project were:

- self-taught group theory and abstract algebra topics to model the nature of the cube
- NP complete problems and nondeterministic brute force solutions as a starting point to begin optimizing

Next Steps:
- create a frontend to make the input of colors more visual, possibly using Python GUIs or Javascript/Node
- optimize thr backend using pruning techniques to make the algorithm useful for any scramble

Json Inputs:

<img width="150" height = "600" src="https://user-images.githubusercontent.com/90010213/147861550-fa9141ed-304f-426b-818f-9e14e502ec47.png">


Terminal Output:

<img width="450" height="400" src="https://user-images.githubusercontent.com/90010213/147861559-1c2c6a25-efb4-4ef4-8109-b29821a77068.png">
