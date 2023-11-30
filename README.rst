============
crispy-bulma
============

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://github.com/ckrybus/crispy-bulma/blob/main/LICENSE
.. image:: https://img.shields.io/github/actions/workflow/status/ckrybus/crispy-bulma/test.yml?branch=main
        :target: https://github.com/ckrybus/crispy-bulma/actions
        :alt: GitHub Workflow Status
.. image:: https://img.shields.io/pypi/v/crispy-bulma
        :target: https://pypi.python.org/pypi/crispy-bulma
        :alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/crispy-bulma
        :target: https://pypi.python.org/pypi/crispy-bulma
        :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/djversions/crispy-bulma
        :target: https://pypi.python.org/pypi/crispy-bulma
        :alt: PyPI - Django Version

Bulma_ template pack for django-crispy-forms_

.. _Bulma: https://bulma.io/
.. _django-crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms

Documentation: https://crispy-bulma.readthedocs.io.


Requirements
------------

Officially supported versions:

* Django: 4.2, 5.0
* Python 3.8, 3.9, 3.10, 3.11, 3.12
* django-crispy-forms 2.0
* Bulma.css 0.9.4


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


Related projects
----------------

crispy-bulma's focus is on form handling. This project assumes that you have already integrated bulma into your project, either manually or using some other package. If crispy-bulma does not meet your needs maybe one of these projects is of interest to you:

* `django-bulma <https://github.com/timonweb/django-bulma>`__ - an alternative way to use bulma forms. Does not use crispy forms.

* `django-simple-bulma <https://github.com/lemonsaurus/django-simple-bulma>`__ - can be used together with this project. Provides bulma integration and ads support for bulma extensions.


License
-------

MIT license
