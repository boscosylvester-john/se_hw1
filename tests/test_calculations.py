import pytest
from src import add, subtract, multiply, divide, get_input, get_operator


def test_add():
    assert add(1, 2) == 3
    assert add(1, -2) == -1


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1, -2) == 3


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1, -2) == -2


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(1, -2) == -0.5


def test_valid_inputs():
    assert get_input("3,5") == [3,5]


def test_valid_operator():
    assert get_operator("+") == "+"
    assert get_operator("-") == "-"
    assert get_operator("*") == "*"
    assert get_operator("/") == "/"


def test_invalid_inputs():
    with pytest.raises(ValueError):
        assert get_input("3,a")
    with pytest.raises(ValueError):
        assert get_input("a,3")
    with pytest.raises(ValueError):
        assert get_input("a,a")


def test_invalid_operator():
    with pytest.raises(ValueError):
        assert get_operator("++")
    with pytest.raises(ValueError):
        assert get_operator("1")
    with pytest.raises(ValueError):
        assert get_operator("asdads")