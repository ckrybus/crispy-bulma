from django.forms import ClearableFileInput
from django.forms import EmailInput as DjangoEmailInput


class EmailInput(DjangoEmailInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        classes = context["widget"]["attrs"]["class"].split()

        if "emailinput" in classes:
            # Django includes this class; it's not the end of the world to keep it
            # but we remove it to keep things clean and avoid accidental styling
            classes.remove("emailinput")

        # The correct class to use with Bulma is "input", so we just need to add it
        classes.append("input")
        context["widget"]["attrs"]["class"] = " ".join(classes)

        return context


class FileUploadInput(ClearableFileInput):
    template_name = 'bulma/widgets/file_upload_input.html'
