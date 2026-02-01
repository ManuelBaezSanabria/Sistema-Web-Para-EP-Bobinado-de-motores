const Sidebar = () => {
  return (
    <nav className="sidebar">
      <ul className="nav-menu">
        <li className="active">
          <a>
            <i className="fas fa-users"></i> Clientes
          </a>
        </li>
        <li>
          <a>
            <i className="fas fa-cogs"></i> Motores
          </a>
        </li>
        <li>
          <a>
            <i className="fas fa-clipboard-list"></i> Órdenes
          </a>
        </li>
      </ul>
    </nav>
  );
};

export default Sidebar;
