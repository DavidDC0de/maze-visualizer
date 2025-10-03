from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random 
import heapq

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

rows, cols = 41, 41


def generate_grid(maze):
    for i in range(rows):
        maze.append([])
        for j in range(cols):
            maze[i].append(1)
    maze[1][1] = 0

def get_unvisited_neighbors(maze, x, y):
    neighbors = []
    if (x > 1) and maze[x - 2][y] == 1:
        neighbors.append((x - 2, y))
        
    if  (x < cols - 3) and maze[x + 2][y] == 1:
        neighbors.append((x + 2, y))
            
    if (y > 1) and maze[x][y - 2] == 1:
        neighbors.append((x, y - 2))
                
    if (y < rows - 3) and maze[x][y + 2] == 1:
        neighbors.append((x, y + 2))

    return neighbors


def generate_maze():
    maze = []
    generate_grid(maze)
    start = (1, 1)
    stack = [start]

    while stack:
        x, y = stack[-1]
        neighbors = get_unvisited_neighbors(maze, x, y)

        if neighbors:
            new_x, new_y = random.choice(neighbors)
            maze[new_x][new_y] = 0
            maze[(x + new_x)//2][(y + new_y) //2] = 0

            stack.append((new_x, new_y))

        else:
            stack.pop()
    return maze


def calculate_h_score(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])


def a_star_neighbours(maze, current):
    neighbors = []
    x, y = current

    if maze[x - 1][y] == 0:
        neighbors.append((x - 1, y))
        
    if maze[x + 1][y] == 0:
        neighbors.append((x + 1, y))
            
    if maze[x][y - 1] == 0:
        neighbors.append((x, y - 1))
                
    if maze[x][y + 1] == 0:
        neighbors.append((x, y + 1))

    return neighbors


def a_star(maze):
    start = (1, 1)
    end = (rows - 2, cols - 2)

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {start: 0}
    f_score = {start: calculate_h_score(start, end)}
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbour in a_star_neighbours(maze, current):
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbour, float("inf")):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g
                f_score[neighbour] = tentative_g + calculate_h_score(neighbour, end)
                heapq.heappush(open_set, (f_score[neighbour], neighbour))

    return None

def show_solved_path(maze, path): #changes the maze to show the solved path
    solved_path = 2
    for node in path:
        x, y = node
        maze[x][y] = solved_path

    return maze


@app.get("/get-maze")
def get_unsolved_maze():
    global maze
    maze = generate_maze()
    return {"maze": maze}

@app.get("/get-solved-maze")
def get_solved_maze():
    global maze
    path = a_star(maze)
    solved_maze = show_solved_path(maze, path)
    return  {"maze": solved_maze}


