#Author: Bruce Chidley, 20104323

from copy import deepcopy

#traversal() requires the following:
#grid: This should always remain main_grid from the main() function
#marked_grid: This starts out as main_marked_grid from main(), 0's are changed to 1's on every call to indicate that the vacuum has been in that cell
#current_position: Tracks the current position the function is analyzing
#total_stack: Represents positions that have been travelled to. Items will be popped off if the vacuum needs to backtrack
#path_stack: Represents directions that have been travelled. Items will be popped off and appended to path if the vacuum needs to backtrack
#path: Represents the total path travelled by the vacuum (in reverse order)
#is_complete: Boolean variable that keeps track of whether the problem is complete or not
#robo_position: This should always remain robo_position from main(). Does not change
#robo_search: Boolean variable that represents whether we are searching for the vacuum after traversing all cells

#traversal() returns the current position of the vacuum and the path travelled in the form of a list
def traversal(grid, marked_grid, current_position, total_stack, path_stack, path, is_complete, robo_position, robo_search):

    while (not is_complete):

        #Performs the "Suck" function when the vacuum would reach a cell that has dust on it
        #Only executes if cells are being traversed for the first time
        if (not robo_search):
            if (grid[current_position[0]][current_position[1]] == 2):
                path.append("Suck!")

        #If an up move is possible, and the cell has not been travelled to, move up
        if ((current_position[0] - 1 >= 1) and (marked_grid[current_position[0] - 1][current_position[1]] == 0)):
            if (not (grid[(current_position[0] - 1)][(current_position[1])] == 1)):
                total_stack.append(current_position)
                new_dest = [current_position[0] - 1, current_position[1]]
                new_marked_grid = deepcopy(marked_grid)
                new_marked_grid[current_position[0] - 1][current_position[1]] = 1

                #If we have found the vacuum after traversing all cells, exit the loop
                if (robo_search == True and robo_position == new_dest):
                    is_complete = True

                #If all cells have been traversed, exit the loop
                if (not(any(0 in sublist for sublist in new_marked_grid))):
                    is_complete = True

                path.append("Up")
                path_stack.append("Up")
                return traversal (grid, new_marked_grid, new_dest, total_stack, path_stack, path, is_complete, robo_position, robo_search)

        #If a down move is possible, and the cell has not been travelled to, move down
        elif ((current_position[0] + 1 <= 3) and (marked_grid[current_position[0] + 1][current_position[1]] == 0)):
            if (not(grid[(current_position[0] + 1)][(current_position[1])] == 1)):
                total_stack.append(current_position)
                new_dest = [current_position[0] + 1, current_position[1]]
                new_marked_grid = deepcopy(marked_grid)
                new_marked_grid[current_position[0] + 1][current_position[1]] = 1


                if (robo_search == True and robo_position == new_dest):
                    is_complete = True

                if (not(any(0 in sublist for sublist in new_marked_grid))):
                    is_complete = True

                path.append("Down")
                path_stack.append("Down")
                return traversal (grid, new_marked_grid, new_dest, total_stack, path_stack, path, is_complete, robo_position, robo_search)

        #If a right move is possible, and the cell has not been travelled to, move right
        elif ((current_position[1] + 1 <= 6)) and (marked_grid[current_position[0]][current_position[1] + 1] == 0):
            if (not(grid[(current_position[0])][(current_position[1] + 1)] == 1)):
                total_stack.append(current_position)
                new_dest = [current_position[0], current_position[1] + 1]
                new_marked_grid = deepcopy(marked_grid)
                new_marked_grid[current_position[0]][current_position[1] + 1] = 1


                if (robo_search == True and robo_position == new_dest):
                    is_complete = True

                if (not(any(0 in sublist for sublist in new_marked_grid))):
                    is_complete = True

                path.append("Right")
                path_stack.append("Right")
                return traversal (grid, new_marked_grid, new_dest, total_stack, path_stack, path, is_complete, robo_position, robo_search)

        #If a left move is possible, and the cell has not been travelled to, move left
        elif ((current_position[1] - 1 >= 1) and (marked_grid[current_position[0]][current_position[1] - 1] == 0)):
            if (not(grid[(current_position[0])][(current_position[1] - 1)] == 1)):
                total_stack.append(current_position)
                new_dest = [current_position[0], current_position[1] - 1]
                new_marked_grid = deepcopy(marked_grid)
                new_marked_grid[current_position[0]][current_position[1] - 1] = 1

                if (robo_search == True and robo_position == new_dest):
                    is_complete = True

                if (not(any(0 in sublist for sublist in new_marked_grid))):
                    is_complete = True

                path.append("Left")
                path_stack.append("Left")
                return traversal (grid, new_marked_grid, new_dest, total_stack, path_stack, path, is_complete, robo_position, robo_search)

        #This "else" branch is entered when all adjacent cells are either blocked or have been travelled to already
        #Implies that the vacuum must backtrack
        else:

            #Loops while there are no adjacent squares that have not been travelled to
            while ((marked_grid[current_position[0]-1][current_position[1]] == 1)
                    and (marked_grid[current_position[0]+1][current_position[1]] == 1)
                    and (marked_grid[current_position[0]][current_position[1]+1] == 1)
                    and (marked_grid[current_position[0]][current_position[1]-1] == 1)):

                #Vacuum moves backwards
                current_position = total_stack.pop()
                
                direction = path_stack.pop()

                #Reverses the previous move direction and appends it to path
                if (direction == "Up"):
                    path.append("Down")
                if (direction == "Down"):
                    path.append("Up")
                if (direction == "Right"):
                    path.append("Left")
                if (direction == "Left"):
                    path.append("Right")

            #Updates values for next function call
            new_dest = current_position
            new_marked_grid = deepcopy(marked_grid)

            return traversal (grid, new_marked_grid, new_dest, total_stack, path_stack, path, is_complete, robo_position, robo_search)

    #Accounts for if the traversal ends on a location with dust
    if (not robo_search):
            if (grid[current_position[0]][current_position[1]] == 2):
                path.append("Suck!")

    return [current_position, path]

#vacuum() requires all variables declared in main()
#Returns a complete path in the form of a list
def vacuum(main_grid, main_marked_grid, position, position_stack, main_path_stack, path_list, complete, robo_position, robo_search):

    #Begins at the bottom left and finds a path that visits every cell
    initial_search = traversal(main_grid, main_marked_grid, position, position_stack, main_path_stack, path_list, complete, robo_position, robo_search)
    
    #Initializes a new starting position and sets robo_search to true, indicating that we will now find a path from the endpoint of the previous function call to the vacuum
    position = initial_search[0]
    initial_path = initial_search[1]
    robo_search = True

    #Re-creates some variables so that a similar second search may occur
    new_position_stack = [position]
    new_main_path_stack = []
    path_list = []
    #Must be set to 0 to account for when the vacuum is in the bottom left position
    main_marked_grid[3][1] = 0
    
    #Returns the end position and path travelled from the previous endpoint to the vacuum's starting position
    robo_hunt = traversal(main_grid, main_marked_grid, position, new_position_stack, new_main_path_stack, path_list, complete, robo_position, robo_search)
    robo_path = robo_hunt[1]
    #Appends the two paths together to create a complete path the robot will take
    total_path = initial_path + robo_path
    #Must reverse the path since it was calculated in reverse
    total_path.reverse()

    final_path = []

    #Since the problem was done backwards, all moves must be reversed as well
    for move in total_path:
        if (move == "Up"):
            final_path.append("Down")
        elif (move == "Down"):
            final_path.append("Up")
        elif (move == "Left"):
            final_path.append("Right")
        elif (move == "Right"):
            final_path.append("Left")
        elif (move == "Suck!"):
            final_path.append("Suck!")

    return final_path


def main():

    #main_grid represents the grid in which the vacuum moves and cleans.
    #It is 3x6 with an added perimeter of 1's to represent the "walls"
    #0's represent empty cells, 1's represent obstacles, and 2's represent dust
    #This can be edited by the user to simulate different environments
    main_grid = [
                [1,1,1,1,1,1,1,1],
                [1,0,0,2,1,2,0,1],
                [1,2,1,1,1,0,0,1],
                [1,0,0,0,0,0,2,1],
                [1,1,1,1,1,1,1,1]
                ]

    #main_marked_grid is used to keep track of where the robot has travelled
    #It should always be an exact copy of the main_grid, except all 2's are changed to 0's, and the bottom left cell is changed to 1
    main_marked_grid = [
                [1,1,1,1,1,1,1,1],
                [1,0,0,0,1,0,0,1],
                [1,0,1,1,1,0,0,1],
                [1,1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1]
                ]
    
    #robo_position represents the start point for the autonomous vacuum cleaner
    #This can be changed by the user to simulate different scenarios
    robo_position = [1,6]

    #Set of preconditins for the function call that must remain unchanged
    complete = False
    robo_search = False
    position = [3,1]
    position_stack = [3,1]
    main_path_stack = []
    path_list = []

    #Function call
    vacuum_path = vacuum(main_grid, main_marked_grid, position, position_stack, main_path_stack, path_list, complete, robo_position, robo_search)
    print ("Robot's Path:")
    print(vacuum_path)

main()