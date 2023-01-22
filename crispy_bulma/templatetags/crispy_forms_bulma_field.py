# This file is currently copied directly from django-crispy-forms==0.12.0
# There are only a few small changes specific to bulma.
# https://github.com/django-crispy-forms/django-crispy-forms/blob/1.12.0/crispy_forms/templatetags/crispy_forms_field.py

from django import forms, template
from django.conf import settings
from django.template import Variable

register = template.Library()


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_password(field):
    return isinstance(field.field.widget, forms.PasswordInput)


@register.filter
def is_radioselect(field):
    # the extra CheckboxSelectMultiple check is needed for django 4.0
    return isinstance(field.field.widget, forms.RadioSelect) and not isinstance(
        field.field.widget, forms.CheckboxSelectMultiple
    )


@register.filter
def is_select(field):
    # warning: this function is True for forms.SelectMultiple too
    return isinstance(field.field.widget, forms.Select)


@register.filter
def is_selectmultiple(field):
    return isinstance(field.field.widget, forms.SelectMultiple)


@register.filter
def is_checkboxselectmultiple(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_clearable_file(field):
    return isinstance(field.field.widget, forms.ClearableFileInput)


@register.filter
def is_multivalue(field):
    return isinstance(field.field.widget, forms.MultiWidget)


@register.filter
def classes(field):
    """
    Returns CSS classes of a field
    """
    return field.widget.attrs.get("class", None)


@register.filter
def css_class(field):
    """
    Returns widgets class name in lowercase
    """
    return field.field.widget.__class__.__name__.lower()


def pairwise(iterable):
    """s -> (s0,s1), (s2,s3), (s4, s5), ..."""
    a = iter(iterable)
    return zip(a, a)


class CrispyBulmaFieldNode(template.Node):
    def __init__(self, field, attrs):
        self.field = field
        self.attrs = attrs

    def render(self, context):
        # Nodes are not threadsafe so we must store and look up our instance
        # variables in the current rendering context first
        if self not in context.render_context:
            context.render_context[self] = (
                Variable(self.field),
                self.attrs,
            )

        field, attrs = context.render_context[self]
        field = field.resolve(context)

        # There are special django widgets that wrap actual widgets,
        # such as forms.widgets.MultiWidget, admin.widgets.RelatedFieldWidgetWrapper
        widgets = getattr(
            field.field.widget,
            "widgets",
            [getattr(field.field.widget, "widget", field.field.widget)],
        )

        if isinstance(attrs, dict):
            attrs = [attrs] * len(widgets)

        converters = {
            "dateinput": "dateinput input",
            "datetimeinput": "datetimeinput input",
            "textinput": "input",
            "fileinput": "fileinput",
            "clearablefileinput": "clearablefileinput",
            "passwordinput": "input",
            "emailinput": "input",
            "checkboxinput": "",
            "select": "",
            "selectmultiple": "",
            "numberinput": "numberinput input",
            "timeinput": "timeinput input",
            "urlinput": "urlinput input",
            # custom widget
            "fileuploadinput": "file-input",
        }
        converters.update(getattr(settings, "CRISPY_CLASS_CONVERTERS", {}))

        for widget, attr in zip(widgets, attrs):
            class_name = widget.__class__.__name__.lower()
            class_name = converters.get(class_name, class_name)
            css_class = widget.attrs.get("class", "")
            if css_class:
                if css_class.find(class_name) == -1:
                    css_class += " %s" % class_name
            else:
                css_class = class_name

            widget.attrs["class"] = css_class

            if "class" in widget.attrs and not widget.attrs["class"]:
                # remove the class="" attribute completely if empty
                del widget.attrs["class"]

            for attribute_name, attribute in attr.items():
                attribute_name = Variable(attribute_name).resolve(context)
                attributes = Variable(attribute).resolve(context)

                if attribute_name in widget.attrs:
                    # multiple attributes are in a single string, e.g.
                    # "form-control is-invalid"
                    for attr in attributes.split():
                        if attr not in widget.attrs[attribute_name].split():
                            widget.attrs[attribute_name] += " " + attr
                else:
                    widget.attrs[attribute_name] = attributes

        return str(field)


@register.tag(name="crispy_field")
def crispy_field(parser, token):
    """
    {% crispy_field field attrs %}
    """
    token = token.split_contents()
    field = token.pop(1)
    attrs = {}

    # We need to pop tag name, or pairwise would fail
    token.pop(0)
    for attribute_name, value in pairwise(token):
        attrs[attribute_name] = value

    return CrispyBulmaFieldNode(field, attrs)
