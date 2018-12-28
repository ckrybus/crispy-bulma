from crispy_forms.layout import (
    BaseInput, ButtonHolder, Div, Field,
    Fieldset, HTML, Hidden, Layout, MultiField,
    MultiWidgetField
)
from crispy_forms.utils import TEMPLATE_PACK, render_field

__all__ = [
    # Defined in this file
    "Button", "Column", "IconField", "Reset", "Row", "Submit", "UploadField",

    # Imported from CrispyForms itself
    "ButtonHolder", "Div", "Field", "Fieldset", "Hidden", "HTML", "Layout",
    "MultiField", "MultiWidgetField",
]


class UploadField(Field):
    def __init__(self, *args, **kwargs):
        if 'css_class' in kwargs:
            kwargs['css_class'] += " file-input"
        else:
            kwargs['css_class'] = "file-input"

        super().__init__(*args, **kwargs)


class Submit(BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag.
    >>> submit = Submit("Search the Site", "search this site")

    The first argument is also slugified and turned into the id for the submit button.
    """

    field_classes = "button is-primary"
    input_type = "submit"


class Button(BaseInput):
    """
    Used to create a Submit input descriptor for the {% crispy %} template tag.
    >>> button = Button("Button 1", "Press Me!")

    The first argument is also slugified and turned into the id for the button.
    """

    field_classes = "button"
    input_type = "button"


class Reset(BaseInput):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag.
    >>> reset = Reset("Reset This Form", "Revert Me!")

    The first argument is also slugified and turned into the id for the button.
    """

    field_classes = "button is-text"
    input_type = "reset"


class Row(Div):
    """
    Layout object. It wraps fields in a div whose default class is "columns".
    >>> Row("form_field_1", "form_field_2", "form_field_3")
    """

    css_class = "columns"


class Column(Div):
    """
    Layout object. It wraps fields in a div whose default class is "column".

    >>> Column("form_field_1", "form_field_2")
    """

    css_class = "column"


class IconField(Field):
    template = "%s/layout/input_with_icon.html"

    def __init__(self, field, icon_prepend=None, icon_append=None, *args, **kwargs):
        self.field = field
        self.icon_prepend = icon_prepend
        self.icon_append = icon_append
        super().__init__(*args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK,
               extra_context=None, **kwargs):
        extra_context = extra_context.copy() if extra_context is not None else {}
        extra_context.update({
            "icon_prepend": self.icon_prepend,
            "icon_append": self.icon_append,
        })
        template = self.get_template_name(template_pack)

        return render_field(
            self.field, form, form_style, context,
            template=template,
            template_pack=template_pack, extra_context=extra_context, **kwargs
        )
