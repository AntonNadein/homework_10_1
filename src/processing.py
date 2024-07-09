def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    new_list = []

    for index in list_dict:
        if index.get("state") == state:
            new_list.append(index)
    return new_list


def sort_by_date(list_dict: list, sort_parameter: bool = True) -> list:
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=sort_parameter)
    return sorted_list
