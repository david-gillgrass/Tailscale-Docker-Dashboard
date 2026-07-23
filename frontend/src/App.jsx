import { useState } from 'react'
import { useEffect } from 'react'
import './App.css'

function App() {

  const [Services, setServices] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/Services")
    .then(response => response.json())
    .then(data => setServices(data.Services));
  },[]);

  return (
    <>
    <pre>{JSON.stringify(Services,null,2)}</pre>
    </>
  )
}

export default App
