============
crispy-bulma
============

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
        :target: https://github.com/ckrybus/crispy-bulma/blob/main/LICENSE
.. image:: https://img.shields.io/github/workflow/status/ckrybus/crispy-bulma/Test
        :target: https://github.com/ckrybus/crispy-bulma/actions
        :alt: GitHub Workflow Status
.. image:: https://img.shields.io/pypi/v/crispy_bulma.svg
        :target: https://pypi.python.org/pypi/crispy-bulma

**This project is under active development. You should not use this package yet, as it is poorly documented and is missing many important features. I'll remove this header when it's ready to use.**

Bulma_ template pack for django-crispy-forms_

.. _Bulma: https://bulma.io/
.. _django-crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms

Documentation: https://crispy-bulma.readthedocs.io.


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

* This project is based on an archived `crispy-forms-bulma <https://github.com/python-discord/django-crispy-bulma>`_ fork by Discord
* The original `crispy-forms-bulma <https://github.com/jhotujec/crispy-forms-bulma>`_ project is by Jure Hotujec

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


License
-------

MIT license
