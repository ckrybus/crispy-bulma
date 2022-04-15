============
crispy-bulma
============

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://github.com/ckrybus/crispy-bulma/blob/main/LICENSE
.. image:: https://img.shields.io/github/workflow/status/ckrybus/crispy-bulma/Test
        :target: https://github.com/ckrybus/crispy-bulma/actions
        :alt: GitHub Workflow Status
.. image:: https://img.shields.io/pypi/v/crispy-bulma
        :target: https://pypi.python.org/pypi/crispy-bulma
        :alt: PyPI

Bulma_ template pack for django-crispy-forms_

.. _Bulma: https://bulma.io/
.. _django-crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms

Documentation: https://crispy-bulma.readthedocs.io.


Requirements
------------

Officially supported versions:

* Django: 2.2, 3.1, 3.2
* Python 3.6, 3.7, 3.8, 3.9
* django-crispy-forms 1.12, 1.13
* Bulma.css 0.9.3

Older versions might work, but are not officially supported.
For example django-crispy-forms >= 1.9.0, Bulma >= 0.7.5 and Django 3.0 are still likely to work.

If you depend on django 3.0 or django-crispy-forms < 1.12.0 use the 0.4.0 version.

This project aims to support the latest django and django-crispy-forms versions in the main branch.


Quickstart
----------

Install this plugin using `pip`::

    $ pip install crispy-bulma

You will need to update your project's settings file to add ``crispy_forms``
and ``crispy_bulma`` to your projects ``INSTALLED_APPS``. Also set
``bulma`` as and allowed template pack and as the default template pack
for your project::

    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_bulma",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = ("bulma",)

    CRISPY_TEMPLATE_PACK = "bulma"


Credits
-------

* This project is based on an archived `crispy-forms-bulma <https://github.com/python-discord/django-crispy-bulma>`__ fork by Discord
* The original `crispy-forms-bulma <https://github.com/jhotujec/crispy-forms-bulma>`__ project is by Jure Hotujec

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


License
-------

MIT license
