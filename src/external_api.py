import os

import requests
from dotenv import load_dotenv

load_dotenv()


def amount_transaction_rub(amount: float, currency: str = "RUB") -> float | str:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции
    :param amount: сумма транзакции
    :param currency: тикер валюты транзакции
    :return: сумма транзакции в рублях
    """
    tuple_currency = ("USD", "CNY", "EUR", "KZT", "HKD")
    if currency in "RUB":
        return float(amount)
    elif currency in tuple_currency:
        API_KEY = os.getenv("API_KEY")
        to = "RUB"
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return "Нет ответа"
        return round(response.json()["result"], 2)
