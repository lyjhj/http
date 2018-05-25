from django.forms import forms


class FileUploadForm(forms.Form):
    # title = forms.CharField(max_length=50)
    my_file = forms.FileField()