import React, { useState } from 'react';
import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

const Registro = () => {
    const [formData, setFormData] = useState({
        nombre: '',
        email: '',
        telefono: '',
        password: '',
        confirm_password: ''
    });

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${BASE_URL}/api/auth/registro/`, formData);
            alert('Registro exitoso! Token: ' + response.data.token);
            localStorage.setItem('token', response.data.token);
        } catch (error: any) {
            alert('Error: ' + (error.response?.data?.error || 'Error desconocido'));
        }
    };

    return (
        <div style={{ maxWidth: '400px', margin: '20px auto', padding: '20px', border: '1px solid #ccc' }}>
            <h2>Registro de Cliente</h2>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '10px' }}>
                    <input
                        type="text"
                        placeholder="Nombre completo"
                        value={formData.nombre}
                        onChange={e => setFormData({...formData, nombre: e.target.value})}
                        required
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                <div style={{ marginBottom: '10px' }}>
                    <input
                        type="email"
                        placeholder="Email"
                        value={formData.email}
                        onChange={e => setFormData({...formData, email: e.target.value})}
                        required
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                <div style={{ marginBottom: '10px' }}>
                    <input
                        type="tel"
                        placeholder="Teléfono"
                        value={formData.telefono}
                        onChange={e => setFormData({...formData, telefono: e.target.value})}
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                <div style={{ marginBottom: '10px' }}>
                    <input
                        type="password"
                        placeholder="Contraseña"
                        value={formData.password}
                        onChange={e => setFormData({...formData, password: e.target.value})}
                        required
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                <div style={{ marginBottom: '20px' }}>
                    <input
                        type="password"
                        placeholder="Confirmar contraseña"
                        value={formData.confirm_password}
                        onChange={e => setFormData({...formData, confirm_password: e.target.value})}
                        required
                        style={{ width: '100%', padding: '8px' }}
                    />
                </div>
                <button type="submit" style={{ padding: '10px 20px', backgroundColor: '#007bff', color: 'white', border: 'none' }}>
                    Registrarse
                </button>
            </form>
        </div>
    );
};

export default Registro;