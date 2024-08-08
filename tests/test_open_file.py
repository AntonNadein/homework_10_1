from unittest.mock import mock_open, patch

import pandas as pd

from src.open_file import open_csv, open_excel, path_to_file


def test_path_to_file():
    """тест пути файла"""
    assert (
        path_to_file("test.src") == "C:\\Users\\Антон\\Desktop\\PyProject\\"
        "homework_10_1\\src\\..\\data\\test.src"
    )


def test_error_open_csv():
    """Проверка наличия файла в директории"""
    result = open_csv("transaction.cs")
    assert result == "Файл отсутствует или неправильно назван"


def test_error_open_excel():
    """Проверка наличия файла в директории"""
    result = open_excel("transactions_excel.xls")
    assert result == "Файл отсутствует или неправильно назван"


@patch("csv.reader")
def test_open_csv(mocked_csv):
    """Проверка нормальной работы"""
    mocked_csv.return_value = [
        [
            "is",
            "state",
            "date",
            "amount",
            "currency_name",
            "currency_code",
            "from",
            "to",
            "description",
        ]
    ]
    result = open_csv("transaction.csv")
    assert result == [
        {
            "date": "date",
            "description": "description",
            "from": "from",
            "id": "is",
            "operationAmount": {
                "amount": "amount",
                "currency": {"code": "currency_code", "name": "currency_name"},
            },
            "state": "state",
            "to": "to",
        }
    ]


@patch("csv.reader")
def test_open_csv1(mocked_csv):
    """Проверка пропуска первой строки"""
    mocked_csv.return_value = [
        [
            "id",
            "state",
            "date",
            "amount",
            "currency_name",
            "currency_code",
            "from",
            "to",
            "description",
        ]
    ]
    result = open_csv("transaction.csv")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_open_csv_excel(mock_file):
    assert open("../Data/transactions_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../Data/transactions_excel.xlsx")

    assert open("../Data/transactions.csv").read() == "data"
    mock_file.assert_called_with("../Data/transactions.csv")


@patch("pandas.read_excel")
def test_read_xlsx_transactions(mock_read_excel):
    """Проверка нормальной работы"""
    file_name = "test.xlsx"
    # создается база данных файла
    data = {
        "id": [1, "2", None, 4],
        "state": ["success", "failed", "success", "failed"],
        "date": ["2022-01-01", "2022-01-02", "-", "2022-01-02"],
        "amount": [100, 200, 300, 400],
        "currency_name": ["USD", "EUR", "RUB", "EU"],
        "currency_code": ["USD", "EUR", "Rub", "EU"],
        "description": [
            "Test transaction",
            "Another transaction",
            "transaction",
            "Another",
        ],
        "from": ["Card_1", "Card_2", "Card_3", "Card_4"],
        "to": ["Card_5", "Card_5", "Card_5", "Card_5"],
    }
    df = pd.DataFrame(data)

    mock_read_excel.return_value = df
    result = open_excel(file_name)
    assert result[0] == {
        "id": 1,
        "state": "success",
        "date": "2022-01-01",
        "operationAmount": {
            "amount": 100.0,
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Test transaction",
        "from": "Card_1",
        "to": "Card_5",
    }
    assert result[1] == {
        "id": 2,
        "state": "failed",
        "date": "2022-01-02",
        "operationAmount": {
            "amount": 200,
            "currency": {"name": "EUR", "code": "EUR"},
        },
        "description": "Another transaction",
        "from": "Card_2",
        "to": "Card_5",
    }
    # Проверка пропуска строки с отсутствием id
    # Выдает следующую строку
    assert result[2] == {
        "id": 4,
        "state": "failed",
        "date": "2022-01-02",
        "operationAmount": {
            "amount": 400.0,
            "currency": {"name": "EU", "code": "EU"},
        },
        "description": "Another",
        "from": "Card_4",
        "to": "Card_5",
    }
