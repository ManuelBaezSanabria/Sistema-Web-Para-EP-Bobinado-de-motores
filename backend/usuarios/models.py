from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
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

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        
        # Crear username automáticamente si no existe
        if 'username' not in extra_fields:
            extra_fields['username'] = email.split('@')[0]
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('issuperuser', True)
        extra_fields.setdefault('isstaff', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
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
    
    @property
    def password(self):
        return self.passwordhash
    
    @password.setter
    def password(self, value):
        self.passwordhash = value
    
    last_login = property(
        lambda self: self.lastlogin,
        lambda self, value: setattr(self, 'lastlogin', value)
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']
    
    objects = UsuarioManager()

    class Meta:
        managed = False
        db_table = 'Usuarios'

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.passwordhash = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.passwordhash)
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
    
    def has_perm(self, perm, obj=None):
        return self.issuperuser
    
    def has_module_perms(self, app_label):
        return self.issuperuser
    
    @property
    def is_superuser(self):
        return self.issuperuser
    
    @property
    def is_staff(self):
        return self.isstaff