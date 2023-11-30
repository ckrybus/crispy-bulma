=======
History
=======


Unreleased
----------

* Drop support for Django 3.2, 4.0 and 4.1


0.10.0 (2023-07-03)
-------------------

* Drop support for Python 3.7
* Add support for Python 3.12
* Add support for Django 4.2


0.9.0 (2023-03-05)
------------------

* Drop support for django-crispy-forms 1.12.0, 1.13.0 and 1.14.0
* Add support for django-crispy-forms 2.0
* Drop support for Django 2.2


0.8.3 (2023-01-31)
------------------

* Fix Select widget error state rendering (the red border was missing).


0.8.2 (2023-01-29)
------------------

* Add support for Django 4.1
* Add support for Python 3.11


0.8.1 (2023-01-22)
------------------

* Fix DateField, DateTimeField and TimeField widget rendering
* Fix DecimalField, FloatField, IntegerField and URLField widget rendering. Fix contributed by pythonbrad.
* Fix FileUploadInput widget rendering. Fix contributed by pythonbrad.
* Fix passing attributes to IconField. Fix contributed by davy39.


0.8.0 (2022-04-28)
------------------

* Feature: add ``FormGroup`` layout object
* Fix ``Submit`` and ``Reset`` input rendering
* BREAKING CHANGE: ``Button`` is now rendered as ``<button></button>``.
  For ``<input type="submit" />`` use ``Submit``.
* BREAKING CHANGE: Redesign IconField. Instead of ``IconField("envelope")`` call it with the
  full icon class e.g. ``IconField("fa fa-envelope")``.
* Drop support for Django 3.1
* Drop support for Python 3.6


0.7.0 (2022-04-17)
------------------

* Fix FormHelper.field_template attribute
* Feature: add InlineCheckboxes field
* Feature: add InlineRadios field
* Add support for django-crispy-forms 1.14.0
* Add support for Python 3.10


0.6.0 (2022-04-15)
------------------

* Add support for Django 4.0
* Fix SelectMultiple widget rendering


0.5.1 (2022-04-14)
------------------

* Readd templatetags removed by mistake.


0.5.0 (2022-04-13)
------------------

* Drop support for Django 3.0
* Upgrade crispy_forms dependency, now version >= 1.12.0 is required


0.4.0 (2022-04-13)
------------------

* Feature: add ``label_class`` helper attribute
* Feature: add support for horizontal forms
* BREAKING CHANGE: HTML in labels is now being escaped, this is consistent with django.
* BREAKING CHANGE: EmailField and EmailInput have been removed. Use django.forms.EmailField instead.
* Feature: add support for forms.MultipleChoiceField with CheckboxSelectMultiple as widget.


0.3.1 (2022-04-08)
------------------

* Fix input wrapper, replace p tag with a div
* Fix checkbox rendering, the input was rendered twice
* Initial version by ckrybus (tests, docs, packaging, no logic changes)


0.3.0 (2020-03-22) [#discord]_
------------------------------

* Add support for django 3.0


0.2.0 (2019-12-12) [#discord]_
------------------------------

* Update dependency pinning


0.1.2 (2019-04-02) [#discord]_
------------------------------

* Add EmailInput widget


0.1.1 (2019-01-15) [#discord]_
------------------------------

* Update docs


0.1.0 (2019-01-13) [#discord]_
------------------------------

* Initial version by discord.


1.1.3 (2017-11-06) [#jhotujec]_
-------------------------------

* Added input with icons


1.1.2 (2017-11-06) [#jhotujec]_
-------------------------------

* Added template for non-field errors
* Fix radio select, which now appears inline
* Fix form actions template (submit, reset)


1.1.1 (2017-11-06) [#jhotujec]_
-------------------------------

* Initial version by @jhotujec


.. rubric:: Footnotes

.. [#discord] At that time the project was called https://github.com/python-discord/django-crispy-bulma

.. [#jhotujec] At that time the project was called https://github.com/jhotujec/crispy-forms-bulma
