import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Registro from './components/Registro.tsx';
import Usuarios from './components/Usuarios.tsx';
import './App.css';
import './styles/style.css';
import './styles/admin.css';
import RegistroSecretaria from './components/pages/Usuarios/RegistroSecretaria.tsx';
import Ordenes from './components/pages/Ordenes/Ordenes.tsx';


function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header className="App-header">
          <h1 className="text-3xl font-bold mb-8">EP Bobinado de Motores</h1>
          <Routes>
            <Route path="/" element={<Registro />} />
            <Route path="/usuarios" element={<Usuarios />} />
            <Route path="/usuarios/registro" element={<RegistroSecretaria />} />
            <Route path="/ordenes" element={<Ordenes />} />
          </Routes>
        </header>
      </div>
    </BrowserRouter>
  );
}

export default App;
