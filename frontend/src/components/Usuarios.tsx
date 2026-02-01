import React, { useEffect, useState } from 'react';
import axios from 'axios';
import LayoutAdmin from './layout/LayoutAdmin.tsx';
import UsuarioModal from './UsuarioModal.tsx';

const BASE_URL = 'http://127.0.0.1:8000';

const Usuarios = () => {
  const [usuarios, setUsuarios] = useState<any[]>([]);
  const [editUsuario, setEditUsuario] = useState<any>(null);
  const [busqueda, setBusqueda] = useState(''); // <-- nuevo estado para la búsqueda

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

  // Filtrar usuarios según búsqueda por nombre, teléfono o cédula
  const usuariosFiltrados = usuarios.filter(u =>
    u.nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
    (u.telefono && u.telefono.includes(busqueda)) ||
    (u.cedula && u.cedula.includes(busqueda))
  );

  return (
    <LayoutAdmin>
      <div className="page-content">
        <h1 className="page-title">Usuarios</h1>

        {/* Sección de búsqueda */}
        <div className="busqueda">
          <input
            type="text"
            placeholder="Buscar por nombre, teléfono o cédula"
            value={busqueda}
            onChange={(e) => setBusqueda(e.target.value)}
            className="input-busqueda"
          />
        </div>

        <table className="data-table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Email</th>
              <th>Teléfono</th>
              <th>Cédula</th>
              <th>Acciones</th>
            </tr>
          </thead>

          <tbody>
            {usuariosFiltrados.map(u => (
              <tr key={u.id}>
                <td>{u.nombre}</td>
                <td>{u.email}</td>
                <td>{u.telefono}</td>
                <td>{u.cedula}</td>
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

