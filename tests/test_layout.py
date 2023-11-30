import pytest

import django
from django import forms
from django.forms.models import formset_factory, modelformset_factory
from django.middleware.csrf import _get_new_csrf_string
from django.template import Context, Template
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from crispy_bulma.layout import Button, Column, Field, FormGroup, Row, Submit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout
from crispy_forms.utils import render_crispy_form

from .forms import (
    CrispyEmptyChoiceTestModel,
    CrispyTestModel,
    FileForm,
    FileFormRequired,
    FormGroupForm,
    HelpTextForm,
    LabelForm,
    SampleForm,
    SampleForm2,
    SampleForm3,
    SampleForm4,
    SampleForm6,
)
from .utils import contains_partial, parse_expected, parse_form


def test_invalid_unicode_characters(settings):
    # Adds a BooleanField that uses non valid unicode characters "ñ"
    form_helper = FormHelper()
    form_helper.add_layout(Layout("españa"))

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )
    c = Context({"form": SampleForm(), "form_helper": form_helper})
    settings.CRISPY_FAIL_SILENTLY = False
    with pytest.raises(Exception):
        template.render(c)


def test_unicode_form_field():
    class UnicodeForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["contraseña"] = forms.CharField()

        helper = FormHelper()
        helper.layout = Layout("contraseña")

    html = render_crispy_form(UnicodeForm())
    assert 'id="id_contraseña"' in html


def test_meta_extra_fields_with_missing_fields():
    class FormWithMeta(SampleForm):
        class Meta:
            fields = ("email", "first_name", "last_name")

    form = FormWithMeta()
    # We remove email field on the go
    del form.fields["email"]

    form_helper = FormHelper()
    form_helper.layout = Layout("first_name")

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )
    c = Context({"form": form, "form_helper": form_helper})
    html = template.render(c)
    assert "email" not in html


def test_layout_unresolved_field(settings):
    form_helper = FormHelper()
    form_helper.add_layout(Layout("typo"))

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )
    c = Context({"form": SampleForm(), "form_helper": form_helper})
    settings.CRISPY_FAIL_SILENTLY = False
    with pytest.raises(Exception):
        template.render(c)


def test_double_rendered_field(settings):
    form_helper = FormHelper()
    form_helper.add_layout(Layout("is_company", "is_company"))

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )
    c = Context({"form": SampleForm(), "form_helper": form_helper})
    settings.CRISPY_FAIL_SILENTLY = False
    with pytest.raises(Exception):
        template.render(c)


def test_context_pollution():
    class ExampleForm(forms.Form):
        comment = forms.CharField()

    form = ExampleForm()
    form2 = SampleForm()

    template = Template(
        """
        {% load crispy_forms_tags %}
        {{ form.as_ul }}
        {% crispy form2 %}
        {{ form.as_ul }}
    """
    )
    c = Context({"form": form, "form2": form2})
    html = template.render(c)

    assert html.count('name="comment"') == 2
    assert html.count('name="is_company"') == 1


@pytest.mark.skip(reason="fieldset")
def test_layout_fieldset_row_html_with_unicode_fieldnames():
    form_helper = FormHelper()
    form_helper.add_layout(
        Layout(
            Fieldset(
                "Company Data",
                "is_company",
                css_id="fieldset_company_data",
                css_class="fieldsets",
                title="fieldset_title",
                test_fieldset="123",
            ),
            Fieldset(
                "User Data",
                "email",
                Row(
                    "password1",
                    "password2",
                    css_id="row_passwords",
                    css_class="rows",
                ),
                HTML('<a href="#" id="testLink">test link</a>'),
                HTML(
                    """
                    {% if flag %}{{ message }}{% endif %}
                """
                ),
                "first_name",
                "last_name",
            ),
        )
    )

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )
    c = Context(
        {
            "form": SampleForm(),
            "form_helper": form_helper,
            "flag": True,
            "message": "Hello!",
        }
    )
    html = template.render(c)

    assert 'id="fieldset_company_data"' in html
    assert 'class="fieldsets' in html
    assert 'title="fieldset_title"' in html
    assert 'test-fieldset="123"' in html
    assert 'id="row_passwords"' in html
    assert html.count("<label") == 6

    assert 'class="row rows"' in html
    assert 'class="form-label' in html

    assert "Hello!" in html
    assert "testLink" in html


@pytest.mark.skip(reason="fieldset")
def test_change_layout_dynamically_delete_field():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )

    form = SampleForm()
    form_helper = FormHelper()
    form_helper.add_layout(
        Layout(
            Fieldset(
                "Company Data",
                "is_company",
                "email",
                "password1",
                "password2",
                css_id="multifield_info",
            ),
            Column(
                "first_name",
                "last_name",
                css_id="column_name",
            ),
        )
    )

    # We remove email field on the go
    # Layout needs to be adapted for the new form fields
    del form.fields["email"]
    del form_helper.layout.fields[0].fields[1]

    c = Context({"form": form, "form_helper": form_helper})
    html = template.render(c)
    assert "email" not in html


@pytest.mark.skip(reason="fieldset")
def test_column_has_css_classes():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )

    form = SampleForm()
    form_helper = FormHelper()
    form_helper.add_layout(
        Layout(
            Fieldset(
                "Company Data",
                "is_company",
                "email",
                "password1",
                "password2",
                css_id="multifield_info",
            ),
            Column("first_name", "last_name"),
        )
    )

    c = Context({"form": form, "form_helper": form_helper})
    html = template.render(c)

    assert html.count("formColumn") == 0
    assert html.count("col-md") == 1


@pytest.mark.skip(reason="formset")
def test_formset_layout():
    SampleFormSet = formset_factory(SampleForm, extra=3)
    formset = SampleFormSet()
    helper = FormHelper()
    helper.form_id = "thisFormsetRocks"
    helper.form_class = "formsets-that-rock"
    helper.form_method = "POST"
    helper.form_action = "simpleAction"
    helper.layout = Layout(
        Fieldset(
            "Item {{ forloop.counter }}",
            "is_company",
            "email",
        ),
        HTML("{% if forloop.first %}Note for first form only{% endif %}"),
        Row("password1", "password2"),
        Fieldset("", "first_name", "last_name"),
    )

    html = render_crispy_form(
        form=formset, helper=helper, context={"csrf_token": _get_new_csrf_string()}
    )

    # Check formset fields
    assert contains_partial(
        html,
        '<input id="id_form-TOTAL_FORMS" name="form-TOTAL_FORMS" type="hidden"'
        ' value="3"/>',
    )
    assert contains_partial(
        html,
        '<input id="id_form-INITIAL_FORMS" name="form-INITIAL_FORMS" type="hidden"'
        ' value="0"/>',
    )
    assert contains_partial(
        html,
        '<input id="id_form-MAX_NUM_FORMS" name="form-MAX_NUM_FORMS" type="hidden"'
        ' value="1000"/>',
    )
    assert contains_partial(
        html,
        '<input id="id_form-MIN_NUM_FORMS" name="form-MIN_NUM_FORMS" type="hidden"'
        ' value="0"/>',
    )
    assert html.count("hidden") == 5

    # Check form structure
    assert html.count("<form") == 1
    assert html.count("csrfmiddlewaretoken") == 1
    assert "formsets-that-rock" in html
    assert 'method="post"' in html
    assert 'id="thisFormsetRocks"' in html
    assert 'action="%s"' % reverse("simpleAction") in html

    # Check form layout
    assert "Item 1" in html
    assert "Item 2" in html
    assert "Item 3" in html
    assert html.count("Note for first form only") == 1
    assert html.count("row") == 3

    assert html.count("mb-3") == 21


@pytest.mark.skip(reason="formset")
def test_modelformset_layout():
    CrispyModelFormSet = modelformset_factory(
        CrispyTestModel, form=SampleForm4, extra=3
    )
    formset = CrispyModelFormSet(queryset=CrispyTestModel.objects.none())
    helper = FormHelper()
    helper.layout = Layout("email")

    html = render_crispy_form(form=formset, helper=helper)

    assert html.count("id_form-0-id") == 1
    assert html.count("id_form-1-id") == 1
    assert html.count("id_form-2-id") == 1

    assert contains_partial(
        html,
        '<input id="id_form-TOTAL_FORMS" name="form-TOTAL_FORMS" type="hidden"'
        ' value="3"/>',
    )
    assert contains_partial(
        html,
        '<input id="id_form-INITIAL_FORMS" name="form-INITIAL_FORMS" type="hidden"'
        ' value="0"/>',
    )
    assert contains_partial(
        html,
        '<input id="id_form-MAX_NUM_FORMS" name="form-MAX_NUM_FORMS" type="hidden"'
        ' value="1000"/>',
    )

    assert html.count('name="form-0-email"') == 1
    assert html.count('name="form-1-email"') == 1
    assert html.count('name="form-2-email"') == 1
    assert html.count('name="form-3-email"') == 0
    assert html.count("password") == 0


@pytest.mark.skip(reason="fieldset")
def test_i18n():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form.helper %}
    """
    )
    form = SampleForm()
    form_helper = FormHelper()
    form_helper.layout = Layout(
        HTML(_("i18n text")),
        Fieldset(
            _("i18n legend"),
            "first_name",
            "last_name",
        ),
    )
    form.helper = form_helper

    html = template.render(Context({"form": form}))
    assert html.count("i18n legend") == 1


def test_default_layout():
    test_form = SampleForm2()
    assert test_form.helper.layout.fields == [
        "is_company",
        "email",
        "password1",
        "password2",
        "first_name",
        "last_name",
        "datetime_field",
    ]


def test_default_layout_two():
    test_form = SampleForm3()
    assert test_form.helper.layout.fields == ["email"]


def test_modelform_layout_without_meta():
    test_form = SampleForm4()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout("email")
    html = render_crispy_form(test_form)

    assert "email" in html
    assert "password" not in html


def test_specialspaceless_not_screwing_intended_spaces():
    # see issue #250
    test_form = SampleForm()
    test_form.fields["email"].widget = forms.Textarea()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        "email", HTML("<span>first span</span> <span>second span</span>")
    )
    html = render_crispy_form(test_form)
    assert "<span>first span</span> <span>second span</span>" in html


def test_choice_with_none_is_selected():
    # see issue #701
    model_instance = CrispyEmptyChoiceTestModel()
    model_instance.fruit = None
    test_form = SampleForm6(instance=model_instance)
    html = render_crispy_form(test_form)
    assert "checked" in html


def test_update_attributes_class():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout("email", Field("password1"), "password2")
    form.helper["password1"].update_attributes(css_class="hello")
    html = render_crispy_form(form)
    assert html.count(' class="hello input') == 1
    form.helper = FormHelper()
    form.helper.layout = Layout(
        "email",
        Field("password1", css_class="hello"),
        "password2",
    )
    form.helper["password1"].update_attributes(css_class="hello2")
    html = render_crispy_form(form)
    assert html.count(' class="hello hello2 input') == 1


@pytest.mark.skip(reason="bulma")
def test_file_field():
    form = FileForm()
    form.helper = FormHelper()
    form.helper.layout = Layout("clearable_file")

    assert parse_form(form) == parse_expected("test_clearable_file_field.html")

    form.helper.layout = Layout("file_field")

    assert parse_form(form) == parse_expected("test_file_field.html")

    form = FileFormRequired({})
    form.helper = FormHelper()
    form.helper.layout = Layout("clearable_file")

    assert parse_form(form) == parse_expected("test_clearable_file_field_failing.html")

    form.helper.layout = Layout("file_field")

    assert parse_form(form) == parse_expected("test_file_field_failing.html")


def test_row():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Row(
            Column("first_name", css_class="is-full"),
        ),
        Row(
            Column("first_name"),
            Column("last_name"),
        ),
    )
    assert parse_form(form) == parse_expected("row.html")


def test_html_label_escape():
    form = LabelForm()
    form.helper = FormHelper()
    form.helper.layout = Layout("text_input")
    html = render_crispy_form(form)
    assert "&lt;b&gt;escape&lt;/b&gt;" in html


@pytest.mark.skip(reason="formset")
def test_tabular_formset_layout():
    SampleFormSet = formset_factory(SampleForm, extra=3)
    formset = SampleFormSet()
    formset.helper = FormHelper()
    formset.helper.template = "bootstrap5/table_inline_formset.html"
    assert parse_form(formset) == parse_expected("test_tabular_formset_layout.html")

    SampleFormSet = formset_factory(SampleForm, extra=3)
    data = {
        "form-TOTAL_FORMS": "1",
        "form-INITIAL_FORMS": "0",
    }
    formset = SampleFormSet(data)
    formset.helper = FormHelper()
    formset.helper.template = "bootstrap5/table_inline_formset.html"
    assert parse_form(formset) == parse_expected(
        "test_tabular_formset_layout_failing.html"
    )


def test_flat_attrs_safe():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Row(
            aria_labelledby="test<>%",
        )
    )
    form.helper.form_tag = False
    assert parse_form(form) == parse_expected("flat_attrs.html")


def test_help_text_is_not_escaped():
    # in django this value is also not HTML-escaped in automatically-generated forms
    form = HelpTextForm()
    form.helper = FormHelper()

    if django.VERSION < (5, 0):
        result = "help_text_escape__lt50.html"
    else:
        result = "help_text_escape.html"
    assert parse_form(form) == parse_expected(result)


def test_form_group_form():
    form = FormGroupForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Field("text_input"),
        FormGroup(
            Field("fruit"),
            Submit("accept", "Accept", css_class="is-primary"),
            Button("Reject", css_class="is-danger"),
        ),
    )

    if django.VERSION < (5, 0):
        result = "test_form_group__lt50.html"
    else:
        result = "test_form_group.html"
    assert parse_form(form) == parse_expected(result)

    form.helper.form_horizontal = True
    if django.VERSION < (5, 0):
        result = "test_form_group_horizontal__lt50.html"
    else:
        result = "test_form_group_horizontal.html"
    assert parse_form(form) == parse_expected(result)
