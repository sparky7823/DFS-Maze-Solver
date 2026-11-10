from Grid import Grid
import sys
import random


def make_grid(filename):
    """
    Parses a maze layout from a text file into a 2D array and initializes
    a Grid state object. Returns the instantiated Grid.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        array = []
        for num in range(len(lines)):
            array.append(list(lines[num].strip()))
        grid = Grid.build(array)
    return grid


def search_from(grid, y, x):
    """
    Executes a recursive Depth-First Search (DFS) backtracking algorithm
    to navigate from current coordinates (x, y) to the exit ('E').
    Marks explored paths and backtracks upon encountering dead ends.
    Returns a boolean indicating path viability.
    """
    if grid.array[y][x]=='E':
        return True
    if x + 1 < len(grid.array[0]) and grid.array[y][x+1]==' ' or grid.array[y][x+1]=='E': # RIGHT
        if not grid.array[y][x+1]=='E':
            grid.array[y][x + 1] = '.'
        if search_from(grid, y, x+1):
            return True
        else:
            grid.array[y][x + 1] = ' '
    if x > 0 and grid.array[y][x-1]==' ' or grid.array[y][x-1]=='E': # LEFT
        if not grid.array[y][x-1]=='E':
            grid.array[y][x - 1] = '.'
        if search_from(grid, y, x-1):
            return True
        else:
            grid.array[y][x - 1] = ' '
    if y + 1 < len(grid.array) and grid.array[y+1][x]==' ' or grid.array[y+1][x]=='E': # DOWN
        #print('Made it to DOWN')
        if not grid.array[y+1][x]=='E':
            #print('Not E')
            grid.array[y + 1][x] = '.'
        if search_from(grid, y+1, x):
            #print('Found it!')
            return True
        else:
            #print('Backtracking')
            grid.array[y + 1][x] = ' '
    if y > 0 and grid.array[y-1][x]==' ' or grid.array[y-1][x]=='E': # UP
        if not grid.array[y-1][x]=='E':
            grid.array[y - 1][x] = '.'
        if search_from(grid, y-1, x):
            return True
        else:
            grid.array[y - 1][x] = ' '
    return False


def solver(filename):
    """
    Locates the starting position ('S') within a parsed grid and initializes
    the recursive pathfinding solver. Outputs the solved maze matrix to the
    console or throws an error if no valid path exists.
    """
    grid = make_grid(filename)

    for y in range(len(grid.array)):
        for x in range(len(grid.array[0])):
            if grid.array[y][x] == 'S':
                try:
                    if search_from(grid, y, x):
                        print('Success! The path is as follows:')
                        for line in grid.array:
                            print(''.join(line))
                    else:
                        print('Error! Solver could find no solution to maze!')
                except Exception as e:
                    print(f'Error! {e}')


def carve(grid, x, y):
    """
    Procedurally generates a randomized maze layout using a recursive backtracking
    algorithm. Modifies the grid matrix in-place by carving paths between structural
    walls and shuffling directional vectors.
    """
    if y == len(grid.array) - 2 and x == len(grid.array[0]) - 2:
        grid.array[y][x] = 'E'
    else:
        grid.array[y][x] = ' '
    # in order:    Right,      Left,       Down,       Up
    directions = [((x+2), y), ((x-2), y), (x, (y+2)), (x, (y-2))]
    random.shuffle(directions)
    for path in directions:
        new_x = path[0]
        new_y = path[1]
        if 1 <= new_x <= (len(grid.array[0]) - 1) and 1 <= new_y <= (len(grid.array) - 1) and grid.array[new_y][new_x] == '#':
            mid_x = int((x + new_x)/2)
            mid_y = int((y + new_y)/2)
            grid.array[mid_y][mid_x] = ' '
            carve(grid, new_x, new_y)


def generate(argvs):
    """
    Validates CLI dimension arguments, initializes a solid grid matrix, and
    invokes the carving algorithm to construct a solvable maze. Writes the
    generated matrix to a specified text file.
    """
    if len(argvs) < 5:
        print('Usage: python3 maze_solver.py [-s filename] [-g width height filename]')
        return
    x, y, filename = int(argvs[2]), int(argvs[3]), argvs[4]

    if x<3 or y<5:
        print('Error! Minimum maze size is 3x5!')
        return

    if x % 2 == 0:
        x += 1
    if y % 2 == 0:
        y += 1

    array = [['#' for column in range(x)] for row in range(y)]
    grid = Grid.build(array)

    carve(grid,1, 1)
    grid.array[1][1] = 'S'
    #grid.array[len(grid.array) - 1][len(grid.array[0]) - 1] = 'E'

    with open(filename, 'w') as file:
        for line in grid.array:
            file.write(f'{''.join(line)}\n')


def main(argvs):
    """
    CLI router. Parses system arguments to execute either the procedural
    generation or recursive solving routines.
    """
    tag = argvs[1]
    if tag == '-s':
        solver(argvs[2])
    elif tag == '-g':
        generate(argvs)


if __name__ == "__main__":
    main(sys.argv)