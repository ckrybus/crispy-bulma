import pytest

from django import forms
from django.template import Context, Template
from django.utils.translation import activate, deactivate
from django.utils.translation import gettext as _

from crispy_forms.bootstrap import InlineRadios  # # TODO switch to bulma specific
from crispy_forms.bootstrap import (
    Alert,
    AppendedText,
    FieldWithButtons,
    InlineCheckboxes,
    InlineField,
    PrependedAppendedText,
    PrependedText,
    StrictButton,
    Tab,
    TabHolder,
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout, MultiWidgetField
from crispy_forms.utils import render_crispy_form

from .forms import (
    CheckboxesSampleForm,
    CustomCheckboxSelectMultiple,
    CustomRadioSelect,
    GroupedChoiceForm,
    InputsForm,
    SampleForm,
    SampleFormCustomWidgets,
)
from .utils import parse_expected, parse_form


def test_email_field():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout("email")
    assert parse_form(form) == parse_expected("test_email_field.html")


def test_field_with_custom_template():
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        Field("email", template="custom_field_template.html")
    )

    html = render_crispy_form(test_form)
    assert "<h1>Special custom field</h1>" in html


def test_multiwidget_field():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form %}
    """
    )

    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        MultiWidgetField(
            "datetime_field",
            attrs=(
                {"rel": "test_dateinput"},
                {"rel": "test_timeinput", "style": "width: 30px;", "type": "hidden"},
            ),
        )
    )

    c = Context({"form": test_form})

    html = template.render(c)

    assert html.count('class="dateinput') == 1
    assert html.count('rel="test_dateinput"') == 1
    assert html.count('rel="test_timeinput"') == 2
    assert html.count('style="width: 30px;"') == 2
    assert html.count('type="hidden"') == 2


def test_field_type_hidden():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy test_form %}
    """
    )

    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        Field("email", type="hidden", data_test=12),
        Field("datetime_field"),
    )

    c = Context({"test_form": test_form})
    html = template.render(c)

    # Check form parameters
    assert html.count('data-test="12"') == 1
    assert html.count('name="email"') == 1
    assert html.count('class="dateinput') == 1
    assert html.count('class="timeinput') == 1


def test_field_wrapper_class(settings):
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(Field("email", wrapper_class="testing"))

    html = render_crispy_form(form)
    assert html.count('class="field testing"') == 1


def test_html_with_carriage_returns(settings):
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        HTML(
            """
            if (a==b){
                // some comment
                a+1;
                foo();
            }
        """
        )
    )
    html = render_crispy_form(test_form)
    assert html.count("\n") == 26


def test_i18n():
    activate("es")
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(HTML(_("Enter a valid value.")))
    html = render_crispy_form(form)
    assert "Introduzca un valor válido" in html

    deactivate()


def test_remove_labels():
    form = SampleForm()
    # remove boolean field as label is still printed in bulma
    del form.fields["is_company"]

    for fields in form:
        fields.label = False

    html = render_crispy_form(form)

    assert "<label" not in html


@pytest.mark.parametrize(
    "input,expected",
    [
        ("text_input", "text_input.html"),
        ("text_area", "text_area.html"),
        # ("checkboxes", "checkboxes.html"),
        # ("radio", "radio.html"),
        ("single_checkbox", "single_checkbox.html"),
    ],
)
def test_inputs(input, expected):
    form = InputsForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(input)
    assert parse_form(form) == parse_expected(expected)


@pytest.mark.skip(reason="InlineRadios")
def test_custom_django_widget():
    # Make sure an inherited RadioSelect gets rendered as it
    form = SampleFormCustomWidgets()
    assert isinstance(form.fields["inline_radios"].widget, CustomRadioSelect)
    form.helper = FormHelper()
    form.helper.layout = Layout("inline_radios")

    html = render_crispy_form(form)
    assert 'class="form-check-input"' in html

    # Make sure an inherited CheckboxSelectMultiple gets rendered as it
    assert isinstance(form.fields["checkboxes"].widget, CustomCheckboxSelectMultiple)
    form.helper.layout = Layout("checkboxes")
    html = render_crispy_form(form)
    assert 'class="form-check-input"' in html


@pytest.mark.skip(reason="prepended_appended_text")
def test_prepended_appended_text():
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        PrependedAppendedText(
            "email", "@<>&", "gmail.com", css_class="form-control-lg"
        ),
        AppendedText("password1", "#"),
        PrependedText("password2", "$"),
    )
    assert parse_form(test_form) == parse_expected("test_prepended_appended_text.html")


@pytest.mark.skip(reason="InlineRadios")
def test_inline_radios():
    test_form = CheckboxesSampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(InlineRadios("inline_radios"))
    html = render_crispy_form(test_form)
    assert html.count('form-check-inline"') == 2


@pytest.mark.skip(reason="bootstrap")
def test_alert():
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.form_tag = False
    test_form.helper.layout = Layout(
        Alert(content="Testing...", css_class="alert-primary"),
        Alert(content="Testing...", css_class="alert-primary", dismiss=False),
    )
    assert parse_form(test_form) == parse_expected("alert.html")


@pytest.mark.skip(reason="bootstrap")
def test_tab_and_tab_holder():
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout(
        TabHolder(
            Tab(
                "one",
                "first_name",
                css_id="custom-name",
                css_class="first-tab-class active",
            ),
            Tab("two", "password1", "password2"),
        )
    )
    html = render_crispy_form(test_form)

    assert (
        html.count(
            '<ul class="nav nav-tabs"> <li class="nav-item">'
            '<a class="nav-link active" href="#custom-name" data-bs-toggle="tab">'
            "One</a></li>"
        )
        == 1
    )
    assert html.count("tab-pane") == 2

    assert html.count('class="tab-pane first-tab-class active"') == 1

    assert html.count('<div id="custom-name"') == 1
    assert html.count('<div id="two"') == 1
    assert html.count('name="first_name"') == 1
    assert html.count('name="password1"') == 1
    assert html.count('name="password2"') == 1


@pytest.mark.skip(reason="bootstrap")
def test_tab_helper_reuse():
    # this is a proper form, according to the docs.
    # note that the helper is a class property here,
    # shared between all instances
    class SampleForm(forms.Form):
        val1 = forms.CharField(required=False)
        val2 = forms.CharField(required=True)
        helper = FormHelper()
        helper.layout = Layout(
            TabHolder(
                Tab("one", "val1"),
                Tab("two", "val2"),
            )
        )

    # first render of form => everything is fine
    test_form = SampleForm()
    html = render_crispy_form(test_form)

    # second render of form => first tab should be active,
    # but not duplicate class
    test_form = SampleForm()
    html = render_crispy_form(test_form)
    assert html.count('class="nav-item active active"') == 0

    # render a new form, now with errors
    test_form = SampleForm(data={"val1": "foo"})
    html = render_crispy_form(test_form)
    tab_class = "tab-pane"
    # if settings.CRISPY_TEMPLATE_PACK == 'bootstrap4':
    # tab_class = 'nav-link'
    # else:
    # tab_class = 'tab-pane'
    # tab 1 should not be active
    assert html.count('<div id="one" \n    class="{} active'.format(tab_class)) == 0
    # tab 2 should be active
    assert html.count('<div id="two" \n    class="{} active'.format(tab_class)) == 1


@pytest.mark.skip(reason="InlineRadios")
def test_radio_attrs():
    form = CheckboxesSampleForm()
    form.fields["inline_radios"].widget.attrs = {"class": "first"}
    form.fields["checkboxes"].widget.attrs = {"class": "second"}
    html = render_crispy_form(form)
    assert 'class="first"' in html
    assert 'class="second"' in html


@pytest.mark.skip(reason="button")
def test_field_with_buttons():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        FieldWithButtons(
            Field("password1", css_class="span4"),
            StrictButton("Go!", css_id="go-button"),
            StrictButton("No!", css_class="extra"),
            StrictButton("Test", type="submit", name="whatever", value="something"),
            css_class="extra",
            autocomplete="off",
        )
    )
    html = render_crispy_form(form)

    form_group_class = "mb-3"

    assert html.count('class="%s extra"' % form_group_class) == 1
    assert html.count('autocomplete="off"') == 1
    assert html.count('class="span4') == 1
    assert html.count('id="go-button"') == 1
    assert html.count("Go!") == 1
    assert html.count("No!") == 1
    assert html.count('class="btn"') == 2
    assert html.count('class="btn extra"') == 1
    assert html.count('type="submit"') == 1
    assert html.count('name="whatever"') == 1
    assert html.count('value="something"') == 1


@pytest.mark.skip(reason="prepended_appended_text")
def test_hidden_fields():
    form = SampleForm()
    # All fields hidden
    for field in form.fields:
        form.fields[field].widget = forms.HiddenInput()

    form.helper = FormHelper()
    form.helper.layout = Layout(
        AppendedText("password1", "foo"),
        PrependedText("password2", "bar"),
        PrependedAppendedText("email", "bar"),
        InlineCheckboxes("first_name"),
        InlineRadios("last_name"),
    )
    html = render_crispy_form(form)
    assert html.count("<input") == 5
    assert html.count('type="hidden"') == 5
    assert html.count("<label") == 0


@pytest.mark.skip(reason="InlineCheckboxes")
def test_multiplecheckboxes():
    test_form = CheckboxesSampleForm()
    html = render_crispy_form(test_form)
    assert html.count("checked") == 6

    test_form.helper = FormHelper(test_form)
    test_form.helper[1].wrap(InlineCheckboxes, inline=True)
    html = render_crispy_form(test_form)
    # TODO Fix this test
    # assert html.count('form-check-input"') == 3


@pytest.mark.skip(reason="InlineCheckboxes")
def test_multiple_checkboxes_unique_ids():
    test_form = CheckboxesSampleForm()
    html = render_crispy_form(test_form)

    expected_ids = [
        "checkboxes_0",
        "checkboxes_1",
        "checkboxes_2",
        "alphacheckboxes_0",
        "alphacheckboxes_1",
        "alphacheckboxes_2",
        "numeric_multiple_checkboxes_0",
        "numeric_multiple_checkboxes_1",
        "numeric_multiple_checkboxes_2",
    ]
    for id_suffix in expected_ids:
        expected_str = f'id="id_{id_suffix}"'
        assert html.count(expected_str) == 1


@pytest.mark.skip(reason="bootstrap")
def test_inline_field():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        InlineField("first_name", wrapper_class="col-4"),
        InlineField("is_company", wrapper_class="col-4"),
    )
    form.helper.form_class = "row row-cols-lg-auto align-items-center"
    assert parse_form(form) == parse_expected("test_inline_field.html")


@pytest.mark.skip(reason="bootstrap")
def test_grouped_checkboxes_radios():
    form = GroupedChoiceForm()
    form.helper = FormHelper()
    form.helper.layout = Layout("checkbox_select_multiple")
    assert parse_form(form) == parse_expected("test_grouped_checkboxes.html")
    form.helper.layout = Layout("radio")
    assert parse_form(form) == parse_expected("test_grouped_radios.html")

    form = GroupedChoiceForm({})
    form.helper = FormHelper()
    form.helper.layout = Layout("checkbox_select_multiple")
    assert parse_form(form) == parse_expected("test_grouped_checkboxes_failing.html")
    form.helper.layout = Layout("radio")
    assert parse_form(form) == parse_expected("test_grouped_radios_failing.html")
