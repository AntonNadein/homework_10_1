import tempfile

from src.decorators import log


def test_log():
    """Тестирует выполнение декорированной функции"""

    @log()
    def dev_null(x, y):
        return x / y

    assert dev_null(5, 1) == 5.0
    assert dev_null(5, 0) == "Error: division by zero Inputs:(5, 0), {}"


def test_log_good_file_log():
    """Тестирует запись в файл после успешного выполнения"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def dev_null(x, y):
        return x / y

    dev_null(1, 2)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert logs == "dev_null ok"


def test_log_good_file_log_error():
    """Тестирует запись в файл после НЕ успешного выполнения"""

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def dev_null(x, y):
        return x / y

    dev_null(1, 0)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert logs == "dev_null, Error: division by zero. Inputs:(1, 0), {}"
