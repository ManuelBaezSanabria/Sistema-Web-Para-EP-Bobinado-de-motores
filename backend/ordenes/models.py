from django.db import models

class OrdenesServicio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    motorid = models.ForeignKey(
        'motores.Motores',  # Referencia lazy a la app motores
        models.DO_NOTHING, 
        db_column='MotorId',
        related_name='ordenes'
    )
    estado = models.CharField(db_column='Estado', max_length=50)
    tecnicoid = models.ForeignKey(
        'usuarios.Usuario',  # Referencia lazy a la app usuarios
        models.DO_NOTHING, 
        db_column='TecnicoId', 
        blank=True, 
        null=True,
        related_name='ordenes_asignadas'
    )
    creadoen = models.DateTimeField(db_column='CreadoEn', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'OrdenesServicio'
        ordering = ['-creadoen']

    def __str__(self):
        return f"Orden #{self.id} - Estado: {self.estado}"