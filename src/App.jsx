
import React, { useState } from "react";
import "./App.css";

function App() {
  const [color, setColor] = useState("Red");

  return (
    <div className="container">
      <h2>Color Changer App</h2>

      <button onClick={() => setColor("Red")}>
        Red
      </button>

      <button onClick={() => setColor("Green")}>
        Green
      </button>

      <button onClick={() => setColor("Blue")}>
        Blue
      </button>

      <div
        className="box"
        style={{ backgroundColor: color }}
      >
        Selected Color: {color}
      </div>
    </div>
  );
}

export default App;
