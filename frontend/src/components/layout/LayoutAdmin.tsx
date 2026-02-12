import React from 'react';
import AdminHeader from './AdminHeader.tsx';
import Sidebar from './Sidebar.tsx';
import '../../styles/layout-admin.css';

interface Props {
  children: React.ReactNode;
}

const LayoutAdmin: React.FC<Props> = ({ children }) => {
  return (
    <div className="admin-layout">
      <Sidebar />
      <div className="admin-main-wrapper">
        <AdminHeader />
        <main className="admin-content">
          {children}
        </main>
        <footer className="admin-footer">
          © 2026 EP Bobinado de Motores
        </footer>
      </div>
    </div>
  );
};

export default LayoutAdmin;
