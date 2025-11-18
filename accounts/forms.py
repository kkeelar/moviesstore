from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError

from .models import Profile


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1',
        'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if not avatar:
            return avatar

        if avatar.size > 2 * 1024 * 1024:  # 2MB limit
            raise ValidationError('Avatar file too large (max 2MB).')

        content_type = avatar.content_type or ''
        if not content_type.startswith('image/'):
            raise ValidationError('Please upload a valid image file.')

        return avatar
