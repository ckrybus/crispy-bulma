# django-crispy-bulma

**This project is an early work in progress. You should not use this package yet, as it is poorly documented and is missing many important features. We'll remove this header when it's ready to use.**

## About

This is a Django application to add `django-crispy-forms` layout objects for [Bulma](https://bulma.io/). 
It is a fork of [crispy-forms-bulma](https://github.com/jhotujec/crispy-forms-bulma) by Jure Hotujec, with the intention 
of adding support for Django 2.0+, as well as for components found in the bulma-extensions library.

## Installation

You can install `django-crispy-bulma` from [PyPI](https://pypi.org/project/django-crispy-bulma/) by running `pip install django-crispy-bulma`. Make sure you also have `django-crispy-forms` installed, as it will not work without it. In order to activate it, you'll need to modify your projects `settings.py` file. 

First, add `django-crispy-bulma` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'crispy_forms',
    'django_crispy_bulma',
    # ...
]
```

Next, add the following to the bottom of the file in order to configure `crispy_forms` to use the **bulma** template pack:
```python
CRISPY_ALLOWED_TEMPLATE_PACKS = (
    "bootstrap",
    "uni_form",
    "bootstrap3",
    "bootstrap4",
    "bulma",
)

CRISPY_TEMPLATE_PACK = "bulma"
```

You may also need to use Layout objects or form objects from `django_crispy_bulma` in order to build certain objects, like the UploadField. See the documentation below for specifics on objects like these.

EmailField
----------

The EmailField looks like this:

![EmailField](https://i.imgur.com/IBioO0Y.gif)

An EmailField can be created simply, like any other field in your form. For example:

```python
from django.forms import Form
from django_crispy_bulma.forms import EmailField

class MyForm(Form):
    my_email = EmailField(
        label="email",
        required=True
    )
```


IconField
---------

If you'd like to render a field with an icon in it, you'll need to make use of the Crispy Forms layout object,
and the `IconField` from our package. See below for an example:

![IconField](https://i.imgur.com/tHsPHrM.png)

```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.forms import Form, CharField

from django_crispy_bulma.layout import IconField

class SetupForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            IconField("username", icon_prepend="user"),
        )

    username = CharField(
        label="Username",
        required=True,
    )
```

Note that `IconField` also supports an `icon_append` keyword argument. This field only supports font-awesome icons.

UploadField
-----------

The UploadField looks like this:

![UploadField](https://i.imgur.com/hCv7g9K.gif)

To create these with CrispyForms, you'll need both a form object and a layout object from our package. Here's an example of how to use them.
```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from django_crispy_bulma.layout import UploadField
from django_crispy_bulma.forms import ImageField, FileField

class MyForm(forms.Form):
    my_image = ImageField(
        label="Upload an image of your dog",
        required=False
    )
    my_file = FileField(
        label="Upload your actual dog in .dog format",
        required=True    
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.layout = Layout(
            UploadField("my_image"),
            UploadField("my_file"),
        )
```

A little bit of javascript is needed in order to get the filename to display after a file upload is successful.

Written in vanilla JS, this might look something like this:

```javascript
window.onload = function() {
    // Apply this to all upload fields
    const upload_fields = document.querySelectorAll(".file");
    for (let i = 0; i < upload_fields.length; i++) {
        let input = upload_fields[i].querySelector(".file-input");
        let filename = upload_fields[i].querySelector(".file-name");

        input.onchange = function() {
            filename.textContent = input.files[0].name;
        }
    }
};
```

For your convenience, we provide a script that handles this in our companion package, [django-simple-bulma](https://github.com/python-discord/django-simple-bulma). We highly recommend you use these two packages together.  
