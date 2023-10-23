import React, { useState } from 'react';
import axios from 'axios';

function MyComponent() {
  const [menus, setMenus] = useState([]);

  const handleClick = () => {
    axios.get('http://192.168.1.41:8000/menus/')
      .then(response => setMenus(response.data))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <button onClick={handleClick}>Get Menus</button>
      <h1>Menus:</h1>
      <ul>
        {menus.map(menu => (
          <li key={menu.id}>{menu.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default MyComponent;
