from src.filtration import filter_dictionary, filter_dictionary_description
from src.open_file import open_csv, open_excel
from src.processing import sort_by_date
from src.selection_cycles import triple_question, while_true_question
from src.utils import json_to_dict
from src.widget import get_date, mask_account_card


def main():
    print(
        "\nПривет! Добро пожаловать в программу работы с "
        "банковскими транзакциями."
        "\nВыберите необходимый пункт меню:"
    )

    str_database = (
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    answer = triple_question(str_database, 1, 2, 3)
    if answer == 1:
        data_dict = json_to_dict("operations.json")
        print("Для обработки выбран JSON-файл.\n")
    elif answer == 2:
        data_dict = open_csv("transaction.csv")
        print("Для обработки выбран CSV-файл.\n")
    elif answer == 3:
        data_dict = open_excel("transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.\n")
    else:
        exit("Вы выбрали выход из программы")
    str_status = (
        "Введите статус, по которому необходимо "
        "выполнить фильтрацию. \nДоступные для фильтровки "
        "статусы: EXECUTED, CANCELED, PENDING\n"
    )
    answer_status = triple_question(
        str_status, "EXECUTED", "CANCELED", "PENDING"
    )
    if answer_status is None:
        exit("Вы выбрали выход из программы")
    filter_dict = filter_dictionary(data_dict, answer_status)

    str_sort_date = "Отсортировать операции по дате? Да/Нет\n"
    str_type_sort = "Отсортировать по возрастанию или по убыванию?\n"
    str_sort_currency = "Выводить только рублевые тразакции? Да/Нет\n"
    str_sort_word = (
        "Отфильтровать список транзакций по "
        "определенному слову в описании? Да/Нет\n"
    )
    # Сортировка по дате операции
    sort_date = while_true_question(str_sort_date, "да", "нет")
    if sort_date == "да":
        #
        # Напрвление сортировки
        type_sort = while_true_question(
            str_type_sort, "возрастанию", "убыванию"
        )
        if type_sort == "возрастанию":
            data_sort_list = sort_by_date(filter_dict, False)
        else:
            data_sort_list = sort_by_date(filter_dict, True)
    else:
        data_sort_list = filter_dict

    # Фильтрация по рублю
    sort_currency = while_true_question(str_sort_currency, "да", "нет")
    if sort_currency == "да":
        the_rub_sort = [
            d
            for d in data_sort_list
            if d["operationAmount"]["currency"]["code"] == "RUB"
        ]
    else:
        the_rub_sort = data_sort_list
    # Фильтрация по описанию
    sort_word = while_true_question(str_sort_word, "да", "нет")
    if sort_word == "да":
        the_rub_sort = filter_dictionary_description(
            the_rub_sort, input("\nВведите описание операции: ")
        )

    len_operation = len(the_rub_sort)
    if len_operation > 0:
        print(
            "Распечатываю итоговый список транзакций...\n"
            f"Всего банковских операций в выборке: {len_operation}"
        )
        for dict_operation in the_rub_sort:
            date_operation = get_date(dict_operation.get("date"))
            from_card = mask_account_card(dict_operation.get("from"))
            to_card = mask_account_card(dict_operation.get("to"))
            print(
                f'{date_operation} {dict_operation.get("description")}\n'
                f"{from_card} -> {to_card}\n"
                f'Сумма: {dict_operation["operationAmount"]["amount"]}\n'
            )
    else:
        print(
            "Не найдено ни одной транзакции,"
            " подходящей под ваши условия фильтрации\n"
        )


if __name__ == "__main__":
    main()
