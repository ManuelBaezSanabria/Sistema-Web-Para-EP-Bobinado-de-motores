import React, { useEffect, useState } from 'react';
import axios from 'axios';
import LayoutAdmin from '../../layout/LayoutAdmin.tsx';
import UsuarioModal from '../../UsuarioModal.tsx';

const BASE_URL = 'http://127.0.0.1:8000';

const Ordenes = () => {
  const [Ordenes, setOrdenes] = useState<any[]>([]);
  const [editOrden, setEditOrden] = useState<any>(null);
  const [busqueda, setBusqueda] = useState(''); // <-- nuevo estado para la búsqueda

  const cargarOrdenes = async () => {
    const res = await axios.get(`${BASE_URL}/api/ordenes/`);
    setOrdenes(res.data);
  };

  useEffect(() => {
    cargarOrdenes();
  }, []);

  const eliminarOrden = async (id: number) => {
    if (!window.confirm('¿Eliminar Orden?')) return;
    await axios.delete(`${BASE_URL}/api/ordenes/${id}/`);
    cargarOrdenes();
  };

  const actualizarOrden = async (data: any) => {
    await axios.put(`${BASE_URL}/api/ordenes/${data.id}/`, data);
    setEditOrden(null);
    cargarOrdenes();
  };

  // Filtrar Ordenes según búsqueda por nombre, teléfono o cédula
  const OrdenesFiltrados = Ordenes.filter(u =>
    (u.motorid && u.motorid.toString().includes(busqueda)) ||
    (u.estado && u.estado.includes(busqueda)) ||
    (u.tecnicoid && u.tecnicoid.toString().includes(busqueda))
  );

  return (
    <LayoutAdmin>
      <div className="page-content">
        <h1 className="page-title">Ordenes</h1>

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
              <th>Motor</th>
              <th>Estado</th>
              <th>Técnico</th>
              <th>Creado</th>
              <th>Acciones</th>
            </tr>
          </thead>

          <tbody>
            {OrdenesFiltrados.map(u => (
              <tr key={u.id}>
                <td>{u.motorid}</td>
                <td>{u.estado}</td>
                <td>{u.tecnicoid}</td>
                <td>{u.creadoen}</td>
                <td className="actions">
                  <button
                    className="btn-sm btn-edit"
                    onClick={() => setEditOrden(u)}
                  >
                    ✏️
                  </button>
                  <button
                    className="btn-sm btn-delete"
                    onClick={() => eliminarOrden(u.id)}
                  >
                    🗑️
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
            
        {/*editOrden && (
          <OrdenModal
            orden={editOrden}
            onClose={() => setEditOrden(null)}
            onSave={actualizarOrden}
          />
        )*/}
      </div>
    </LayoutAdmin>
  );
};

export default Ordenes;