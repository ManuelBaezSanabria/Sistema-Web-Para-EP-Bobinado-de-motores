import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../../api.ts";
import './../../styles/auth.css';

const Login: React.FC = () => {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [error, setError] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    
    try {
      const response = await loginUser({ email, password });
      localStorage.setItem("userSession", JSON.stringify(response));
      navigate("/cliente-dashboard");
    } catch (error: any) {
      setError("Error al iniciar sesión: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-page">
      <h1 className="auth-page-title">EP Bobinado</h1>
      
      <div className="auth-container">
        <div className="auth-header">
          <h2>Iniciar Sesión</h2>
          <p>Ingresa tus credenciales para continuar</p>
        </div>

        {error && (
          <div className="alert alert-error">
            {error}
          </div>
        )}

        <form className="auth-form" onSubmit={handleLogin}>
          <div className="form-group">
            <label>Correo Electrónico</label>
            <input 
              type="email" 
              placeholder="tu@email.com" 
              value={email} 
              onChange={e => setEmail(e.target.value)} 
              required 
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label>Contraseña</label>
            <input 
              type="password" 
              placeholder="••••••••" 
              value={password} 
              onChange={e => setPassword(e.target.value)} 
              required 
              disabled={loading}
            />
          </div>

          <button 
            type="submit" 
            className="btn-primary btn-block"
            disabled={loading}
          >
            {loading ? "Cargando..." : "Entrar"}
          </button>
        </form>

        <div className="auth-footer">
          <p>
            ¿No tienes cuenta? <a href="/registro">Regístrate</a>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;