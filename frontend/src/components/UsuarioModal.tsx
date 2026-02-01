import React, { useState, useEffect } from 'react';

interface Props {
  usuario: any;
  onClose: () => void;
  onSave: (data: any) => void;
}

const UsuarioModal = ({ usuario, onClose, onSave }: Props) => {
  const [form, setForm] = useState(usuario);

  useEffect(() => {
    setForm(usuario);
  }, [usuario]);

  const handleChange = (e: any) => {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === 'checkbox' ? checked : value
    });
  };

  return (
    <div className="modal-backdrop">
      <div className="modal">
        <h3>Editar Usuario</h3>

        <input
          name="nombre"
          value={form.nombre}
          onChange={handleChange}
          placeholder="Nombre"
        />

        <input
          name="email"
          value={form.email}
          onChange={handleChange}
          placeholder="Email"
        />

        <input
          name="telefono"
          value={form.telefono}
          onChange={handleChange}
          placeholder="Teléfono"
        />

        <label>
          <input
            type="checkbox"
            name="activo"
            checked={form.activo}
            onChange={handleChange}
          />
          Activo
        </label>

        <div className="modal-actions">
          <button onClick={() => onSave(form)} className="btn-edit">
            Guardar
          </button>
          <button onClick={onClose} className="btn-delete">
            Cancelar
          </button>
        </div>
      </div>
    </div>
  );
};

export default UsuarioModal;
