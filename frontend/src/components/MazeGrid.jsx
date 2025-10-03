import "../styles/maze.css";

function MazeGrid({ maze }) {
  return (
    <div className="maze">
      {maze.map((row, rowIndex) => ( // for every row in the maze
        <div key={rowIndex} className="row">
          {row.map((cell, colIndex) => (  //for every cell in the row 
            <div
              key={colIndex}
              className={`cell ${
                cell === 0 ? "path": 
                cell === 1 ? "wall":
                "solved"}`}
            />
          ))}
        </div>
      ))}
    </div>
  );
}

export default MazeGrid;