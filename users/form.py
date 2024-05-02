from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegister(UserCreationForm):
    """Registration form attributes"""
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(required=True)
    job_title = forms.CharField(required=True)
    company = forms.CharField(required=True)
    country = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """Authentication form for user"""
    email = forms.EmailField(
        label='Enter email',
        widget=forms.EmailInput(attrs={
            'class': 'border rounded-md col-span-2\
            text-sm text-slate-600 focus:transition-all\
            outline-none px-4 py-3', 'placeholder': 'someone@workplace.com'
        }))
    password = forms.CharField(
        label='Enter password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'border rounded-md col-span-2\
            text-sm text-slate-600 focus:transition-all\
            outline-none px-4 py-3', 'placeholder': '********'
        }))

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)  # Remove the 'username' field from the form
        self.order_fields(['email', 'password'])

