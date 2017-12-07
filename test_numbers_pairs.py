from numbers_pairs import numbers_pairs


# Tests for len(number) < 2
def test_1():
    assert numbers_pairs(-5) == set()

# Tests for len(number) >= 2
def test_2():
    assert numbers_pairs(1, 4, 5, 8, 3, 6, 9) == {(1, 9), (4, 6)}


def test_3():
    assert numbers_pairs(1, 4, 5, 2, 8, 8, 3, 6, 9, 2) == {(1, 9), (4, 6), (2, 8)}


def test_4():
    assert numbers_pairs(1, 4, 5, 2, 8, 8, 3, 6, 9, 2, 25, -15) == {(1, 9), (4, 6), (2, 8), (-15, 25)}

def test_5():
    assert numbers_pairs(5, 5) == {(5, 5)}

def test_6():
    assert numbers_pairs(5, 7) == set()