from django.forms import EmailField as DjangoEmailField
from django.forms import FileField as DjangoFileField
from django.forms import ImageField as DjangoImageField

from django_crispy_bulma.widgets import EmailInput, FileUploadInput


class EmailField(DjangoEmailField):
    widget = EmailInput()


class ImageField(DjangoImageField):
    widget = FileUploadInput()


class FileField(DjangoFileField):
    widget = FileUploadInput()
