from typing import List, Dict, Any


def filter_by_state(list_dict: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    '''
    Фильтрует список транзакций по заданному состоянию
    :param list_dict: Список словарей с данными о транзакциях.
    :param state: Состояние транзакции для фильтрации (по умолчанию 'EXECUTED').
    :return:Новый список, содержащий только те транзакции, у которых ключ 'state' равен переданному значению.
    '''
    new_list = []

    for index in list_dict:
        if index.get("state") == state:
            new_list.append(index)
    return new_list


def sort_by_date(list_dict: List[Dict[str, any]], sort_parameter: bool = True) -> List[Dict[str, Any]]:
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=sort_parameter)
    return sorted_list
