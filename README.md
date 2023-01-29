# Vacuum-Search

This repository contains a python file titled "Vacuum_Problem.py"

The code provides a solution to a simplified version of the Vacuum Search problem, where the vacuum knows its starting point in addition to the location of the obstacles and dust in a 3x6 grid. The vacuum() function takes several variables including a representation of the grid, and the vacuum's starting point. From there, the path that the vacuum must take is calculated backwards, starting in the bottom left corner. So, from the bottom left corner, vacuum() creates a path that visits every cell on the grid, and sucks when the grid has dust on it. Once every cell has been travelled to, a path is then created that leads back to the starting point of the vacuum. Once this complete path is generated, the vacuum travels it in reverse, so that it will properly navigate the grid and end up in the bottom left.

This code does not cover the case where the vacuum does not know its own starting point.
