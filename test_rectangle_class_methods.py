import pytest
from python_code_for_unit_test import Rectangle
from mock import patch


@pytest.fixture
def rectangle():
    rectangle = Rectangle(2, 3, "black")
    return rectangle


@patch('builtins.print')
def test_describe_rectangle(mock_print, rectangle):
    rectangle.describe()
    mock_print.assert_called_with(f'Dreptunghiul are culoarea {rectangle.color}, lungimea de {rectangle.lenght} '
                                  f'si latimea de {rectangle.width}')


def test_rectangle_area(rectangle):
    assert rectangle.area() == 6


def test_rectangle_perimeter(rectangle):
    assert rectangle.perimeter() == 10


def test_rectangle_change_color(rectangle):
    rectangle.change_color("blue")
    assert rectangle.color == "blue"
