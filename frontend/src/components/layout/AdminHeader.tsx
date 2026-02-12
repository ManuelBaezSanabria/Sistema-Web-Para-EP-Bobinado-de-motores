import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  FaTools,
  FaBell, 
  FaUserCircle, 
  FaSignOutAlt,
  FaCog
} from 'react-icons/fa';
import '../../styles/admin-header.css';

const AdminHeader: React.FC = () => {
  const navigate = useNavigate();
  const [showNotifications, setShowNotifications] = useState(false);
  
  const handleLogout = () => {
    if (window.confirm('¿Está seguro de cerrar sesión?')) {
      localStorage.removeItem('userSession');
      localStorage.removeItem('authToken');
      navigate('/login');
    }
  };

  // Obtener datos del usuario
  const userSessionStr = localStorage.getItem('userSession');
  let userName = 'Admin';
  let userRole = 'Administrador';
  
  if (userSessionStr) {
    try {
      const userSession = JSON.parse(userSessionStr);
      userName = userSession.user?.name || 'Admin';
      userRole = userSession.user?.role === 'admin' ? 'Administrador' : 
                 userSession.user?.role === 'secretaria' ? 'Secretaria' : 'Usuario';
    } catch (error) {
      console.error('Error parsing user session:', error);
    }
  }

  return (
    <header className="admin-header">
      <div className="header-logo">
        <FaTools className="logo-icon" />
        <span className="logo-text">EP Bobinado</span>
      </div>

      <div className="header-user-section">
        <div className="welcome-text">
          Bienvenido, <strong>{userName}</strong>
          <span className="user-role-badge">{userRole}</span>
        </div>

        <div className="header-actions">
          <button 
            className="header-btn notification-btn"
            onClick={() => setShowNotifications(!showNotifications)}
          >
            <FaBell />
            <span className="notification-count">3</span>
          </button>

          <button className="header-btn settings-btn" title="Configuración">
            <FaCog />
          </button>

          <button className="header-btn logout-btn" onClick={handleLogout}>
            <FaSignOutAlt />
            <span className="btn-text">Salir</span>
          </button>
        </div>

        {/* Dropdown de notificaciones */}
        {showNotifications && (
          <div className="notifications-dropdown">
            <div className="notifications-header">
              <h4>Notificaciones</h4>
              <span className="notifications-count">3 nuevas</span>
            </div>
            <div className="notifications-list">
              <div className="notification-item unread">
                <div className="notification-icon">
                  <FaBell />
                </div>
                <div className="notification-content">
                  <p className="notification-title">Nueva orden creada</p>
                  <p className="notification-time">Hace 5 minutos</p>
                </div>
              </div>
              <div className="notification-item unread">
                <div className="notification-icon">
                  <FaUserCircle />
                </div>
                <div className="notification-content">
                  <p className="notification-title">Nuevo cliente registrado</p>
                  <p className="notification-time">Hace 1 hora</p>
                </div>
              </div>
              <div className="notification-item">
                <div className="notification-icon">
                  <FaTools />
                </div>
                <div className="notification-content">
                  <p className="notification-title">Servicio completado</p>
                  <p className="notification-time">Hace 2 horas</p>
                </div>
              </div>
            </div>
            <div className="notifications-footer">
              <a href="/notificaciones">Ver todas las notificaciones</a>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default AdminHeader;
