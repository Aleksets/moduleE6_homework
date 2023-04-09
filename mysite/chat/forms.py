from django import forms
from .models import Room


# Форма создания и редактирования чата
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'users']

    # метод проверки на существование введенного названия чата
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if Room.objects.filter(name=name).exists():
    #         raise forms.ValidationError("This room name is already in use! Come up with a different name")
    #     return name
