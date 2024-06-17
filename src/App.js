import './App.css';
import { useState } from 'react';

function App() {
  // Variables

  function sgc() {
    window.open("https://classroom.google.com/c/NjYzNTUwNzIxNjUy?cjc=3szhm7i", "_blank");
  }
  function discord() {
    window.open("", "_blank");
  }
  function SlothGoogleClassroom() {
    return (
      <>
        <button onClick={sgc}>Sloth Google Classroom</button>
      </>
    )
  }
  function DiscordInvite() {
    return (
      <>
        <button onClick={discord}>rbaxim's discord sever</button>
      </>
    )
  }
  // html
  return (
    <div className="App">
      <header className="App-header">
          <h1>Welcome to the Sloth Website</h1>
          <SlothGoogleClassroom />
          <DiscordInvite />
          <p>Give me ideas on these pages above</p>
          <hr />
          <h6>This is a placeholder for games</h6>
      </header>
    </div>
  );
}


export default App;
