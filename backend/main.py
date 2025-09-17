from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random 

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

generate_maze()
print_maze(maze)
@app.get("/get-maze")
def get_data():
    return data


