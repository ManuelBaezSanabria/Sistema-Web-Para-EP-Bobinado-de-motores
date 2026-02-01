import React, { useEffect, useState } from 'react';
import axios from 'axios';
import LayoutAdmin from './layout/LayoutAdmin.tsx';
import UsuarioModal from './UsuarioModal.tsx';

const BASE_URL = 'http://127.0.0.1:8000';

const Usuarios = () => {
  const [usuarios, setUsuarios] = useState<any[]>([]);
  const [editUsuario, setEditUsuario] = useState<any>(null);

  const cargarUsuarios = async () => {
    const res = await axios.get(`${BASE_URL}/api/auth/usuarios/`);
    setUsuarios(res.data);
  };

  useEffect(() => {
    cargarUsuarios();
  }, []);

  const eliminarUsuario = async (id: number) => {
    if (!window.confirm('¿Eliminar usuario?')) return;
    await axios.delete(`${BASE_URL}/api/auth/usuarios/${id}/`);
    cargarUsuarios();
  };

  const actualizarUsuario = async (data: any) => {
    await axios.put(`${BASE_URL}/api/auth/usuarios/${data.id}/`, data);
    setEditUsuario(null);
    cargarUsuarios();
  };

  return (
  <LayoutAdmin>
    <div className="page-content">

      <h1 className="page-title">Usuarios</h1>

      <table className="data-table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {usuarios.map(u => (
            <tr key={u.id}>
              <td>{u.nombre}</td>
              <td>{u.email}</td>
              <td className="actions">
                <button
                  className="btn-sm btn-edit"
                  onClick={() => setEditUsuario(u)}
                >
                  ✏️
                </button>

                <button
                  className="btn-sm btn-delete"
                  onClick={() => eliminarUsuario(u.id)}
                >
                  🗑️
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {editUsuario && (
        <UsuarioModal
          usuario={editUsuario}
          onClose={() => setEditUsuario(null)}
          onSave={actualizarUsuario}
        />
      )}

    </div>
  </LayoutAdmin>
);

};

export default Usuarios;
