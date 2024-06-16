import './App.css';
import { useState } from 'react';

function App() {
  // Variables

  function sgc() {
    window.open("https://classroom.google.com/c/NjYzNTUwNzIxNjUy?cjc=3szhm7i", "_blank");
  }

  function SlothGoogleClassroom() {
    return (
      <>
        <button onClick={sgc}>Sloth Google Classroom</button>
      </>
    )
  }
  // html
  return (
    <div className="App">
      <header className="App-header">
          <h1>hi</h1>
          <SlothGoogleClassroom />
      </header>
    </div>
  );
}


export default App;
