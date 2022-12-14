from django.template import Template
from django.template.loader import render_to_string

from crispy_forms.layout import (
    HTML,
    BaseInput,
    ButtonHolder,
    Div,
    Field,
    Fieldset,
    Hidden,
    Layout,
    LayoutObject,
    MultiField,
    MultiWidgetField,
    TemplateNameMixin,
)
from crispy_forms.utils import TEMPLATE_PACK, flatatt, render_field

__all__ = [
    # Defined in this file
    "Button",
    "Column",
    "IconField",
    "Reset",
    "Row",
    "Submit",
    "FormGroup",
    "UploadField",
    # Imported from CrispyForms itself
    "ButtonHolder",
    "Div",
    "Field",
    "Fieldset",
    "Hidden",
    "HTML",
    "Layout",
    "MultiField",
    "MultiWidgetField",
]


class UploadField(Field):
    def __init__(self, *args, **kwargs):
        if "css_class" in kwargs:
            kwargs["css_class"] += " file-input"
        else:
            kwargs["css_class"] = "file-input"

        super().__init__(*args, **kwargs)


class BulmaBaseInput(BaseInput):
    def __init__(self, *args, **kwargs):
        self.control_class = kwargs.pop("control_class", None)
        super().__init__(*args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        """
        Renders an `<input />` if container is used as a Layout object.
        Input button value can be a variable in context.

        """
        if self.control_class:
            context["control_class"] = self.control_class
        return super().render(
            form, form_style, context, template_pack=template_pack, **kwargs
        )


class Submit(BulmaBaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag.
    >>> submit = Submit("Search the Site", "search this site")

    The first argument is also slugified and turned into the id for the submit button.
    """

    field_classes = "button"
    input_type = "submit"


class Button(TemplateNameMixin):
    """
    Layout object for rendering an HTML button::
        Button("button content", css_class="extra")

    """

    template = "%s/layout/button.html"
    field_classes = "button"

    def __init__(self, content, **kwargs):
        self.content = content
        self.template = kwargs.pop("template", self.template)
        self.control_class = kwargs.pop("control_class", None)

        # We turn css_id and css_class into id and class
        if "css_id" in kwargs:
            kwargs["id"] = kwargs.pop("css_id")
        kwargs["class"] = self.field_classes
        if "css_class" in kwargs:
            kwargs["class"] += " %s" % kwargs.pop("css_class")

        self.flat_attrs = flatatt(kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        self.content = Template(str(self.content)).render(context)
        template = self.get_template_name(template_pack)

        extra_context = {"button": self}
        if self.control_class:
            extra_context["control_class"] = self.control_class

        context.update(extra_context)
        return render_to_string(template, context.flatten())


class Reset(BulmaBaseInput):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag.
    >>> reset = Reset("Reset This Form", "Revert Me!")

    The first argument is also slugified and turned into the id for the button.
    """

    field_classes = "button"
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
    """
    Layout object for rendering icons left and/or right of an input field.

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
    *fields: str
        Usually a single field, but can be any number of fields, to be rendered
        with the same attributes applied.
    icon_prepend: str, optional
        Icon class of supported by Bulma icon font libraries e.g. ``fas fa-home``.
        By default ``None``.
    icon_append: str, optional
        Icon class of supported by Bulma icon font libraries e.g. ``fas fa-home``.
        By default ``None``.
    css_class: str, optional
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
        attributes are added to the ``<div>``.

    Examples
    --------

    Example::

        IconField('field_name', icon_prepend="fa-solid fa-envelope")
    """

    template = "%s/layout/input_with_icon.html"

    def __init__(self, field, icon_prepend=None, icon_append=None, *args, **kwargs):
        self.field = field
        self.icon_prepend = icon_prepend
        self.icon_append = icon_append
        super().__init__(*args, **kwargs)

    def render(
        self,
        form,
        form_style,
        context,
        template_pack=TEMPLATE_PACK,
        extra_context=None,
        **kwargs
    ):
        extra_context = extra_context.copy() if extra_context is not None else {}
        extra_context.update(
            {
                "icon_prepend": self.icon_prepend,
                "icon_append": self.icon_append,
            }
        )
        template = self.get_template_name(template_pack)

        return render_field(
            self.field,
            form,
            form_style,
            context,
            template=template,
            template_pack=template_pack,
            extra_context=extra_context,
            attrs=self.attrs,
            **kwargs
        )


class FormGroup(LayoutObject):
    """
    Bulma layout object. It wraps fields in a <div class="field is-grouped">
    Attributes
    ----------
    template: str
        The default template which this Layout Object will be rendered with.
    Parameters
    ----------
    *fields : HTML or BaseInput
        The layout objects to render within the ``FormGroup``. It should
        only hold `HTML` and `BaseInput` inherited objects.
    css_id : str, optional
        A custom DOM id for the layout object which will be added to the
        ``<div>`` if provided. By default None.
    css_class : str, optional
        Additional CSS classes to be applied to the ``<div>``. By default
        None.
    template : str, optional
        Overrides the default template, if provided. By default None.
    **kwargs : dict, optional
        Additional attributes are passed to ``flatatt`` and converted into
        key="value", pairs. These attributes are added to the ``<div>``.
    Examples
    --------
    An example using ``FormGroup`` in your layout::
        FormGroup(
            Submit('Save', 'Save', css_class='is-primary'),
            Button('Delete', css_class='is-danger'),
            css_class="is-grouped-centered"
        )
    """

    template = "%s/layout/formgroup.html"

    def __init__(self, *fields, css_id=None, css_class=None, template=None, **kwargs):
        self.fields = list(fields)
        self.id = css_id
        self.css_class = css_class
        self.template = template or self.template
        self.flat_attrs = flatatt(kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        # TODO use extra_context
        # There seem to be a bug in crispy_forms, the `extra_context` kwarg is not being
        # passed on to `field.render` in `render_field` which is called by `get_rendered_fields`.
        # Right now `exclude_field_wrapper` is being passed on also to `formgroup.html`,
        # but it does not break anything.
        context["exclude_field_wrapper"] = True
        html = self.get_rendered_fields(
            form, form_style, context, template_pack, **kwargs
        )
        template = self.get_template_name(template_pack)
        context.update({"formgroup": self, "fields_output": html})
        return render_to_string(template, context.flatten())
