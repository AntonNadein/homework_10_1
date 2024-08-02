import logging

# Создаем логеры для различных компонентов программы
mask_logger = logging.getLogger("app.get_mask_account")
card_number_logger = logging.getLogger("app.get_mask_card_number")
# Перезапись логов в файле
file_handler = logging.FileHandler("logs\\masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
# handler с уровнем логгирования DEBUG для функции get_mask_account
mask_logger.addHandler(file_handler)
mask_logger.setLevel(logging.DEBUG)
# handler с уровнем логгирования DEBUG для функции get_mask_card_number
card_number_logger.addHandler(file_handler)
card_number_logger.setLevel(logging.DEBUG)


def get_mask_account(number_account: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_logger.info(f"Полученый номер банковского счета: {number_account}")
    str_number_account = str(number_account)
    if len(str_number_account) == 20:
        mask_account = "*" * 2 + str_number_account[-4:]
        mask_logger.info(f"Успешное выполнение: {mask_account} ")
        return mask_account
    else:
        mask_logger.info("Длинна номера счета не равна 20")
        return "Введен неверный номер карты/счета"


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_logger.info(f"Полученый номер банковской карты: {card_number}")
    number_card_list = []
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        mask_card_number = str_card_number[0:6] + "*" * len(str_card_number[6:-4]) + str_card_number[-4:]
        for i in range(0, len(mask_card_number), 4):
            number_card_list.append(mask_card_number[i: i + 4])
            result_number = " ".join(number_card_list)
        card_number_logger.info(f"Успешное выполнение: {result_number}")
        return result_number
    else:
        card_number_logger.info("Длинна номера карты не равна 16")
        return "Введен неверный номер карты/счета"
