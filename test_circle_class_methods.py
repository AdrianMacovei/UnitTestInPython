import pytest
from mock import patch
from python_code_for_unit_test import Circle


@pytest.fixture
def circle():
    circle = Circle(4, "black")
    return circle


@patch('builtins.print')
def test_describe_circle(mock_print, circle):
    circle.describe_circle()
    mock_print.assert_called_with(f'Circle color is {circle.color} and radius {circle.radius}')


def test_circle_area(circle):
    assert circle.area() == 50.27


def test_circle_diameter(circle):
    assert circle.diameter() == 8


def test_circle_circumference(circle):
    assert circle.circumference() == 25.13