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
    parent = {} 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    
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
    
    return None 

def reconstruct_path(parent, start, end):
    path = []
    while end != start:
        path.append(end)
        end = parent[end]
    path.append(start)
    return path[::-1]  

def print_path_coordinates(path):
    print("Path coordinates:")
    for coord in path:
        print(coord)

def main():
    filename = "maze.txt"
    maze = read_maze_from_file(filename)
    start = find_start(maze)
    
    path = solve_maze_dfs(maze, start)
    
    print_path_coordinates(path)

if __name__ == "__main__":
    main()
