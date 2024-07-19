# Проект Homework_10

## Описание:

Homework_10 - это домашняя работа на Python для SkyPro в которой реализуются функции, декораторы, генераторы.

## Использование:

1. Функцию маскировки номера банковского счета *get_mask_account* которая принимает на вход номер счета в виде числа и
   возвращает маску номера по правилу
   '**XXXX
2. Функцию маскировки номера банковской карты *get_mask_card_number* которая принимает на вход номер карты в виде числа
   и возвращает маску номера по правилу
   'XXXX XX** **** XXXX'
3. Функция *get_date*, которая принимает на вход строку с датой в формате **"2024-03-11T02:26:18.671407"** и возвращает
   строку с датой в формате
   **"ДД.ММ.ГГГГ" ("11.03.2024")**
4. Функция *mask_account_card*, которая умеет обрабатывать информацию как о картах, так и о счетах принимает строку
   формата **Maestro 7000792289606361**
   , или **Счет 73654108430135874305** и возвращает строку с замаскированным номером .
5. Функция *filter_by_state* на вход принимает два параметра список словарей и опционально значение для ключа
   **state (по умолчанию 'EXECUTED')**. Функция возвращает новый список словарей, содержащий только те словари, у
   которых ключ
   state соответствует указанному значению.
6. Функция *sort_by_date*, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
   (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате **(date)**.
7. Функция *filter_by_currency*, которая принимает на вход список словарей формата

       ```[{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"},...]```

, возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
**(например, USD)**.

8. Генератор *transaction_descriptions*, который принимает список словарей (пердставлен выше) с транзакциями и
   возвращает описание каждой операции по очереди.
9. Генератор *card_number_generator*, который выдает номера банковских карт в формате **XXXX XXXX XXXX XXXX**
10. Дероратор *log* проверяет функции на  наличие ошибок, принимает необязательный аргумент **filename**, который 
определяет имя файла, в который будут записываться логи. Если **filename** не задан, то логи выводятся в консоль.

## Тестирование:

Для тестироваия используйте файлы **[test_masks.py](tests%2Ftest_masks.py),
[test_processing.py](tests%2Ftest_processing.py), [test_widget.py](tests%2Ftest_widget.py), 
[test_generators.py](tests%2Ftest_generators.py), [test_decorators.py](tests%2Ftest_decorators.py)**
test coverage [index.html](htmlcov%2Findex.html)

## Лицензия:

Этот проект не имеет лицензий.
