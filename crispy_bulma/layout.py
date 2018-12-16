from crispy_forms.layout import (
    BaseInput, ButtonHolder, Div, Field,
    Fieldset, HTML, Hidden, Layout, MultiField,
    MultiWidgetField
)

__all__ = [
    # Defined in this file
    "Button", "Column", "Reset", "Row", "Submit",

    # Imported from CrispyForms itself
    "Div", "Field", "HTML", "Layout", "ButtonHolder",
    "Hidden", "Fieldset", "MultiField", "MultiWidgetField"
]


class Submit(BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag.
    >>> submit = Submit('Search the Site', 'search this site')

    The first argument is also slugified and turned into the id for the submit button.
    """

    field_classes = 'button is-primary'
    input_type = 'submit'


class Button(BaseInput):
    """
    Used to create a Submit input descriptor for the {% crispy %} template tag.
    >>> button = Button('Button 1', 'Press Me!')

    The first argument is also slugified and turned into the id for the button.
    """

    field_classes = 'button'
    input_type = 'button'


class Reset(BaseInput):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag.
    >>> reset = Reset('Reset This Form', 'Revert Me!')

    The first argument is also slugified and turned into the id for the button.
    """

    field_classes = 'button is-text'
    input_type = 'reset'


class Row(Div):
    """
    Layout object. It wraps fields in a div whose default class is "columns".
    >>> Row('form_field_1', 'form_field_2', 'form_field_3')
    """

    css_class = 'columns'


class Column(Div):
    """
    Layout object. It wraps fields in a div whose default class is "column".

    >>> Column('form_field_1', 'form_field_2')
    """

    css_class = 'column'
