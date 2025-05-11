from crispy_forms.layout import Field


class InlineRadios(Field):
    """
    Layout object for rendering radiobuttons inline.

    Attributes
    ----------
    template : str
        The default template which this Layout Object will be rendered
        with.
    attrs : dict
        Attributes to be applied to the field. These are converted into html
        attributes. e.g. ``data_id: 'test'`` in the attrs dict will become
        ``data-id='test'`` on the field's ``<input>``.

    Parameters
    ----------
    *fields : str
        Usually a single field, but can be any number of fields, to be rendered
        with the same attributes applied.
    css_class : str, optional
        CSS classes to be applied to the field. These are added to any classes
        included in the ``attrs`` dict. By default ``None``.
    wrapper_class: str, optional
        CSS classes to be used when rendering the Field. This class is usually
        applied to the ``<div>`` which wraps the Field's ``<label>`` and
        ``<input>`` tags. By default ``None``.
    template : str, optional
        Overrides the default template, if provided. By default ``None``.
    **kwargs : dict, optional
        Additional attributes are converted into key="value", pairs. These
        attributes are added to the field's ``<input>``.

    Examples
    --------

    Example::

        InlineRadios('field_name')
    """

    template = "%s/layout/radioselect_inline.html"


class InlineCheckboxes(Field):
    """
    Layout object for rendering checkboxes inline.

    Attributes
    ----------
    template : str
        The default template which this Layout Object will be rendered
        with.
    attrs : dict
        Attributes to be applied to the field. These are converted into html
        attributes. e.g. ``data_id: 'test'`` in the attrs dict will become
        ``data-id='test'`` on the field's ``<input>``.

    Parameters
    ----------
    *fields : str
        Usually a single field, but can be any number of fields, to be rendered
        with the same attributes applied.
    css_class : str, optional
        CSS classes to be applied to the field. These are added to any classes
        included in the ``attrs`` dict. By default ``None``.
    wrapper_class: str, optional
        CSS classes to be used when rendering the Field. This class is usually
        applied to the ``<div>`` which wraps the Field's ``<label>`` and
        ``<input>`` tags. By default ``None``.
    template : str, optional
        Overrides the default template, if provided. By default ``None``.
    **kwargs : dict, optional
        Additional attributes are converted into key="value", pairs. These
        attributes are added to the field's ``<input>``.

    Examples
    --------

    Example::

        InlineCheckboxes('field_name')
    """

    template = "%s/layout/checkboxselectmultiple_inline.html"
