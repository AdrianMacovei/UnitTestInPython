from python_code_for_unit_test import Employee
import pytest
from mock import patch


@pytest.fixture
def employee():
    employee = Employee("Adrian", "Macovei", 2000)
    return employee


@patch('builtins.print')
def test_describe_rectangle(mock_print, employee):
    employee.describe_employee()
    mock_print.assert_called_with(f'I am {employee.first_name} {employee.second_name} '
                                  f'and my salary is {employee.salary} euro.')


def test_complete_name(employee):
    assert employee.complet_name() == "Adrian Macovei"


def test_month_salary(employee):
    assert employee.month_salary() == 2000


def test_annual_salary(employee):
    assert employee.annual_salary() == 24000


def test_increase_salary(employee):
    employee_salary_before = employee.salary
    employee.increase_salary(25)
    assert employee.salary == employee_salary_before + (employee_salary_before * 0.25)
