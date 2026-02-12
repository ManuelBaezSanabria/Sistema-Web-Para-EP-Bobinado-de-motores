import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { 
  FaUsers, 
  FaMotorcycle,
  FaClipboardList, 
  FaTools,
  FaHistory,
  FaChartBar,
  FaCog
} from 'react-icons/fa';
import '../../styles/sidebar.css';

const Sidebar: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const menuItems = [
    { path: '/usuarios', icon: <FaUsers />, label: 'Clientes' },
    { path: '/motores', icon: <FaMotorcycle />, label: 'Motores' },
    { path: '/ordenes', icon: <FaClipboardList />, label: 'Órdenes' },
    { path: '/servicios', icon: <FaTools />, label: 'Servicios' },
    { path: '/historial', icon: <FaHistory />, label: 'Historial' },
    { path: '/reportes', icon: <FaChartBar />, label: 'Reportes' },
    { path: '/configuracion', icon: <FaCog />, label: 'Configuración' },
  ];

  const isActive = (path: string) => location.pathname === path;

  return (
    <nav className="sidebar">
      <div className="sidebar-header">
        <div className="sidebar-brand">
          <FaTools className="brand-icon" />
          <span className="brand-text">Mi Taller</span>
        </div>
      </div>
      
      <ul className="sidebar-menu">
        {menuItems.map((item) => (
          <li 
            key={item.path}
            className={`menu-item ${isActive(item.path) ? 'active' : ''}`}
          >
            <a onClick={() => navigate(item.path)}>
              <span className="menu-icon">{item.icon}</span>
              <span className="menu-label">{item.label}</span>
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Sidebar;