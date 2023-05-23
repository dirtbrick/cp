import typing
maze_matrix = [[1, 0, 0, 0],
               [1, 1, 1, 1],
               [0, 1, 0, 0],
               [1, 1, 1, 1]]

solution_matrix = [[0 for x in range(len(maze_matrix[0]))]for y in range(len(maze_matrix))]
x = 1
y = 0
# cur = (y,x), end = (y,x)
def recur_solve(coord: typing.List[int], endpt: int) -> bool:
    try:
        right = maze_matrix[coord[y]][coord[x]+1]
    except:
        right = 0
    try:
        down = maze_matrix[coord[y]+1][coord[x]]
    except:
        down = 0
    try:
        solution_matrix[coord[y]][coord[x]] = 1
    except:
        pass
    print("(y,x):",coord[y],coord[x])
    print("r:",right)
    print("d:",down)
    isDead = True if right == 0 and down == 0 else False
    if isDead:
        print("Dead at:",coord[y],coord[x])
        try:
            solution_matrix[coord[y]][coord[x]] = 0
        except:
            return False
    elif right == 1:
        if not recur_solve((coord[y],coord[x]+1),endpt):
            return recur_solve((coord[y]+1,coord[x]),endpt)
    elif down == 1:
        return recur_solve((coord[y]+1,coord[x]),endpt)
    
def mprint(matrix: typing.List[typing.List[int]]) -> None:
    for rows in matrix:
        for item in rows:
            print(item,end=" ")
        print()
                    
def main():
    recur_solve([0,0],[3,3])
    print()
    mprint(maze_matrix)
    print()
    mprint(solution_matrix)

if __name__ == "__main__":
    main()
