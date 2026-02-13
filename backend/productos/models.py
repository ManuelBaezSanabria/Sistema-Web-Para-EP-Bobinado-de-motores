from django.db import models

class Productos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100)
    categoria = models.CharField(db_column='Categoria', max_length=50, blank=True, null=True)
    stock = models.IntegerField(db_column='Stock', default=0)
    stockminimo = models.IntegerField(db_column='StockMinimo', default=0)
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2, blank=True, null=True)
    activo = models.BooleanField(db_column='Activo', default=True)

    class Meta:
        managed = False
        db_table = 'Productos'

    def __str__(self):
        return self.nombre
    
    @property
    def necesita_reposicion(self):
        """Retorna True si el stock está por debajo del mínimo"""
        return self.stock <= self.stockminimo
