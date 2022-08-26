from clients.models import Cliente
from login.models import Relation
from django.contrib.auth.models import User


def get_loged_client(request):
    user = request.user
    cliente_id = Relation.objects.filter(user_id=user.pk).first().cliente_id
    return Cliente.objects.filter(customer_id= cliente_id).first()

def get_loged_user(cliente):
    user_id = Relation.objects.filter(cliente_id=cliente.pk).first().user_id
    return User.objects.filter(pk=user_id).first()