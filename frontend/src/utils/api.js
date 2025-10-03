export async function fetchMaze(maze_state) {
    let response;
    if (maze_state === "unsolved") {
        response = await fetch("http://127.0.0.1:8000/get-maze");
    } else {
        response = await fetch("http://127.0.0.1:8000/get-solved-maze");
    }
    
    const data = await response.json();
    return data.maze;
} // maze is extracted through the api from the backend 