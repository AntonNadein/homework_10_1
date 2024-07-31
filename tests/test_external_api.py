import os
from unittest.mock import patch, Mock

from src.external_api import amount_transaction_rub
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


@patch('requests.get')
def test_amount_transaction_rub(mocked_response, dict_external_api_usd):
    mocked_response.return_value.status_code = 201
    result = amount_transaction_rub(dict_external_api_usd)
    assert result == 'Нет ответа'


@patch('requests.get')
def test_amount_transaction_rub_currency(mocked_get, dict_external_api_usd):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {'result': 800}
    result = amount_transaction_rub(dict_external_api_usd)
    assert result == 800
    mocked_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100", headers={"apikey": API_KEY}
    )


def test_amount_transaction_rub_not_currency(dict_external_api_rub):
    result = amount_transaction_rub(dict_external_api_rub)
    assert result == 31957.58


def test_amount_transaction_rub_key_error():
    result = amount_transaction_rub({})
    assert result == "В словаре нет ключа amount или currency"