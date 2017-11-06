from crispy_forms.utils import TEMPLATE_PACK, render_field

from layout import Field


class InputWithIcon(Field):
    template = "%s/layout/input_with_icon.html"

    def __init__(self, field, icon_prepend=None, icon_append=None, *args, **kwargs):
        self.field = field
        self.icon_prepend = icon_prepend
        self.icon_append = icon_append

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK,
               extra_context=None, **kwargs):
        extra_context = extra_context.copy() if extra_context is not None else {}
        extra_context.update({
            'icon_prepend': self.icon_prepend,
            'icon_append': self.icon_append,
        })
        template = self.get_template_name(template_pack)

        return render_field(
            self.field, form, form_style, context,
            template=template,
            template_pack=template_pack, extra_context=extra_context, **kwargs
        )
