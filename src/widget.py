from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция создает маски карт и счетов"""
    new_numbers = []
    new_name = []
    if info_card == "" or info_card is None:
        return ""
    else:
        info_card_list = info_card.split(" ")
        for number in info_card_list:
            if number.isdigit():
                new_numbers.append(number)
            elif number.isalpha():
                new_name.append(number)
        number_card_account_str = "".join(new_numbers)
        len_number_card = len(number_card_account_str)
        if len_number_card == 16:
            mask_number = get_mask_card_number(int(number_card_account_str))
        elif len_number_card == 20:
            mask_number = get_mask_account(int(number_card_account_str))
        else:
            return "Введен неверный номер карты/счета"
        return f'{" ".join(new_name)} {mask_number}'


def get_date(dates: str) -> str:
    """Функция, которая выводит дату в формает DD.MM.YYYY"""
    return f"{dates[8:10]}.{dates[5:7]}.{dates[0:4]}"
