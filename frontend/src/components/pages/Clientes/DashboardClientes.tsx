import React from "react";
import { 
  FaTools, 
  FaMotorcycle, 
  FaClock, 
  FaClipboardList, 
  FaHistory, 
  FaUser,
  FaSignOutAlt,
  FaCheckCircle,
  FaHourglassHalf,
  FaExclamationTriangle,
  FaArrowRight
} from "react-icons/fa";
import "../../../styles/cliente.css";

const Dashboard: React.FC = () => {
  const userName = "Juan Pérez";

  const logout = () => {
    if (window.confirm("¿Está seguro de cerrar sesión?")) {
      localStorage.removeItem("userSession");
      window.location.href = "/login";
    }
  };

  // Datos de ejemplo
  const activeOrders = [
    {
      id: 1,
      motor: "Yamaha YZF-R1 2020",
      service: "Mantenimiento General",
      status: "En progreso",
      technician: "Carlos Méndez",
      progress: 65,
      estimatedDate: "15 Feb 2026"
    },
    {
      id: 2,
      motor: "Honda CBR 600RR 2019",
      service: "Cambio de aceite",
      status: "Pendiente",
      technician: "Ana García",
      progress: 30,
      estimatedDate: "14 Feb 2026"
    }
  ];

  const recentActivity = [
    { date: "10 Feb", action: "Servicio completado", motor: "Kawasaki Ninja 650" },
    { date: "05 Feb", action: "Nueva orden creada", motor: "Yamaha YZF-R1" },
    { date: "28 Ene", action: "Motor registrado", motor: "Honda CBR 600RR" }
  ];

  return (
    <div className="dashboard-page">
      {/* Header */}
      <header className="dashboard-header-nav">
        <div className="container-fluid">
          <nav className="nav-content">
            <a href="/cliente-dashboard" className="brand-logo">
              <FaTools className="logo-icon" />
              <FaMotorcycle className="logo-icon" />
              <span className="brand-name">Mi Taller</span>
            </a>
            
            <div className="nav-menu">
              <a href="/cliente-dashboard" className="nav-item active">
                <FaTools /> Dashboard
              </a>
              <a href="/cliente-mis-motores" className="nav-item">
                <FaMotorcycle /> Mis Motores
              </a>
              <a href="/cliente-mis-ordenes" className="nav-item">
                <FaClipboardList /> Órdenes
              </a>
              <a href="/cliente-historial" className="nav-item">
                <FaHistory /> Historial
              </a>
              <a href="/cliente-perfil" className="nav-item">
                <FaUser /> Perfil
              </a>
            </div>

            <div className="nav-actions">
              <div className="user-info">
                <div className="user-avatar">
                  {userName.charAt(0)}
                </div>
                <span className="user-name">{userName}</span>
              </div>
              <button onClick={logout} className="btn-logout">
                <FaSignOutAlt />
              </button>
            </div>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="dashboard-main">
        <div className="container-fluid">
          {/* Welcome Section */}
          <div className="welcome-section">
            <div className="welcome-text">
              <h1>¡Bienvenido, {userName}! 👋</h1>
              <p>Aquí está el resumen de tus motores y servicios</p>
            </div>
            <button className="btn-primary">
              <FaMotorcycle /> Registrar Nuevo Motor
            </button>
          </div>

          {/* Stats Cards */}
          <div className="stats-grid">
            <div className="stat-card card-blue">
              <div className="stat-icon-wrapper">
                <FaMotorcycle className="stat-icon" />
              </div>
              <div className="stat-details">
                <h3 className="stat-number">3</h3>
                <p className="stat-label">Motores Registrados</p>
                <a href="/cliente-mis-motores" className="stat-link">
                  Ver todos <FaArrowRight />
                </a>
              </div>
            </div>

            <div className="stat-card card-orange">
              <div className="stat-icon-wrapper">
                <FaHourglassHalf className="stat-icon" />
              </div>
              <div className="stat-details">
                <h3 className="stat-number">2</h3>
                <p className="stat-label">Órdenes Activas</p>
                <a href="/cliente-mis-ordenes" className="stat-link">
                  Ver todas <FaArrowRight />
                </a>
              </div>
            </div>

            <div className="stat-card card-green">
              <div className="stat-icon-wrapper">
                <FaCheckCircle className="stat-icon" />
              </div>
              <div className="stat-details">
                <h3 className="stat-number">15</h3>
                <p className="stat-label">Servicios Completados</p>
                <a href="/cliente-historial" className="stat-link">
                  Ver historial <FaArrowRight />
                </a>
              </div>
            </div>

            <div className="stat-card card-purple">
              <div className="stat-icon-wrapper">
                <FaClock className="stat-icon" />
              </div>
              <div className="stat-details">
                <h3 className="stat-number">1</h3>
                <p className="stat-label">Próximos Mantenimientos</p>
                <a href="/cliente-mis-ordenes" className="stat-link">
                  Ver detalles <FaArrowRight />
                </a>
              </div>
            </div>
          </div>

          {/* Active Orders Section */}
          <div className="dashboard-section">
            <div className="section-header">
              <h2>
                <FaClipboardList /> Órdenes Activas
              </h2>
              <a href="/cliente-mis-ordenes" className="view-all-link">
                Ver todas <FaArrowRight />
              </a>
            </div>

            <div className="orders-grid">
              {activeOrders.map((order) => (
                <div key={order.id} className="order-card">
                  <div className="order-header">
                    <div className="order-motor">
                      <FaMotorcycle className="motor-icon" />
                      <div>
                        <h3>{order.motor}</h3>
                        <p>{order.service}</p>
                      </div>
                    </div>
                    <span className={`status-badge ${order.status === 'En progreso' ? 'status-progress' : 'status-pending'}`}>
                      {order.status === 'En progreso' ? <FaHourglassHalf /> : <FaExclamationTriangle />}
                      {order.status}
                    </span>
                  </div>

                  <div className="order-body">
                    <div className="order-info-row">
                      <span className="info-label">Técnico:</span>
                      <span className="info-value">{order.technician}</span>
                    </div>
                    <div className="order-info-row">
                      <span className="info-label">Fecha estimada:</span>
                      <span className="info-value">{order.estimatedDate}</span>
                    </div>

                    <div className="progress-section">
                      <div className="progress-header">
                        <span>Progreso</span>
                        <span className="progress-percentage">{order.progress}%</span>
                      </div>
                      <div className="progress-bar">
                        <div 
                          className="progress-fill" 
                          style={{ width: `${order.progress}%` }}
                        ></div>
                      </div>
                    </div>
                  </div>

                  <div className="order-footer">
                    <button className="btn-secondary btn-sm">Ver Detalles</button>
                    <button className="btn-outline btn-sm">Contactar Técnico</button>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Recent Activity */}
          <div className="dashboard-section">
            <div className="section-header">
              <h2>
                <FaHistory /> Actividad Reciente
              </h2>
            </div>

            <div className="activity-list">
              {recentActivity.map((activity, index) => (
                <div key={index} className="activity-item">
                  <div className="activity-date">{activity.date}</div>
                  <div className="activity-content">
                    <p className="activity-action">{activity.action}</p>
                    <p className="activity-motor">{activity.motor}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;