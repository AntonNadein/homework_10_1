import csv
import logging
import os
from typing import Any, Dict, List

import pandas as pd

from src.constant import PATH_TO_FILE

open_csv_logger = logging.getLogger("app.open_csv")
open_excel_logger = logging.getLogger("app.open_excel")
# Перезапись логов в файле
file_handler = logging.FileHandler(
    "logs\\open_file.log", mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
# handler с уровнем логгирования DEBUG для функции get_mask_account
open_csv_logger.addHandler(file_handler)
open_csv_logger.setLevel(logging.DEBUG)
open_excel_logger.addHandler(file_handler)
open_excel_logger.setLevel(logging.DEBUG)


def open_csv(file_name: str) -> List[Dict[str, Any]] | str:
    """
    Преобразовывает csv файл в список словарей
    :param file_name: Имя файла в формате .csv
    :return: Список словарей в приведенном формате
    """
    csv_list_dict = []
    try:
        with open(
            os.path.join(PATH_TO_FILE, file_name), "r", encoding="utf-8"
        ) as file:
            open_csv_logger.info(f"Открываемый файл {file}")
            csv_data = csv.reader(file, delimiter=";")
            for row in csv_data:
                # условие пропуска первой строки без next
                if row[0] != "id":
                    csv_dict = {
                        "id": row[0],
                        "state": row[1],
                        "date": row[2],
                        "operationAmount": {
                            "amount": row[3],
                            "currency": {"name": row[4], "code": row[5]},
                        },
                        "description": row[8],
                        "from": row[6],
                        "to": row[7],
                    }
                    csv_list_dict.append(csv_dict)
            # с ней не проходят тесты, но работает программа
            # open_csv_logger.info(f"Первая строка {csv_list_dict[0]}")
            return csv_list_dict
    except FileNotFoundError as e:
        open_csv_logger.error(f"Произошла ошибка: {e}")
        return "Файл отсутствует или неправильно назван"


def open_excel(file_name: str) -> List[Dict[str, Any]] | str:
    """
    Преобразовывает excel файл в список словарей
    :param file_name: file_name: Имя файла в формате .excel
    :return: Список словарей в приведенном формате
    """
    list_dict_excel = []
    try:
        file = os.path.join(PATH_TO_FILE, file_name)
        open_excel_logger.info(f"Открываемый файл {file}")
        excel_data = pd.read_excel(file)
        for i in range(len(excel_data)):
            # проверка на пустую строку через отсутствие id
            if not pd.notna(excel_data.loc[i, "id"]):
                continue
            elif not pd.notna(excel_data.loc[i, "from"]):
                id_dict = {
                    "id": int(excel_data.loc[i, "id"]),
                    "state": excel_data.loc[i, "state"],
                    "date": excel_data.loc[i, "date"],
                    "operationAmount": {
                        "amount": float(excel_data.loc[i, "amount"]),
                        "currency": {
                            "name": excel_data.loc[i, "currency_name"],
                            "code": excel_data.loc[i, "currency_code"],
                        },
                    },
                    "description": excel_data.loc[i, "description"],
                    "from": None,
                    "to": excel_data.loc[i, "to"],
                }
                list_dict_excel.append(id_dict)
            else:
                id_dict = {
                    "id": int(excel_data.loc[i, "id"]),
                    "state": excel_data.loc[i, "state"],
                    "date": excel_data.loc[i, "date"],
                    "operationAmount": {
                        "amount": float(excel_data.loc[i, "amount"]),
                        "currency": {
                            "name": excel_data.loc[i, "currency_name"],
                            "code": excel_data.loc[i, "currency_code"],
                        },
                    },
                    "description": excel_data.loc[i, "description"],
                    "from": excel_data.loc[i, "from"],
                    "to": excel_data.loc[i, "to"],
                }
                list_dict_excel.append(id_dict)
        open_excel_logger.info(f"Первая строка {list_dict_excel[0]}")
        return list_dict_excel
    except FileNotFoundError as e:
        open_excel_logger.error(f"Произошла ошибка: {e}")
        return "Файл отсутствует или неправильно назван"
