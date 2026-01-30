/* =========================================================
   CREACIÓN DE BASE DE DATOS
   ========================================================= */
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'EPBobinadoDB')
BEGIN
    CREATE DATABASE EPBobinadoDB;
END
GO

USE EPBobinadoDB;
GO

/* =========================================================
   SEGURIDAD Y USUARIOS
   ========================================================= */
CREATE TABLE Roles (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(50) NOT NULL UNIQUE,
    Descripcion NVARCHAR(255)
);
GO

CREATE TABLE Direcciones (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Provincia NVARCHAR(100) NOT NULL,
    Canton NVARCHAR(100) NOT NULL,
    Distrito NVARCHAR(100) NOT NULL,
    CodigoPostal NVARCHAR(20),
    Descripcion NVARCHAR(255),
    CreadoEn DATETIME2 DEFAULT SYSDATETIME()
);
GO

CREATE TABLE Usuarios (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(255) NOT NULL,
    RolId INT NOT NULL,
    DireccionId INT NULL,
    Telefono NVARCHAR(20) NULL,
    Activo BIT DEFAULT 1,
    CreadoEn DATETIME2 DEFAULT SYSDATETIME(),

    -- Campos para Django auth
    Username NVARCHAR(150) NULL,
    LastLogin DATETIME2 NULL,
    IsSuperuser BIT DEFAULT 0,
    IsStaff BIT DEFAULT 0,
    
    CONSTRAINT FK_Usuarios_Roles
        FOREIGN KEY (RolId) REFERENCES Roles(Id),
    CONSTRAINT FK_Usuarios_Direcciones
        FOREIGN KEY (DireccionId) REFERENCES Direcciones(Id)
);
GO

CREATE TABLE Sesiones (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    UsuarioId INT NOT NULL,
    Token NVARCHAR(255) NOT NULL UNIQUE,
    Inicio DATETIME2 DEFAULT SYSDATETIME(),
    UltimaActividad DATETIME2,
    Activa BIT DEFAULT 1,
    CONSTRAINT FK_Sesiones_Usuarios
        FOREIGN KEY (UsuarioId) REFERENCES Usuarios(Id)
);
GO

/* =========================================================
   CLIENTES Y MOTORES
   ========================================================= */

CREATE TABLE Clientes (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Telefono NVARCHAR(20),
    Email NVARCHAR(100),
    Direccion NVARCHAR(255),
    Activo BIT DEFAULT 1,
    CreadoEn DATETIME2 DEFAULT SYSDATETIME()
);
GO

CREATE TABLE ModelosMotor (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Especificaciones NVARCHAR(MAX)
);
GO

CREATE TABLE Motores (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    ClienteId INT NOT NULL,
    ModeloId INT NOT NULL,
    NumeroSerie NVARCHAR(100),
    CreadoEn DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Motores_Clientes
        FOREIGN KEY (ClienteId) REFERENCES Clientes(Id),
    CONSTRAINT FK_Motores_Modelos
        FOREIGN KEY (ModeloId) REFERENCES ModelosMotor(Id)
);
GO

/* =========================================================
   ÓRDENES DE SERVICIO
   ========================================================= */

CREATE TABLE OrdenesServicio (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    MotorId INT NOT NULL,
    Estado NVARCHAR(50) NOT NULL,
    TecnicoId INT NULL,
    CreadoEn DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Ordenes_Motores
        FOREIGN KEY (MotorId) REFERENCES Motores(Id),
    CONSTRAINT FK_Ordenes_Tecnicos
        FOREIGN KEY (TecnicoId) REFERENCES Usuarios(Id)
);
GO

CREATE TABLE DiagnosticosIniciales (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    OrdenId INT NOT NULL,
    Descripcion NVARCHAR(MAX) NOT NULL,
    CreadoEn DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_DiagnosticoInicial_Orden
        FOREIGN KEY (OrdenId) REFERENCES OrdenesServicio(Id)
);
GO

CREATE TABLE DiagnosticosTecnicos (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    OrdenId INT NOT NULL,
    Detalle NVARCHAR(MAX) NOT NULL,
    CreadoEn DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_DiagnosticoTecnico_Orden
        FOREIGN KEY (OrdenId) REFERENCES OrdenesServicio(Id)
);
GO

/* =========================================================
   INVENTARIO
   ========================================================= */

CREATE TABLE Productos (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Categoria NVARCHAR(50),
    Stock INT DEFAULT 0,
    StockMinimo INT DEFAULT 0,
    Precio DECIMAL(10,2),
    Activo BIT DEFAULT 1
);
GO

CREATE TABLE Proveedores (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Contacto NVARCHAR(100),
    CreadoPor INT NOT NULL,
    FechaCreacion DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Proveedores_Usuarios
        FOREIGN KEY (CreadoPor) REFERENCES Usuarios(Id)
);
GO

CREATE TABLE MovimientosInventario (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    ProductoId INT NOT NULL,
    OrdenId INT NULL,
    Tipo NVARCHAR(10) CHECK (Tipo IN ('ENTRADA','SALIDA')),
    Cantidad INT NOT NULL,
    Fecha DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_MovInv_Producto
        FOREIGN KEY (ProductoId) REFERENCES Productos(Id),
    CONSTRAINT FK_MovInv_Orden
        FOREIGN KEY (OrdenId) REFERENCES OrdenesServicio(Id)
);
GO

/* =========================================================
   COTIZACIÓN Y FACTURACIÓN
   ========================================================= */

CREATE TABLE Cotizaciones (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    OrdenId INT NOT NULL,
    Total DECIMAL(10,2),
    Aprobada BIT DEFAULT 0,
    CreadoEn DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Cotizaciones_Orden
        FOREIGN KEY (OrdenId) REFERENCES OrdenesServicio(Id)
);
GO

CREATE TABLE Facturas (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    OrdenId INT NOT NULL,
    Total DECIMAL(10,2),
    Impuesto DECIMAL(10,2),
    Fecha DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Facturas_Orden
        FOREIGN KEY (OrdenId) REFERENCES OrdenesServicio(Id)
);
GO

CREATE TABLE Pagos (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FacturaId INT NOT NULL,
    Monto DECIMAL(10,2) NOT NULL,
    MetodoPago NVARCHAR(50),
    Fecha DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Pagos_Facturas
        FOREIGN KEY (FacturaId) REFERENCES Facturas(Id)
);
GO

/* =========================================================
   CONFIGURACIÓN (YA RELACIONADA)
   ========================================================= */

CREATE TABLE ConfiguracionPrecios (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    PrecioHora DECIMAL(10,2) NOT NULL,
    Margen DECIMAL(5,2) NOT NULL,
    ConfiguradoPor INT NOT NULL,
    FechaConfiguracion DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_ConfigPrecios_Usuarios
        FOREIGN KEY (ConfiguradoPor) REFERENCES Usuarios(Id)
);
GO

CREATE TABLE ConfiguracionImpuestos (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Porcentaje DECIMAL(5,2) NOT NULL,
    ConfiguradoPor INT NOT NULL,
    FechaConfiguracion DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_ConfigImpuestos_Usuarios
        FOREIGN KEY (ConfiguradoPor) REFERENCES Usuarios(Id)
);
GO

/* =========================================================
   BITÁCORA DE AUDITORÍA
   ========================================================= */

CREATE TABLE Bitacora (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    UsuarioId INT NULL,
    Accion NVARCHAR(100) NOT NULL,
    TablaAfectada NVARCHAR(100),
    RegistroId INT,
    Fecha DATETIME2 DEFAULT SYSDATETIME(),
    CONSTRAINT FK_Bitacora_Usuarios
        FOREIGN KEY (UsuarioId) REFERENCES Usuarios(Id)
);
GO

/* =========================================================
   BACKUPS
   ========================================================= */

CREATE TABLE Backups (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Archivo NVARCHAR(255),
    Fecha DATETIME2 DEFAULT SYSDATETIME(),
    RealizadoPor INT,
    CONSTRAINT FK_Backups_Usuarios
        FOREIGN KEY (RealizadoPor) REFERENCES Usuarios(Id)
);
GO

/* =========================================================
   INSERTAR DATOS DE PRUEBA
   ========================================================= */

INSERT INTO Roles (Nombre, Descripcion) VALUES
('Administrador', 'Acceso total al sistema'),
('Técnico', 'Realiza diagnósticos y reparaciones'),
('Recepcionista', 'Registra órdenes y clientes'),
('Cliente', 'Acceso limitado a su información');