from django.forms import ModelForm
from .models import Note


class EditForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
