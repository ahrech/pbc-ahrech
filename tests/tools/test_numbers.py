import pytest

from pbc.tools.numbers import numbers_pairs


@pytest.mark.valid
@pytest.mark.parametrize("test_input, expected", [
    ((1, 4, 5, 8, 3, 6, 9), {(1, 9), (4, 6)}),
    ((1, 4, 5, 2, 8, 8, 3, 6, 9, 2), {(1, 9), (4, 6), (2, 8)}),
    ((1, 4, 5, 2, 8, 8, 3, 6, 9, 2, 25, -15), {(1, 9), (4, 6), (2, 8), (-15, 25)}),
    ((5, 5), {(5, 5)})
])
def test_parametrized(test_input, expected):
    assert numbers_pairs(*test_input) == expected


@pytest.mark.invalid
@pytest.mark.parametrize("test_input, expected", [
    ((-5,), set()),
    ((5, 7), set())
])
def test_parametrized_invalid(test_input, expected):
    assert numbers_pairs(*test_input) == expected
