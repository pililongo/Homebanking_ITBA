from django.db import models
from django.contrib.auth.models import User
from clients.models import Cliente
# Create your models here.

class Relation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)