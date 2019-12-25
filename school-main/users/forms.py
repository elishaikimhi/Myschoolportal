from django import forms
from django.contrib.auth.forms import UserCreationForm  # , UserChangeForm
from .models import User


class CostumeLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# class CostumeSinupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = UserCreationForm.Meta.fields + ('is_teacher',)


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = UserChangeForm.Meta.fields


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        if commit:
            user.save()
        return user


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        if commit:
            user.save()
        return user
