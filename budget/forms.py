from django import forms

from .models import Budget
from budget.utils.validation import is_valid_mime_type


class BudgetForm(forms.ModelForm):

    files = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'id': 'files',
                'accept': '.pdf, .png, .jpg, .jpeg, .doc, .docx, .xls, .xlsx',
            }
        ),
        label='Documentos',
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
        labels = {
            'full_name': 'Nome completo',
            'email': 'E-mail',
            'whatsapp_number': 'WhatsApp',
            'source_language': 'Idioma de Origem',
            'target_language': 'Idioma de Destino',
        }

    def clean_files(self):
        files = self.files.getlist('files')

        for file in files:
            if not is_valid_mime_type(file):
                self.add_error('files', 'Tipo de arquivo inválido.')

        return files
