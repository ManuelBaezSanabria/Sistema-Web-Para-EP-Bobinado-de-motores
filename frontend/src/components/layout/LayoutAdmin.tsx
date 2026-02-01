import React from 'react';
import AdminHeader from './AdminHeader.tsx';
import Sidebar from './Sidebar.tsx';

interface Props {
  children: React.ReactNode;
}

const LayoutAdmin = ({ children }: Props) => {
  return (
    <div className="admin-page">
      <AdminHeader />
      <Sidebar />

      <main className="main-content">
        {children}
      </main>

      <footer className="admin-footer">
        © 2026 EP Bobinado de Motores
      </footer>
    </div>
  );
};

export default LayoutAdmin;
