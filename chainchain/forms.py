from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    phoneNumber = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', ]


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    class Meta:
        model = Profile
        fields = ['username', 'location','phone_number', 'email', 'bio', 'dp', ]

