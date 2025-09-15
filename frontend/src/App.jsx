import { useState, useEffect } from 'react'


function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/get-data")
    .then((res) => res.json())
    .then((data) => setMessage(data.message))
    .catch((err) => console.log(err));
  }, []);


  return (
    <div>
      <h1>Message from Python:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
