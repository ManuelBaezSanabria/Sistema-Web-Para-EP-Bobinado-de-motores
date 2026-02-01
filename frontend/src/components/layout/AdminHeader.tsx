const AdminHeader = () => {
  return (
    <header className="admin-header">
      <div className="logo">
        <i className="fas fa-tools"></i>
        <span>EP Bobinado</span>
      </div>

      <div className="user-info">
        <span>
          Bienvenido, <strong>Admin</strong>
        </span>
        <a className="btn-notify">
          <i className="fas fa-bell"></i>
        </a>
        <a className="btn-logout">
          <i className="fas fa-sign-out-alt"></i> Salir
        </a>
      </div>
    </header>
  );
};

export default AdminHeader;
