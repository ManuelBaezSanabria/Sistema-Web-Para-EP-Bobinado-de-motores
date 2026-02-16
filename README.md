# Sistema-Web-Para-EP-Bobinado-de-motores

Sistema web completo para la gestión de un taller de bobinado de motores eléctricos. Incluye autenticación de usuarios, registro de clientes, gestión de inventario, órdenes de servicio, y más.

## Arquitectura

- Backend: Django REST Framework (Python)
- Frontend: React + TypeScript
- Base de Datos: SQL Server
- Autenticación: Token-based (Django REST Framework)

## Estructura del Proyecto

- Sistema-Web-Para-EP-Bobinado-de-motores/
  - backend/
      - usuarios (Implementado)
      - proveedores (Implementado)
      - clientes (Por implementar)
      - motores (Por implementar)
      - inventario (Por implementar)
      - ordenes (Por implementar)
      - facturacion (Por implementar)
      - backend (Configuración del proyecto)
  - frontend
      -  src/
          - components/
          - App.tsx
          - Index.tsx
      - package.json
- venv (Entorno virtual de Python)
- README.nd
  
## Software necesario 

- Python 3.11+
- Node.js 18+
- SQL Server 2019+
- Git
- Visual Studio Code (recomendado)

## Configuración Inicial (Primera Vez)

1. Clonar el repositorio
     ```bash
       git clone https://github.com/ManuelBaezSanabria/Sistema-Web-Para-EP-Bobinado-de-motores
   
       cd Sistema-Web-Para-EP-Bobinado-de-motores

2. Ejecutar en SQL Server Management Studio (EPBobinadoDB.sql)
3. Configurar Backend (Django)
    ```bash
      # Crear entorno virtual
      python -m venv venv
        
      # Activar entorno virtual
      # Windows:
      venv\Scripts\activate
      # Mac/Linux:
      source venv/bin/activate
        
      # Instalar dependencias desde requirements.txt
      pip install -r requirements.txt
        
      # Navegar a la carpeta backend
      cd backend
        
      # Aplicar migraciones
      python manage.py migrate
    ```

4. Configurar Frontend (React)
    ```bash
      # Volver a la raíz del proyecto
      cd ..
      
      # Navegar a frontend
      cd frontend
      
      # Instalar dependencias
      npm install
    ```

## Ejecutar el Proyecto

### Terminal 1: Backend (Django)
    
  ```bash
  cd backend

  python manage.py migrate  

  python manage.py runserver
  ```
Verificar en: http://localhost:8000/api/auth/registro/

### Terminal 2: Frontend (React)

  ```bash
  cd frontend

  npm start
  ```

Verificar en: http://localhost:3000


