# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Backups(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    realizadopor = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='RealizadoPor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Backups'


class Bitacora(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuarioid = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='UsuarioId', blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    tablaafectada = models.CharField(db_column='TablaAfectada', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    registroid = models.IntegerField(db_column='RegistroId', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bitacora'


class Clientes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes'


class Configuracionimpuestos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2)  # Field name made lowercase.
    configuradopor = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ConfiguradoPor')  # Field name made lowercase.
    fechaconfiguracion = models.DateTimeField(db_column='FechaConfiguracion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfiguracionImpuestos'


class Configuracionprecios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    preciohora = models.DecimalField(db_column='PrecioHora', max_digits=10, decimal_places=2)  # Field name made lowercase.
    margen = models.DecimalField(db_column='Margen', max_digits=5, decimal_places=2)  # Field name made lowercase.
    configuradopor = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ConfiguradoPor')  # Field name made lowercase.
    fechaconfiguracion = models.DateTimeField(db_column='FechaConfiguracion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfiguracionPrecios'


class Cotizaciones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ordenid = models.ForeignKey('Ordenesservicio', models.DO_NOTHING, db_column='OrdenId')  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aprobada = models.BooleanField(db_column='Aprobada', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cotizaciones'


class Diagnosticosiniciales(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ordenid = models.ForeignKey('Ordenesservicio', models.DO_NOTHING, db_column='OrdenId')  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiagnosticosIniciales'


class Diagnosticostecnicos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ordenid = models.ForeignKey('Ordenesservicio', models.DO_NOTHING, db_column='OrdenId')  # Field name made lowercase.
    detalle = models.TextField(db_column='Detalle', db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiagnosticosTecnicos'


class Direcciones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    canton = models.CharField(db_column='Canton', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Direcciones'


class Facturas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ordenid = models.ForeignKey('Ordenesservicio', models.DO_NOTHING, db_column='OrdenId')  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impuesto = models.DecimalField(db_column='Impuesto', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Facturas'


class Modelosmotor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    especificaciones = models.TextField(db_column='Especificaciones', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModelosMotor'


class Motores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    clienteid = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ClienteId')  # Field name made lowercase.
    modeloid = models.ForeignKey(Modelosmotor, models.DO_NOTHING, db_column='ModeloId')  # Field name made lowercase.
    numeroserie = models.CharField(db_column='NumeroSerie', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Motores'


class Movimientosinventario(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    productoid = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ProductoId')  # Field name made lowercase.
    ordenid = models.ForeignKey('Ordenesservicio', models.DO_NOTHING, db_column='OrdenId', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovimientosInventario'


class Ordenesservicio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    motorid = models.ForeignKey(Motores, models.DO_NOTHING, db_column='MotorId')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    tecnicoid = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='TecnicoId', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrdenesServicio'


class Pagos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    facturaid = models.ForeignKey(Facturas, models.DO_NOTHING, db_column='FacturaId')  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=10, decimal_places=2)  # Field name made lowercase.
    metodopago = models.CharField(db_column='MetodoPago', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pagos'


class Productos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.
    stockminimo = models.IntegerField(db_column='StockMinimo', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Productos'


class Proveedores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creadopor = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='CreadoPor')  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='FechaCreacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedores'


class Roles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Sesiones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usuarioid = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='UsuarioId')  # Field name made lowercase.
    token = models.CharField(db_column='Token', unique=True, max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    ultimaactividad = models.DateTimeField(db_column='UltimaActividad', blank=True, null=True)  # Field name made lowercase.
    activa = models.BooleanField(db_column='Activa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sesiones'


class Usuarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    rolid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RolId')  # Field name made lowercase.
    direccionid = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='DireccionId', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin', blank=True, null=True)  # Field name made lowercase.
    issuperuser = models.BooleanField(db_column='IsSuperuser', blank=True, null=True)  # Field name made lowercase.
    isstaff = models.BooleanField(db_column='IsStaff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'
