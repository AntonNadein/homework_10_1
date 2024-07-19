from functools import wraps
from typing import Any, Callable


def log(filename: str = "console") -> Callable:
    """
    Декоратор может логировать работу функции и ее результат как в файл, так и в консоль.
    :param filename: Если параметр задан, логи записываются в указанный файл.
    :return:Если вызов функции закончился ошибкой, записывается сообщение об ошибке и входные параметры функции
    """

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename == "console":
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    return f"Error: {e} Inputs:{args}, {kwargs}"
            else:
                with open(filename, "w") as file:
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} ok")
                        return result
                    except Exception as e:
                        error_file = f"Error: {e}"
                        file.write(f"{func.__name__}, {error_file}. Inputs:{args}, {kwargs}")
                        return error_file

        return wrapper

    return my_decorator
