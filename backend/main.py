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
maze = []
rows, cols = 11, 11
data = {"maze": maze}

def generate_grid():
    for i in range(rows):
        maze.append([])
        for j in range(cols):
            maze[i].append(1)
    maze[1][1] = 0

def get_unvisited_neighbors(x, y):
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
    generate_grid()
    start = (1, 1)
    stack = [start]

    while stack:
        x, y = stack[-1]
        neighbors = get_unvisited_neighbors(x, y)

        if neighbors:
            new_x, new_y = random.choice(neighbors)
            maze[new_x][new_y] = 0
            maze[(x + new_x)//2][(y + new_y) //2] = 0

            stack.append((new_x, new_y))

        else:
            stack.pop()

def print_maze(maze):
    for row in maze:
        print("".join("⬛" if cell == 1 else "⬜" for cell in row))


def calculate_h_score(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])

def calculate_f_score(node, end):
    x, y = node
    g_score = 0
    h_score = 0
    f_score = 0

    if (node == (1, 1)):
        g_score = 0
        h_score = calculate_h_score(node, end)

def a_star_neighbours(current):
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


def a_star():
    start = (1, 1)
    end = (rows - 2, cols - 2)

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {strart: 0}
    f_score = (start: calculate_f_score(start, end))
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

        for neighbors in a_star_neighbours(current):
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + calculate_h_score(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


generate_maze()
print_maze(maze)
@app.get("/get-maze")
def get_data():
    return data


