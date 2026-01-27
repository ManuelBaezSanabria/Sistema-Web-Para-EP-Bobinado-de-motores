import React from 'react';
import Registro from './components/Registro.tsx';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="text-3xl font-bold mb-8">EP Bobinado de Motores</h1>
        <Registro />
      </header>
    </div>
  );
}

export default App;