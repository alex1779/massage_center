# import form class from django
from django import forms
from .models import Reservation
from django.contrib.admin.widgets import AdminDateWidget

class XYZ_DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"
    #input_type = "datetime"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

# create a ModelForm
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {
            'service'  :   forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            'hour'  :   forms.Select(attrs={'class':'form-control'})
        }
