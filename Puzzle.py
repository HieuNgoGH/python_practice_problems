import copy

def is_valid(Board,x,y):
    # check if position is within board
    return x >= 0 and y >= 0 and x < len(Board) and y < len(Board[x]) and Board[x][y] == '-'

def solve_puzzle_helper(Board, x , y, destination, path, visited, paths, LRUD_paths):
    # if moving is not valid
    if not is_valid(Board, x, y):
       return

    if (x, y) not in visited:
        visited.append((x, y))

    # when we reach the destination
    if (x, y) == destination:
        visited_for_copy = copy.copy(visited)
        paths.append(visited_for_copy)
        real_LRUD_copy = copy.copy(path)
        LRUD_paths.append(real_LRUD_copy)
        visited = []
        path = ""
        return

    # check if each direction is a valid move
    if is_valid(Board, x-1, y) and (x-1, y) not in visited:
        visited.append((x-1, y))
        solve_puzzle_helper(Board, x-1, y, destination, path + 'U', visited, paths, LRUD_paths)
        visited.pop()
    if is_valid(Board, x+1, y) and (x+1, y) not in visited:
        visited.append((x+1, y))
        solve_puzzle_helper(Board, x+1, y, destination, path + 'D', visited, paths, LRUD_paths)
        visited.pop()
    if is_valid(Board, x, y-1) and (x, y-1) not in visited:
        visited.append((x, y-1))
        solve_puzzle_helper(Board, x, y-1, destination, path + 'L', visited, paths, LRUD_paths)
        visited.pop()
    if is_valid(Board, x, y+1) and (x, y+1) not in visited:
        visited.append((x, y+1))
        solve_puzzle_helper(Board, x, y+1, destination, path + 'R', visited, paths, LRUD_paths)
        visited.pop()

def solve_puzzle(Board, Source, Destination):
    visited = []
    paths = []
    lrud_paths = []
    shortest_path = ""
    solve_puzzle_helper(Board, Source[0], Source[1], Destination, '', visited, paths, lrud_paths)

    if len(lrud_paths) == 0:
        return

    minimum_length = 9999999
    element_counter = -1
    counter = -1

    # look for the shortest path
    for i in lrud_paths:
        counter += 1
        if len(i) < minimum_length:
            element_counter = counter
            minimum_length = len(i)

    shortest_path_edges = (paths[element_counter])
    shortest_path += lrud_paths[element_counter]

    if len(paths) > 1:
        return (shortest_path_edges, shortest_path)
    else:
        return shortest_path_edges

Puzzle = [
 ['-', '-', '-', '-', '-'],
 ['-', '-', '#', '-', '-'],
 ['-', '-', '-', '-', '-'],
 ['#', '-', '#', '#', '-'],
 ['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0, 2), (2, 2)))
print(solve_puzzle(Puzzle, (0, 0), (4, 4)))
print(solve_puzzle(Puzzle, (0, 0), (4, 0)))
print(solve_puzzle(Puzzle, (0, 0), (0, 0)))