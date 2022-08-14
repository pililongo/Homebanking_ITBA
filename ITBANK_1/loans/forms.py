from django import forms
from .models import Prestamo
from django.utils.translation import gettext_lazy as _

class LoansForm(forms.ModelForm):
    loan_type = forms.ChoiceField(
        label=_("Tipo de prestamo:"),
        choices = [
            ('HIPOTECARIO', 'HIPOTECARIO'),
            ('PERSONAL', 'PERSONAL'),
            ('PRENDARIO', 'PRENDARIO'),
        ]
    )

    loan_date = forms.CharField(
        label= _("Fecha de inicio:"),
        # help_text=_("Formato: aaaa-mm-dd"),
    )

    loan_total = forms.IntegerField(
        label= _("Monto:"),
    )
    class Meta:
        model = Prestamo
        fields = ['loan_type','loan_date','loan_total']
