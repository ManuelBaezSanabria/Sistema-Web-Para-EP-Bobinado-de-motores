from django.db import models

class DiagnosticosTecnicos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    orden = models.ForeignKey(
        'ordenes.OrdenesServicio',  # Referencia lazy
        models.DO_NOTHING, 
        db_column='OrdenId',
        related_name='diagnosticos'
    )
    detalle = models.TextField(db_column='Detalle')
    creadoen = models.DateTimeField(db_column='CreadoEn', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'DiagnosticosTecnicos'
        ordering = ['-creadoen']

    def __str__(self):
        return f"Diagnóstico #{self.id} - Orden #{self.orden_id}"
    
    @property
    def resumen(self):
        """Retorna un resumen del detalle (primeros 100 caracteres)"""
        if len(self.detalle) > 100:
            return self.detalle[:100] + '...'
        return self.detalle
