from django.forms import ImageField as DjangoImageField
from django.forms import FileField as DjangoFileField

from plugins.crispy_bulma.crispy_bulma.widgets import FileUploadInput


class ImageField(DjangoImageField):
    widget = FileUploadInput()


class FileField(DjangoFileField):
    widget = FileUploadInput()
