from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PDFDocument

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        allowed_extensions = ['pdf', 'docx', 'pptx', 'txt']
        extension = file.name.split('.')[-1].lower()
        if extension not in allowed_extensions:
            raise forms.ValidationError('File type not supported.')
        return file
