from typing import List

def mprint(
    matrix: List[List[int]]
) -> None:
    for rows in matrix:
        for item in rows:
            print(item,end=" ")
        print()
        
isReached = False  

def final_solve(
    maze: List[List[int]], 
    solution: List[List[int]],
    x: int = 0,
    y: int = 0
) -> List[List[int]]: 
    global isReached
    if y == 3 and x == 3:
        solution[y][x] = 1
        isReached = True
        return solution
    else:
        if y < len(maze) and x+1 < len(maze):
            if maze[y][x+1] == 1 and isReached == False:
                solution[y][x] = 1
                final_solve(maze,solution,x+1,y)
        if y+1 < len(maze) and x < len(maze):
            if maze[y+1][x] == 1 and isReached == False:
                solution[y][x] = 1
                final_solve(maze,solution,x,y+1)
        if isReached == False:
            solution[y][x] = 0
          
def printer(x,y,grid): 
    global isReached
    print("X: {}, Y: {}, G[Y][X]: {}".format(x,y,grid[y][x]))  
    if y == 3 and x == 3:
        isReached = True
        print("Reached End")
    else:
        if y < len(grid) and x+1 < len(grid):
            if grid[y][x+1] == 1 and isReached == False:
                printer(x+1,y,grid)
        if y+1 < len(grid) and x < len(grid):
            if grid[y+1][x] == 1 and isReached == False:
                printer(x,y+1,grid)
        if isReached == False:
            print("Reached Else: x: {}, y: {}".format(x,y))          
              
def main():
    maze_matrix =  [[1, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 1, 0, 0],
                    [1, 1, 1, 1]]
    empty_matrix = [[0 for x in range(len(maze_matrix[0]))] for y in range(len(maze_matrix))]
    mprint(maze_matrix)
    print()
    final_solve(maze_matrix,empty_matrix)
    #printer(0,0,maze_matrix)
    print()
    mprint(empty_matrix)
    

if __name__ == "__main__":
    main()
