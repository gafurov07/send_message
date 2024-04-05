from django import forms
from django.contrib.auth.hashers import make_password

from apps.models import CustomUser


class CustomUserCreateModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean_confirm_password(self, *args, **kwargs):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError('Parol notogi tasdiqlandi!')
        return confirm_password

    def clean(self):
        data = super().clean()
        data['password'] = make_password(data.get('password'))
        return data

