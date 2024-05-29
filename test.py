def add_numbers(a, b):
    return a + b


def test_add_numbers():
    assert add_numbers(3, 4) == 7
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


test_add_numbers()
