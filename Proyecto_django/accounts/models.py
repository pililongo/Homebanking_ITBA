from django.db import models
from clients.models import Cliente

# Create your models here.

class TipoCuenta(models.Model):
    cuenta_id = models.AutoField(primary_key=True)
    account_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, db_column="customer_id", on_delete = models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()
    cuenta = models.ForeignKey(TipoCuenta, on_delete = models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cuenta'