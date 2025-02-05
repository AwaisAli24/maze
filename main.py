def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file]
    return maze

def find_start(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j
    return None

def solve_maze_dfs(maze, start):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    parent = {}  # To reconstruct the path
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    while stack:
        x, y = stack.pop()
        if maze[x][y] == 'E':
            return reconstruct_path(parent, start, (x, y))
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#' and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = (x, y)
    
    return None  # No path found

def reconstruct_path(parent, start, end):
    path = []
    while end != start:
        path.append(end)
        end = parent[end]
    path.append(start)
    return path[::-1]  # Reverse to get correct order

def print_maze_with_path(maze, path):
    for x, y in path[1:-1]:  # Avoid overwriting start and end
        maze[x][y] = '.'
    for row in maze:
        print(''.join(row))

def print_path_coordinates(path):
    print("Path coordinates:")
    for coord in path:
        print(coord)

def main():
    filename = "maze.txt"
    maze = read_maze_from_file(filename)
    start = find_start(maze)
    
    if not start:
        print("Start position not found!")
        return
    
    path = solve_maze_dfs(maze, start)
    
    if path:
        print("Path found:")
        print_maze_with_path(maze, path)
        print_path_coordinates(path)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
