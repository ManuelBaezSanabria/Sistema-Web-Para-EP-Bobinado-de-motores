from django.db import models
from django.utils import timezone

class Direcciones(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    provincia = models.CharField(db_column='Provincia', max_length=100)
    canton = models.CharField(db_column='Canton', max_length=100)
    distrito = models.CharField(db_column='Distrito', max_length=100)
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)
    creadoen = models.DateTimeField(db_column='CreadoEn', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Direcciones'

class Roles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=50)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Roles'


class Usuario(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    id = models.AutoField(db_column='Id', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100)
    email = models.EmailField(db_column='Email', unique=True, max_length=100)
    passwordhash = models.CharField(db_column='PasswordHash', max_length=255)
    rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RolId')
    direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='DireccionId', blank=True, null=True)
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)
    activo = models.BooleanField(db_column='Activo', default=True)
    creadoen = models.DateTimeField(db_column='CreadoEn', auto_now_add=True)
    username = models.CharField(db_column='Username', max_length=150, unique=True, blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='LastLogin', blank=True, null=True)
    issuperuser = models.BooleanField(db_column='IsSuperuser', default=False)
    isstaff = models.BooleanField(db_column='IsStaff', default=False)

class Modelosmotor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    especificaciones = models.TextField(db_column='Especificaciones', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModelosMotor'

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

class Motores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    clienteid = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ClienteId')  # Field name made lowercase.
    modeloid = models.ForeignKey(Modelosmotor, models.DO_NOTHING, db_column='ModeloId')  # Field name made lowercase.
    numeroserie = models.CharField(db_column='NumeroSerie', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Motores'
        
class OrdenesServicio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    motorid = models.ForeignKey(Motores, models.DO_NOTHING, db_column='MotorId')  # Field name made lowercase. rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RolId')
    estado = models.CharField(db_column='Estado', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    tecnicoid = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='TecnicoId', blank=True, null=True)  # Field name made lowercase.
    creadoen = models.DateTimeField(db_column='CreadoEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'OrdenesServicio'

    def __str__(self):
        return f"Orden {self.id} - Estado: {self.estado}"