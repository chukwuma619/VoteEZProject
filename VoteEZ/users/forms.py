from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from django.contrib.auth.views import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    # Form for handing user registration
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(label="Email", widget=forms.TextInput(attrs={"autofocus": True,
                                                                          'name': "email"}
                                                                   ))

    def __init__(self, request=None, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(request=None, *args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'type': 'email',
            "id": "email",
            'class': "w-full h-9 rounded pl-2 mt-2 border-none outline outline-1 outline-blue-600 focus:ring-2"
                     " placeholder:text-sm",
            'name': 'email',
            "autocomplete": "email",
            "placeholder": "Enter your email",
        })

        self.fields['password'].widget = forms.TextInput(attrs={
            'type': "password",
            "id": "password",
            'class': "w-full h-9 rounded pl-2 border-none outline outline-blue-600 outline-1 focus:ring-2"
                     " placeholder:text-sm",
            'name': 'password',
            "placeholder": "Enter password",
            'autocomplete': "current-password",
        })
