import json
import os
from typing import Any, Dict, List


def json_to_dict(file_name: str) -> List[Dict[str, Any]]:
    """
    Принимает на вход имя JSON-файла и возвращает список словарей
    :param file_name: имя файла, с расширением JSON
    :return: список словарей
    """
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
    try:
        with open(PATH_TO_FILE, "r", encoding="utf-8") as file:
            parsed_data = json.load(file)
        return parsed_data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
