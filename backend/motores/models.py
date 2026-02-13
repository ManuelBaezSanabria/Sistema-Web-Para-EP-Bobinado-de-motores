from django.db import models

class ModelosMotor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100)
    especificaciones = models.TextField(db_column='Especificaciones', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ModelosMotor'
        verbose_name = 'Modelo de Motor'
        verbose_name_plural = 'Modelos de Motor'

    def __str__(self):
        return self.nombre


class Motores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    usuario = models.ForeignKey(
        'usuarios.Usuario',  # Referencia lazy
        models.DO_NOTHING,
        db_column='UsuarioId',
        related_name='motores'
    )
    modelo = models.ForeignKey(
        ModelosMotor,
        models.DO_NOTHING,
        db_column='ModeloId',
        related_name='motores'
    )
    numeroserie = models.CharField(db_column='NumeroSerie', max_length=100, blank=True, null=True)
    creadoen = models.DateTimeField(db_column='CreadoEn', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Motores'
        verbose_name = 'Motor'
        verbose_name_plural = 'Motores'
        ordering = ['-creadoen']

    def __str__(self):
        return f"Motor #{self.id} - {self.modelo.nombre} ({self.numeroserie or 'Sin Serie'})"
    
    @property
    def info_completa(self):
        """Retorna información completa del motor"""
        return {
            'id': self.id,
            'modelo': self.modelo.nombre,
            'serie': self.numeroserie,
            'usuario': self.usuario.nombre,
            'email': self.usuario.email
        }
