import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../../../styles/proveedores.css';


const BASE_URL = 'http://127.0.0.1:8000';

const Proveedores = () => {

  const [formData, setFormData] = useState({
    nombre: '',
    contacto: '',
    creadopor: '',
    fechacreacion: ''
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      // Envía los datos al backend
      const response = await axios.post(`${BASE_URL}/api/proveedores/`, formData);
      alert('Proveedor registrado con éxito!');
      setFormData({
        nombre: '',
        contacto: '',
        creadopor: '',
        fechacreacion: ''
      });
    } catch (error: any) {
      alert('Error: ' + (error.response?.data?.error || 'Error desconocido'));
    }
  };

  return (
    <div className="form-container">
    <h2>Registro</h2>
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label >Nombre completo</label>
        <input type="text" 
               id="nombre" 
               name="nombre" 
               value={formData.nombre}
               onChange={e => setFormData({ ...formData, nombre: e.target.value })}
               required 
        />
      </div>

      <div className="form-group">
        <label >Contacto</label>
        <input type="text" 
               id="contacto" 
               name="contacto" 
               value={formData.contacto}
               onChange={e => setFormData({ ...formData, contacto: e.target.value })}
               required 
        />
      </div>

      <button type="submit" className="btn">Registrar</button>
    </form>

  </div>

  );


}

export default Proveedores;