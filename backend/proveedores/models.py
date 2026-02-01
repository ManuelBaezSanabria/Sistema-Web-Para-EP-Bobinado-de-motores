from django.db import models

# Create your models here.
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

class Proveedores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS') 
    contacto = models.CharField(db_column='Contacto', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True) 
    creadopor = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='CreadoPor')  
    fechacreacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Proveedores'