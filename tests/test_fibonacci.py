import pytest
from homework_app.fibonacci import fibonacci


@pytest.mark.valid
@pytest.mark.parametrize("test_input, expected", [
    (1, [0]),
    (2, [0, 1]),
    (8, [0, 1, 1, 2, 3, 5, 8, 13])
])
def test_parametrized(start_selenium, test_input, expected):
    assert fibonacci(test_input) == expected


@pytest.mark.invalid
@pytest.mark.parametrize("test_input, expected", [
    (-5, []),
    ('test', []),
    (5.555, [])
])
def test_parametrized_invalid(start_selenium, test_input, expected):
    assert fibonacci(test_input) == expected
