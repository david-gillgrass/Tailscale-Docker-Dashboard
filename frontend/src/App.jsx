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
      {Services.map((service) => (
        <div key = {service.Name}>
        <h2><u>{service.Name}</u></h2>
        <p2>{service.LAN_URL}</p2>
        <p>{service.Tailscale_URL}</p>
        </div>
      ))}
      </>
    );
}

export default App
