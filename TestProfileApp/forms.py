from django import forms
from TestProfileApp.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields= ["FirstName", "LastName", "ProfileImagePath"]
