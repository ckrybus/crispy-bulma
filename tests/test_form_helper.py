import pytest

from django import forms
from django.forms.models import formset_factory
from django.middleware.csrf import _get_new_csrf_string
from django.template import Context, Template
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from crispy_bulma.layout import Button, Hidden, Reset, Submit
from crispy_forms.helper import FormHelper, FormHelpersException
from crispy_forms.layout import Field, Layout
from crispy_forms.templatetags.crispy_forms_tags import CrispyFormNode
from crispy_forms.utils import render_crispy_form

from .forms import SampleForm, SampleForm7, SampleForm8, SampleFormWithMedia
from .utils import parse_expected, parse_form


@pytest.mark.parametrize(
    "form_field,expected",
    [
        (
            Submit(
                "my-submit",
                "Submit",
                css_class="is-danger",
                control_class="is-expanded",
            ),
            "test_submit.html",
        ),
        (
            Reset(
                "my-reset", "Reset", css_class="is-danger", control_class="is-expanded"
            ),
            "test_reset.html",
        ),
        (Hidden("my-hidden", "Hidden"), "test_hidden.html"),
        (
            Button(
                "My Button",
                css_class="is-primary",
                control_class="is-expanded",
                css_id="button-id",
            ),
            "test_button.html",
        ),
    ],
)
def test_inputs(form_field, expected):
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(form_field)
    assert parse_form(form) == parse_expected(expected)


@pytest.mark.parametrize(
    "form_field,expected",
    [
        (
            Submit(
                "my-submit",
                "Submit",
                css_class="is-danger",
                control_class="is-expanded",
            ),
            "test_submit_horizontal.html",
        ),
        (
            Button(
                "My Button",
                css_class="is-primary",
                control_class="is-expanded",
                css_id="button-id",
            ),
            "test_button_horizontal.html",
        ),
    ],
)
def test_inputs_horizontal(form_field, expected):
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.form_horizontal = True
    form.helper.layout = Layout(form_field)
    assert parse_form(form) == parse_expected(expected)


def test_invalid_form_method():
    form_helper = FormHelper()
    with pytest.raises(FormHelpersException):
        form_helper.form_method = "superPost"


def test_form_with_helper_without_layout():
    form_helper = FormHelper()
    form_helper.form_id = "this-form-rocks"
    form_helper.form_class = "forms-that-rock"
    form_helper.form_method = "GET"
    form_helper.form_action = "simpleAction"
    form_helper.form_error_title = "ERRORS"

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy testForm form_helper %}
    """
    )

    # now we render it, with errors
    form = SampleForm({"password1": "wargame", "password2": "god"})
    form.is_valid()
    c = Context({"testForm": form, "form_helper": form_helper})
    html = template.render(c)

    # Lets make sure everything loads right
    assert html.count("<form") == 1
    assert "forms-that-rock" in html
    assert 'method="get"' in html
    assert 'id="this-form-rocks"' in html
    assert 'action="%s"' % reverse("simpleAction") in html

    assert "ERRORS" in html
    assert "<li>Passwords dont match</li>" in html

    # now lets remove the form tag and render it again. All the True items above
    # should now be false because the form tag is removed.
    form_helper.form_tag = False
    html = template.render(c)
    assert "<form" not in html
    assert "forms-that-rock" not in html
    assert 'method="get"' not in html
    assert 'id="this-form-rocks"' not in html


def test_form_show_errors_non_field_errors():
    form = SampleForm({"password1": "wargame", "password2": "god"})
    form.helper = FormHelper()
    form.helper.form_show_errors = True
    form.is_valid()

    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy testForm %}
    """
    )

    # First we render with errors
    c = Context({"testForm": form})
    html = template.render(c)

    # Ensure those errors were rendered
    assert "<li>Passwords dont match</li>" in html
    assert str(_("This field is required.")) in html

    # Now we render without errors
    form.helper.form_show_errors = False
    c = Context({"testForm": form})
    html = template.render(c)

    # Ensure errors were not rendered
    assert "<li>Passwords dont match</li>" not in html
    assert str(_("This field is required.")) not in html


def test_media_is_included_by_default_with_bulma():
    form = SampleFormWithMedia()
    form.helper = FormHelper()
    form.helper.template_pack = "bulma"
    html = render_crispy_form(form)
    assert "test.css" in html
    assert "test.js" in html


def test_media_removed_when_include_media_is_false_with_bulma():
    form = SampleFormWithMedia()
    form.helper = FormHelper()
    form.helper.template_pack = "bulma"
    form.helper.include_media = False
    html = render_crispy_form(form)
    assert "test.css" not in html
    assert "test.js" not in html


def test_attrs():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.attrs = {"id": "TestIdForm", "autocomplete": "off"}
    html = render_crispy_form(form)

    assert 'autocomplete="off"' in html
    assert 'id="TestIdForm"' in html


def test_template_context():
    helper = FormHelper()
    helper.attrs = {
        "id": "test-form",
        "class": "test-forms",
        "action": "submit/test/form",
        "autocomplete": "off",
    }
    node = CrispyFormNode("form", "helper")
    context = node.get_response_dict(helper, {}, False)

    assert context["form_id"] == "test-form"
    assert context["form_attrs"]["id"] == "test-form"
    assert "test-forms" in context["form_class"]
    assert "test-forms" in context["form_attrs"]["class"]
    assert context["form_action"] == "submit/test/form"
    assert context["form_attrs"]["action"] == "submit/test/form"
    assert context["form_attrs"]["autocomplete"] == "off"


def test_template_context_using_form_attrs():
    helper = FormHelper()
    helper.form_id = "test-form"
    helper.form_class = "test-forms"
    helper.form_action = "submit/test/form"
    node = CrispyFormNode("form", "helper")
    context = node.get_response_dict(helper, {}, False)

    assert context["form_id"] == "test-form"
    assert context["form_attrs"]["id"] == "test-form"
    assert "test-forms" in context["form_class"]
    assert "test-forms" in context["form_attrs"]["class"]
    assert context["form_action"] == "submit/test/form"
    assert context["form_attrs"]["action"] == "submit/test/form"


def test_template_helper_access():
    helper = FormHelper()
    helper.form_id = "test-form"

    assert helper["form_id"] == "test-form"


def test_without_helper():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form %}
    """
    )
    c = Context({"form": SampleForm()})
    html = template.render(c)

    # Lets make sure everything loads right
    assert "<form" in html
    assert 'method="post"' in html
    assert "action" not in html


def test_invalid_helper(settings):
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )
    c = Context({"form": SampleForm(), "form_helper": "invalid"})

    settings.CRISPY_FAIL_SILENTLY = settings.TEMPLATE_DEBUG = False
    with pytest.raises(TypeError):
        template.render(c)


@pytest.mark.skip(reason="formset")
def test_formset_with_helper_without_layout():
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy testFormSet formset_helper %}
    """
    )

    form_helper = FormHelper()
    form_helper.form_id = "thisFormsetRocks"
    form_helper.form_class = "formsets-that-rock"
    form_helper.form_method = "POST"
    form_helper.form_action = "simpleAction"

    SampleFormSet = formset_factory(SampleForm, extra=3)
    testFormSet = SampleFormSet()

    c = Context(
        {
            "testFormSet": testFormSet,
            "formset_helper": form_helper,
            "csrf_token": _get_new_csrf_string(),
        }
    )
    html = template.render(c)

    assert html.count("<form") == 1
    assert html.count("csrfmiddlewaretoken") == 1

    # Check formset management form
    assert "form-TOTAL_FORMS" in html
    assert "form-INITIAL_FORMS" in html
    assert "form-MAX_NUM_FORMS" in html

    assert "formsets-that-rock" in html
    assert 'method="post"' in html
    assert 'id="thisFormsetRocks"' in html
    assert 'action="%s"' % reverse("simpleAction") in html


def test_CSRF_token_POST_form():
    form_helper = FormHelper()
    template = Template(
        """
        {% load crispy_forms_tags %}
        {% crispy form form_helper %}
    """
    )

    # The middleware only initializes the CSRF token when processing a real request
    # So using RequestContext or csrf(request) here does not work.
    # Instead I set the key `csrf_token` to a CSRF token manually, which `csrf_token`
    # tag uses
    c = Context(
        {
            "form": SampleForm(),
            "form_helper": form_helper,
            "csrf_token": _get_new_csrf_string(),
        }
    )
    html = template.render(c)

    assert "csrfmiddlewaretoken" in html


def test_CSRF_token_GET_form():
    form_helper = FormHelper()
    form_helper.form_method = "GET"
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
            "csrf_token": _get_new_csrf_string(),
        }
    )
    html = template.render(c)

    assert "csrfmiddlewaretoken" not in html


def test_disable_csrf():
    form = SampleForm()
    helper = FormHelper()
    helper.disable_csrf = True
    html = render_crispy_form(form, helper, {"csrf_token": _get_new_csrf_string()})
    assert "csrf" not in html


def test_render_unmentioned_fields():
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout("email")
    test_form.helper.render_unmentioned_fields = True

    html = render_crispy_form(test_form)
    assert html.count("<input") == 8


def test_render_unmentioned_fields_order():
    test_form = SampleForm7()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout("email")
    test_form.helper.render_unmentioned_fields = True

    html = render_crispy_form(test_form)
    assert html.count("<input") == 4
    assert (
        # From layout
        html.index('id="div_id_email"')
        # From form.Meta.fields
        < html.index('id="div_id_password"')
        < html.index('id="div_id_password2"')
        # From fields
        < html.index('id="div_id_is_company"')
    )

    test_form = SampleForm8()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout("email")
    test_form.helper.render_unmentioned_fields = True

    html = render_crispy_form(test_form)
    assert html.count("<input") == 4
    assert (
        # From layout
        html.index('id="div_id_email"')
        # From form.Meta.fields
        < html.index('id="div_id_password2"')
        < html.index('id="div_id_password"')
        # From fields
        < html.index('id="div_id_is_company"')
    )


def test_render_hidden_fields():
    from .utils import contains_partial

    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout("email")
    test_form.helper.render_hidden_fields = True

    html = render_crispy_form(test_form)
    assert html.count("<input") == 1

    # Now hide a couple of fields
    for field in ("password1", "password2"):
        test_form.fields[field].widget = forms.HiddenInput()

    html = render_crispy_form(test_form)
    assert html.count("<input") == 3
    assert html.count("hidden") == 2

    assert contains_partial(html, '<input name="password1" type="hidden"/>')
    assert contains_partial(html, '<input name="password2" type="hidden"/>')


def test_render_required_fields():
    test_form = SampleForm()
    test_form.helper = FormHelper()
    test_form.helper.layout = Layout("email")
    test_form.helper.render_required_fields = True

    html = render_crispy_form(test_form)
    assert html.count("<input") == 7


def test_helper_custom_template():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.template = "custom_form_template.html"

    html = render_crispy_form(form)
    assert "<h1>Special custom form</h1>" in html


def test_helper_custom_field_template():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout("password1", "password2")
    form.helper.field_template = "custom_field_template.html"

    html = render_crispy_form(form)
    assert html.count("<h1>Special custom field</h1>") == 2


def test_helper_custom_field_template_no_layout():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.field_template = "custom_field_template.html"

    html = render_crispy_form(form)
    for field in form.fields:
        assert html.count('id="div_id_%s"' % field) == 1
    assert html.count("<h1>Special custom field</h1>") == len(form.fields)


def test_helper_std_field_template_no_layout():
    form = SampleForm()
    form.helper = FormHelper()

    html = render_crispy_form(form)
    for field in form.fields:
        assert html.count('id="div_id_%s"' % field) == 1


def test_form_show_errors():
    form = SampleForm(
        {
            "email": "invalidemail",
            "first_name": "first_name_too_long",
            "last_name": "last_name_too_long",
            "password1": "yes",
            "password2": "yes",
        }
    )
    form.helper = FormHelper()
    form.helper.layout = Layout(
        Field("email"),
        Field("first_name"),
        Field("last_name"),
        Field("password1"),
        Field("password2"),
    )
    form.is_valid()

    form.helper.form_show_errors = True
    html = render_crispy_form(form)
    assert html.count("help is-danger") == 3

    form.helper.form_show_errors = False
    html = render_crispy_form(form)
    assert html.count("help is-danger") == 0


def test_label_class_bulma():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.label_class = "is-pulled-left"
    html = render_crispy_form(form)
    assert 'class="label is-pulled-left"' in html
    # there are 7 form fields, but one of them is a checkbox without a label
    assert html.count("is-pulled-left") == 6


def test_passthrough_context():
    """
    Test to ensure that context is passed through implicitly from outside of
    the crispy form into the crispy form templates.
    """
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.template = "custom_form_template_with_context.html"

    c = {"prefix": "foo", "suffix": "bar"}

    html = render_crispy_form(form, helper=form.helper, context=c)
    assert "Got prefix: foo" in html
    assert "Got suffix: bar" in html


def test_form_horizontal():
    form = SampleForm()
    form.helper = FormHelper()
    form.helper.layout = Layout(
        "first_name",
    )
    form.helper.form_horizontal = True
    assert parse_form(form) == parse_expected("test_form_horizontal.html")
