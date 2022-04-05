=====
Usage
=====

You will need to update your project's settings file to add crispy_forms and crispy_bulma to your projects INSTALLED_APPS. Also set bulma as and allowed template pack and as the default template pack for your project::

    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_bulma",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bulma"

    CRISPY_TEMPLATE_PACK = "bulma"
