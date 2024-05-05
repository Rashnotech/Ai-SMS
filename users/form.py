from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class UserRegister(UserCreationForm):
    """Registration form attributes"""
    email = forms.EmailField(required=False)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput())

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput()
    )
    password_strength = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name',
                  'email', 'telephone',
                  'address', 'job_title',
                  'company', 'country')


class AuthenticationForm(forms.Form):
    """Authentication form for user"""
    email = forms.EmailField(
        label='Enter email',
        widget=forms.EmailInput())
    password = forms.CharField(
        label='Enter password',
        strip=False,
        widget=forms.PasswordInput())

    def __init__(self, request=None, *args, **kwargs):
        """Initialization"""
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)  # Remove the 'username' field from the form
        self.order_fields(['email', 'password'])

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user = authenticate(
                self.request, email=email, password=password
            )
            if self.user is None:
                raise forms.ValidationError(
                    "Invalid user credentials."
                )
        return self.cleaned_data

    def get_user(self):
        return self.user

