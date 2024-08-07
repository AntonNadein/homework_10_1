import os

import requests
from dotenv import load_dotenv

load_dotenv()


def amount_transaction_rub(transaction: dict) -> float | str:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции
    :param transaction: словарь с транзакциями
    :return: сумма транзакции в рублях
    """
    try:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return float(amount)
        else:
            API_KEY = os.getenv("API_KEY")
            to = "RUB"
            url = (f"https://api.apilayer.com/exchangerates_data/"
                   f"convert?to={to}&from={currency}&amount={amount}")
            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                return "Нет ответа"
            return round(response.json()["result"], 2)
    except KeyError:
        return "В словаре нет ключа amount или currency"
