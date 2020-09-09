from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CreateUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CreateUser
        fields = ('email','roles',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CreateUser
        fields = ('email','roles',)

class PublicUserCreationForm(UserCreationForm):

    
    class Meta(UserCreationForm):
        model = CreateUser
        fields = ('email','first_name','last_name','roles',)