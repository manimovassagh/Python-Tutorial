from calculater import calc


def test_add_numbers():
    result = calc.add_numbers(4, 6)
    assert result == 10


def test_multiply_numbers():
    result = calc.multiply_nums(2,4)
    assert result == 8
