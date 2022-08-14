from django.db import models
from clients.models import Cliente
# Create your models here.

class MarcaTarjeta(models.Model):
    brand_id = models.AutoField(primary_key=True)
    card_brand = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField(unique=True)
    card_cvv = models.IntegerField()
    card_grant_date = models.TextField()  # This field type is a guess.
    card_expiration_date = models.TextField()  # This field type is a guess.
    card_type = models.TextField()
    brand = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'