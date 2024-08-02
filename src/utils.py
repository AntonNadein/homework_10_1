import json
import logging
import os
from typing import Any, Dict, List

json_to_dict_logger = logging.getLogger("app.json_to_dict")
# Перезапись логов в файле
file_handler = logging.FileHandler("logs\\utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
# handler с уровнем логгирования DEBUG для функции get_mask_account
json_to_dict_logger.addHandler(file_handler)
json_to_dict_logger.setLevel(logging.DEBUG)


def json_to_dict(file_name: str) -> List[Dict[str, Any]]:
    """
    Принимает на вход имя JSON-файла и возвращает список словарей
    :param file_name: имя файла, с расширением JSON
    :return: список словарей
    """
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
    json_to_dict_logger.info(f"Путь к файлу {PATH_TO_FILE}")
    json_to_dict_logger.info(f"Имя к файла {file_name}")
    try:
        with open(PATH_TO_FILE, "r", encoding="utf-8") as file:
            parsed_data = json.load(file)
        json_to_dict_logger.info("Файл открыт")
        return parsed_data
    except (FileNotFoundError, json.decoder.JSONDecodeError) as ex:
        json_to_dict_logger.error(f"Произошла ошибка: {ex}")
        return []
