from django.forms import FileField as DjangoFileField
from django.forms import ImageField as DjangoImageField

from crispy_bulma.widgets import FileUploadInput


class ImageField(DjangoImageField):
    widget = FileUploadInput()


class FileField(DjangoFileField):
    widget = FileUploadInput()
