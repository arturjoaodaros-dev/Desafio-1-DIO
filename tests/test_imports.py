from Backend.Account import Account
from Client.Client import Client
from Transaction import Transaction


def test_modules_import_without_circular_error():
    assert Account is not None
    assert Client is not None
    assert Transaction is not None
