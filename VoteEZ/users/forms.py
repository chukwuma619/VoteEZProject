from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.views import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterForm(UserCreationForm):
    # Form for handing user registration

    password2 = forms.CharField(
        label=_("Confirm password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email',)
        field_classes = {'email': forms.EmailField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].widget = forms.TextInput(attrs={
            "id": "last_name",
            'class': "w-full h-9 rounded pl-2 mt-2 border-none outline outline-1 outline-blue-600 focus:ring-2"
                     " placeholder:text-sm",
            "autocomplete": "family-name",
            "placeholder": "Enter your last name",
        })

        self.fields['first_name'].widget = forms.TextInput(attrs={
            "id": "first_name",
            'class': "w-full h-9 rounded pl-2 mt-2 border-none outline outline-1 outline-blue-600 focus:ring-2"
                     " placeholder:text-sm",
            "autocomplete": "given-name",
            "placeholder": "Enter your first name",
        })

        self.fields['email'].widget = forms.EmailInput(attrs={
            "id": "email",
            'class': "w-full h-9 rounded pl-2 mt-2 border-none outline outline-1 outline-blue-600 focus:ring-2"
                     " placeholder:text-sm",
            "autocomplete": "email",
            "placeholder": "Enter your email",
        })

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            "id": "password1",
            'class': "w-full mt-2 h-9 rounded pl-2 border-none outline outline-blue-600 outline-1 focus:ring-2"
                     " placeholder:text-sm ",
            "autocomplete": "new-password",
            "placeholder": "Enter password",
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            "id": "password2",
            'class': "w-full mt-2 h-9 rounded pl-2 border-none outline outline-blue-600 outline-1 focus:ring-2"
                     " placeholder:text-sm",
            "autocomplete": "new-password",
            "placeholder": "Enter confirm password",
        })

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        # Check if a user with the same username already exists
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already taken. Please choose a different email.')
        return cleaned_data


class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(label="Email",
                             widget=forms.TextInput(
                                 attrs={"autofocus": True,
                                        'name': "email"}))
    error_messages = {
        "invalid_login": "Invalid username or password. Please check your credentials and try again.",
        "inactive": "This account is inactive.",
    }

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
