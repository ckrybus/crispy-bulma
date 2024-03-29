.. `widgets`:

=======
Widgets
=======

Bulma Widget objects
~~~~~~~~~~~~~~~~~~~~

The widget objects below can be used for a better styled form.

.. _here: https://django-crispy-forms.readthedocs.io/en/latest/layouts.html#universal-layout-objects


These ones live under module ``crispy_bulma.widgets``.


- **FileUploadInput**: Add a style to both ClearableFileInput and FileInput widgets

In your forms.py ::

    from django import forms
    from crispy_bulma.widgets import FileUploadInput

    class ArticleForm(forms.Form):
        name = forms.CharField()
        url = forms.URLField()
        image = forms.ImageField(widget=FileUploadInput)
        

This javascript code can be used for dynamic modification of the filename on file input change

.. code-block:: javascript

    document.addEventListener('DOMContentLoaded', () => {
      // Get all "file-input" elements
      const fileInputs = Array.prototype.slice.call(document.querySelectorAll('.file-input'), 0);

      // Add a onchange event on each of them
      fileInputs.forEach(el => {
        el.addEventListener('change', () => {
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
          // Update the filename
          $target.textContent = el.value;
        });
      });
    });

.. image:: images/file_input.png
   :align: center

.. image:: images/clearable_file_input.png
   :align: center
