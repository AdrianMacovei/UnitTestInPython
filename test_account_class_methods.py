import pytest
from python_code_for_unit_test import Account
from mock import patch


@pytest.fixture
def account():
    account = Account(123456, "Adrian Macovei", 5000)
    return account


@patch('builtins.print')
def test_display_balance(mock_print, account):
    account.balance_display()
    mock_print.assert_called_with(f'Owner {account.owner} has in account with iban:{account.iban} '
                                  f'the amount of {account.balance} RON.')


def test_debiting_account(account):
    account.debiting(1000)
    assert account.balance == 4000


def test_deposit_account(account):
    account.deposit(1500)
    assert account.balance == 6500
