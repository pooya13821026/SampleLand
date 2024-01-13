from django import forms
from django.core.exceptions import ValidationError

from accounting.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','mobile','biography','address','avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3,
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 3,
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'first_name': 'نام',
            'last_name': ' نام خانوادگی',
            'email': 'ایمیل',
            'mobile': 'موبایل',
            'biography': 'بیوگرافی',
            'address': 'آدرس',
            'avatar': 'تصویر پروفایل',
        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    new_password = forms.CharField(
        label='کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور وارد شده با تکرار آن مطابقت ندارد')
