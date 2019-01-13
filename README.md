# django-crispy-bulma

**This project is a work in progress. We'll remove this header when it's ready to use.**

Release 0.0.1 is simply a structural/branding change.

## About

This is a `Django` application to add `django-crispy-forms` layout objects for [Bulma](https://bulma.io/). 
It is a fork of [crispy-forms-bulma](https://github.com/jhotujec/crispy-forms-bulma) by Jure Hotujec, with the intention 
of adding support for Django 2.0+, as well as for components found in the bulma-extensions library.

## Installation

Clone it from github. Installation via `pip` coming soon!

Add package settings to your project settings file  
`from crispy_forms_bulma.settings import *` #TODO: Find a linter-friendly way to do this

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
