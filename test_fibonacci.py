from fibonacci import fibonacci

# Tests for n <= 0
def test_1():
    assert fibonacci(-5) == []

# Tests for n == 1
def test_4():
    assert fibonacci(1) == [0]

# Tests for n == 2
def test_6():
    assert fibonacci(2) == [0, 1]

# Tests for n > 2
def test_8():
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

# Test for non-numeric n
def test_9():
    assert fibonacci('test') == []

# Test for non-integer number n
def test_10():
    assert fibonacci(5.555) == []


