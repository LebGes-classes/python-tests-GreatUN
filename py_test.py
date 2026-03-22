import pytest
from test_file import *

# Использование параметризации для позитивных тестов сложения
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
])
@pytest.mark.feature('add')
def test_add_param(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.feature('subtract')
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

@pytest.mark.feature('multiply')
def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(0, 100) == 0

@pytest.mark.feature('divide')
def test_divide():
    assert divide(10, 5) == 2.0
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# Тестирование ошибки типа
@pytest.mark.parametrize("func", [add, subtract, multiply, divide])
def test_types_validation(func):
    with pytest.raises(TypeError):
        func("test", 5)

    with pytest.raises(TypeError):
        func(10, None)
