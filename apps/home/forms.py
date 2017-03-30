from django import forms
from apps.home.models import UsersAccount

class UsersAccountForm(forms.ModelForm):
    class Meta:
        model = UsersAccount
        fields = ('firstname','lastname',)