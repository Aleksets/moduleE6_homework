from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from chat.models import ChatUser


# Форма для регистрации нового пользователя
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )

    # метод проверки на существование введенного при регистрации имени пользователя
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError("This username already exists! Come up with a different username")
    #     return username


# Форма для изменения имени пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


# Форма для изменения аватара пользователя
class ChatUserEditForm(forms.ModelForm):
    class Meta:
        model = ChatUser
        fields = ['avatar']
