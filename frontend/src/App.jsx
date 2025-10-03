import { useState, useEffect } from 'react'
import { fetchMaze } from './utils/api' 
import MazeGrid from "./components/MazeGrid";
import Controls from "./components/Controls"


function App() {
  const [maze, setMaze] = useState([]);  //holds the maze data from the backend 

  
  async function getMaze() {  
    const data = await fetchMaze("unsolved");  
    setMaze(data);  
  }

  async function getSolvedMaze() {  
    const data = await fetchMaze("solved");  
    setMaze(data);  
  }

  useEffect(() => {
    getMaze();
  }, [])
  

  return ( 
    <div>
      
      <Controls onSolve={getSolvedMaze} onGenerate={getMaze}/>
      <MazeGrid maze={maze} /> 
    </div>
  );
}

export default App;
