import re
from typing import Any, Dict, List


def filter_dictionary(
    list_dict: List[Dict[str, Any]], string: str
) -> List[Dict[str, Any]] | str:
    """Фильтр списка словарей по параметру state"""
    list_dict_filtered = []
    try:
        for dict_operation in list_dict:
            if dict_operation.get("state") is None:
                continue
            elif string == "":
                return []
            else:
                pattern = re.compile(string, flags=re.I)
                if pattern.search(dict_operation.get("state")):
                    list_dict_filtered.append(dict_operation)
        return list_dict_filtered
    except TypeError:
        return "Неожиданный тип данных"
