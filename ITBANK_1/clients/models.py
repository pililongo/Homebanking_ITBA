from django.db import models
from bank.models import Sucursal, Direcciones

# Create your models here.

class TipoCliente(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField()
    branch_id = models.ForeignKey(Sucursal,db_column = 'branch_id', on_delete = models.CASCADE)
    client = models.ForeignKey(TipoCliente, on_delete = models.DO_NOTHING)
    address_id = models.ForeignKey(Direcciones,db_column = 'address_id', on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.customer_name} {self.customer_surname}'

    class Meta:
        managed = False
        db_table = 'cliente'