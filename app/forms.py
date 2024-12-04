# from django import forms
# from .models import Project
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['title', 'description', 'image']


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

# portfolio/forms.py
from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name', 'profession', 'bio', 'skills', 'experience', 'profile_image']
