import os
from unittest.mock import patch, Mock

from src.external_api import amount_transaction_rub
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


@patch('requests.get')
def test_amount_transaction_rub(mocked_response):
    mocked_response.return_value.status_code = 201
    result = amount_transaction_rub(100, currency="USD")
    assert result == 'Нет ответа'


@patch('requests.get')
def test_amount_transaction_rub_currency(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {'result': 800}
    result = amount_transaction_rub(100, currency="USD")
    assert result == 800
    mocked_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100", headers={"apikey": API_KEY}
    )


def test_amount_transaction_rub_not_currency():
    result = amount_transaction_rub(1000)
    assert result == 1000.00


def test_amount_transaction_rub_input_RUB():
    result = amount_transaction_rub(1000, currency="RUB")
    assert result == 1000.00
