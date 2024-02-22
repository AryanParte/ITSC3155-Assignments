from collections import deque
import heapq

# Example grid with walls
example_grid = [
    ['S', '2', '1', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '.', '#', '.', '.', '.', '.'],
    ['3', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '5', '4', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '7', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '8', '6', '#', '.', '.', '.', 'G']
]

grid_rows, grid_columns = len(example_grid), len(example_grid[0])
grid = [['*' for _ in range(grid_columns)] for _ in range(grid_rows)]

start_point, goal_point = None, None
for i in range(grid_rows):
    for j in range(grid_columns):
        grid[i][j] = example_grid[i][j] if example_grid[i][j] in ['#', 'S', 'G'] else '*'
        if example_grid[i][j] == 'S':
            start_point = (i, j)
        elif example_grid[i][j] == 'G':
            goal_point = (i, j)

algorithm = input("Enter the search algorithm (DFS/BFS/Uniform Cost): ")

def DFS_search(grid, start, goal):
    stack = [start]
    visited = set([start])
    parent = {start: None}
    visited_tiles = 0
    while stack:
        current = stack.pop()
        visited_tiles += 1
        if current == goal:
            print(f"Tiles visited: {visited_tiles}")
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            next_cell = (current[0] + dx, current[1] + dy)
            if 0 <= next_cell[0] < grid_rows and 0 <= next_cell[1] < grid_columns and grid[next_cell[0]][next_cell[1]] != '#' and next_cell not in visited:
                stack.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

def BFS_search(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    visited_tiles = 0
    while queue:
        current = queue.popleft()
        visited_tiles += 1
        if current == goal:
            print(f"Tiles visited: {visited_tiles}")
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            next_cell = (current[0] + dx, current[1] + dy)
            if 0 <= next_cell[0] < grid_rows and 0 <= next_cell[1] < grid_columns and grid[next_cell[0]][next_cell[1]] != '#' and next_cell not in visited:
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

def uniform_cost_search(grid, start, goal):
    frontier = [(0, start, [])]
    visited = set()
    visited_tiles = 0
    while frontier:
        cost, current, path = heapq.heappop(frontier)
        if current not in visited:
            visited_tiles += 1
            visited.add(current)
            if current == goal:
                print(f"Tiles visited: {visited_tiles}")
                return path + [current]
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_cell = (current[0] + dx, current[1] + dy)
                if 0 <= next_cell[0] < grid_rows and 0 <= next_cell[1] < grid_columns and grid[next_cell[0]][next_cell[1]] != '#' and next_cell not in visited:
                    heapq.heappush(frontier, (cost + 1, next_cell, path + [current]))

path = []
if algorithm == "DFS":
    path = DFS_search(grid, start_point, goal_point)
elif algorithm == "BFS":
    path = BFS_search(grid, start_point, goal_point)
elif algorithm == "Uniform Cost":
    path = uniform_cost_search(grid, start_point, goal_point)

if path:
    for r, c in path:
        if (r, c) != start_point and (r, c) != goal_point:
            grid[r][c] = "P"

print("Final grid with path:")
for row in grid:
    print(' '.join(row))
