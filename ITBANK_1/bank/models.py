from django.db import models

# Create your models here.

class Direcciones(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.TextField()
    number = models.TextField()  # This field type is a guess.
    city = models.TextField()
    province = models.TextField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.IntegerField()
    branch_name = models.TextField()
    address = models.ForeignKey(Direcciones, db_column= 'address_id', on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.ForeignKey(Sucursal, on_delete = models.CASCADE)
    address = models.ForeignKey(Direcciones, on_delete = models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empleado'


class Movimientos(models.Model):
    transaction_id = models.AutoField(primary_key=True, blank=True, null=False)
    account_number = models.IntegerField()
    amount = models.IntegerField()
    transaction_type = models.TextField()
    transaction_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'