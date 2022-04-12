from django.forms import ClearableFileInput


class FileUploadInput(ClearableFileInput):
    template_name = "bulma/widgets/file_upload_input.html"
