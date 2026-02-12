import React, { useState } from 'react';
import axios from 'axios';
//import LayoutAdmin from '../../layout/LayoutAdmin.tsx';

const BASE_URL = 'http://127.0.0.1:8000';


const Registro = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    email: '',
    telefono: '',
    password: '',
    confirm_password: '',
    cedula: '',
    rol: 'Usuario', 
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Validación de contraseñas
    if (formData.password !== formData.confirm_password) {
      alert('Las contraseñas no coinciden');
      return;
    }

    try {
      // Envía los datos al backend
      const response = await axios.post(`${BASE_URL}/api/auth/registro/`, formData);
      alert('Usuario registrado con éxito!');
      setFormData({
        nombre: '',
        email: '',
        telefono: '',
        password: '',
        confirm_password: '',
        cedula: '',
        rol: 'Usuario',
      });
    } catch (error: any) {
      alert('Error: ' + (error.response?.data?.error || 'Error desconocido'));
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2 style={styles.title}>Registrarse en el Sistema</h2>
        <form onSubmit={handleSubmit} style={styles.form}>
          <input
            type="text"
            placeholder="Nombre completo"
            value={formData.nombre}
            onChange={e => setFormData({ ...formData, nombre: e.target.value })}
            required
            style={styles.input}
          />

          <input
            type="email"
            placeholder="Email"
            value={formData.email}
            onChange={e => setFormData({ ...formData, email: e.target.value })}
            required
            style={styles.input}
          />

          <input
            type="tel"
            placeholder="Teléfono"
            value={formData.telefono}
            onChange={e => setFormData({ ...formData, telefono: e.target.value })}
            style={styles.input}
          />

          <input
            type="password"
            placeholder="Contraseña"
            value={formData.password}
            onChange={e => setFormData({ ...formData, password: e.target.value })}
            required
            style={styles.input}
          />

          <input
            type="password"
            placeholder="Confirmar contraseña"
            value={formData.confirm_password}
            onChange={e => setFormData({ ...formData, confirm_password: e.target.value })}
            required
            style={styles.input}
          />

          <select
            value={formData.rol}
            onChange={e => setFormData({ ...formData, rol: e.target.value })}
            style={styles.input}
            required
          >
            <option value="Administrador">Administrador</option>
            <option value="Secretaria">Secretaria</option>
            <option value="Usuario">Usuario</option>
          </select>

          <input
            type="text"
            placeholder="Cédula"
            value={formData.cedula}
            onChange={e => setFormData({ ...formData, cedula: e.target.value })}
            required
            style={styles.input}
          />

          <button type="submit" style={styles.button}>
            Registrarse
          </button>
        </form>
      </div>
    </div>
  );
};

export default Registro;

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f6fa',
    padding: '20px',
  },
  card: {
    width: '100%',
    maxWidth: '400px',
    backgroundColor: '#fff',
    padding: '30px',
    borderRadius: '10px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
  },
  title: {
    textAlign: 'center',
    marginBottom: '20px',
    color: '#333',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '12px',
  },
  input: {
    padding: '10px',
    fontSize: '16px',
    borderRadius: '6px',
    border: '1px solid #ccc',
  },
  button: {
    padding: '12px',
    backgroundColor: '#007bff',
    color: '#fff',
    fontSize: '16px',
    border: 'none',
    borderRadius: '6px',
    cursor: 'pointer',
    marginTop: '10px',
  },
};