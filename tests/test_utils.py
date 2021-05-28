from crispy_forms.utils import list_intersection


def test_list_intersection():
    assert list_intersection([1, 3], [2, 3]) == [3]
