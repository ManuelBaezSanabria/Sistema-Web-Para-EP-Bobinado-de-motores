import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Registro from './components/Registro.tsx';
import Usuarios from './components/Usuarios.tsx';
import Login from "./components/auth/Login.tsx";
import Ordenes from './components/pages/Ordenes/Ordenes.tsx';
import Proveedores from './components/pages/Proveedores/Proveedores.tsx';
import RegistroSecretaria from './components/pages/Usuarios/RegistroSecretaria.tsx';
import DashboardClientes from './components/pages/Clientes/DashboardClientes.tsx';
import './App.css';
import './styles/style.css';
import './styles/admin.css';

// Componente para proteger rutas
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const userSession = localStorage.getItem('userSession');
  
  if (!userSession) {
    return <Navigate to="/login" replace />;
  }
  
  return <>{children}</>;
};

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          {/* Rutas Públicas */}
          <Route path="/login" element={<Login />} />
          <Route path="/registro" element={<Registro />} />
          
          {/* Rutas Protegidas - Clientes */}
          <Route 
            path="/cliente-dashboard" 
            element={
              <ProtectedRoute>
                <DashboardClientes />
              </ProtectedRoute>
            } 
          />
          
          {/* Rutas Protegidas - Admin/Usuarios */}
          <Route 
            path="/usuarios" 
            element={
              <ProtectedRoute>
                <Usuarios />
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/usuarios/registro" 
            element={
              <ProtectedRoute>
                <RegistroSecretaria />
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/ordenes" 
            element={
              <ProtectedRoute>
                <Ordenes />
              </ProtectedRoute>
            } 
          />
          <Route 
            path="/proveedores" 
            element={
              <ProtectedRoute>
                <Proveedores />
              </ProtectedRoute>
            } 
          />
          
          {/* Redirección por defecto */}
          <Route path="/" element={<Navigate to="/login" replace />} />
          
          {/* Ruta 404 */}
          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
