from django.forms import ModelForm
from todolist.models import tasklist

class taskform(ModelForm):
    class Meta:
        model = tasklist
        fields = [
            'title',
            'description'
        ]