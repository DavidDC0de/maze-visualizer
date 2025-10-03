function Controls({onGenerate, onSolve}) {
    return (
        <div className="controls">
            <h1 className="text_title">A* Path finder in Maze </h1>
            <button className="generate_button" onClick={onGenerate}>Generate</button>
            <button className="solve_button" onClick={onSolve}>Solve</button>
            
        </div>
    )
}

export default Controls