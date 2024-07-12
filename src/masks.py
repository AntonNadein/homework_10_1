def get_mask_account(number_account: int) -> str:
    """Функция маскировки номера банковского счета"""
    str_number_account = str(number_account)
    if len(str_number_account) == 20:
        return "*" * 2 + str_number_account[-4:]
    else:
        return "Введен неверный номер карты/счета"


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    number_card_list = []
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        mask_card_number = str_card_number[0:6] + "*" * len(str_card_number[6:-4]) + str_card_number[-4:]
        for i in range(0, len(mask_card_number), 4):
            number_card_list.append(mask_card_number[i: i + 4])
        return " ".join(number_card_list)
    else:
        return "Введен неверный номер карты/счета"
