import React from "react";
import { FaTools, FaSignOutAlt } from "react-icons/fa";

const Header = () => {
  return (
    <header className="public-header">
      <div className="container">
        <nav className="public-nav">
          <a href="/dashboard" className="logo">
            <FaTools />
            <span>Mi Taller</span>
          </a>
          <ul className="nav-links">
            <li>
              <button className="btn btn-outline">
                <FaSignOutAlt /> Salir
              </button>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;

