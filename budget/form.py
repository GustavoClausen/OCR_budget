from django import forms

from .models import Budget


class BudgetForm(forms.ModelForm):

    files = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'id': 'files',
                'accept': '.pdf, .png, .jpg, .jpeg, .doc, .docx, .xls, .xlsx',
            }
        ),
    )

    class Meta:
        model = Budget
        fields = [
            'full_name',
            'email',
            'whatsapp_number',
            'source_language',
            'target_language',
        ]
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Insira seu nome completo',
                    'class': 'form-control',
                    'maxlength': '250',
                    'required': True,
                    'id': 'inputFullName',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Insira um e-mail válido',
                    'class': 'form-control',
                    'required': True,
                    'id': 'inputEmail',
                }
            ),
            'whatsapp_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'id': 'phone',
                }
            ),
            'source_language': forms.Select(
                attrs={
                    'class': 'form-select',
                    'required': True,
                    'id': 'source-language',
                },
            ),
            'target_language': forms.Select(
                attrs={
                    'class': 'form-select',
                    'required': True,
                    'id': 'target-language',
                },
            ),
        }
