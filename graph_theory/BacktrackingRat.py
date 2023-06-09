from typing import List

# helps print the 2D List : matrix
mprint = lambda matrix: [[[print(item,end=" ") for item in rows],print()] for rows in matrix]

# right-down only solution to the maze        
isReached = False  
def final_solve(
    maze: List[List[int]],      # maze matrix
    solution: List[List[int]],  # solution matrix
    x: int = 0,                 # initial x position
    y: int = 0,                 # initial y position
    xf: int = 3,                # goal x position
    yf: int = 3                 # goal y position
) -> List[List[int]]: 
    global isReached
    if y == yf and x == xf:
        solution[y][x] = 1
        isReached = True
        return solution
    else:
        if y < len(maze) and x+1 < len(maze):
            if maze[y][x+1] == 1 and isReached == False:
                solution[y][x] = 1
                final_solve(maze,solution,x+1,y,xf,yf)
        if y+1 < len(maze) and x < len(maze):
            if maze[y+1][x] == 1 and isReached == False:
                solution[y][x] = 1
                final_solve(maze,solution,x,y+1,xf,yf)
        if isReached == False:
            solution[y][x] = 0
            
# For Debugging        
def printer(x,y,grid,xf=3,yf=3): 
    global isReached
    print("X: {}, Y: {}, G[Y][X]: {}".format(x,y,grid[y][x]))  
    if y == yf and x == xf:
        isReached = True
        print("Reached End")
    elif isReached == False:
        if y < len(grid) and x+1 < len(grid):
            if grid[y][x+1] == 1 and isReached == False:
                printer(x+1,y,grid,xf=xf,yf=yf)
        if y+1 < len(grid) and x < len(grid):
            if grid[y+1][x] == 1 and isReached == False:
                printer(x,y+1,grid,xf=xf,yf=yf)
        if isReached == False:
            print("Reached Else: x: {}, y: {}".format(x,y))          
              
def main():
    maze_matrix =  [[1, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 1, 0, 0],
                    [1, 1, 1, 1]]
    solution_matrix = [[0 for x in range(len(maze_matrix[0]))] for y in range(len(maze_matrix))]
    print("Maze")
    mprint(maze_matrix)
    final_solve(maze_matrix,solution_matrix)
    # printer(0,0,maze_matrix,xf=len(maze_matrix)-2,yf=len(maze_matrix)-1) # debug
    print("Solution")
    mprint(solution_matrix)
    

if __name__ == "__main__":
    main()
