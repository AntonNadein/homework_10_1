def while_true_question(question, answer_true, answer_false):
    while True:
        string = (input(f"{question}: ")).lower()
        if string in [answer_true.lower()]:
            return answer_true.lower()
        elif string in [answer_false.lower()]:
            return answer_false.lower()
        elif string in ["exit"]:
            break
        else:
            print(f"Введите {answer_true} или {answer_false}\n")


def triple_question(question, answer_one, answer_two, answer_three):
    while True:
        string = input(f"{question}: ")
        if string.isdigit():
            string_int = int(string)
            if string_int == answer_one:
                return answer_one
            elif string_int == answer_two:
                return answer_two
            elif string_int == answer_three:
                return answer_three
            elif string_int == 0:
                break
            else:
                print(
                    f"Статус операции {string} недоступен\n"
                    f"\nВведите {answer_one},{answer_two} или {answer_three}\n"
                )
        elif (
            type(string) is str
            and type(answer_one) is str
            and type(answer_two) is str
            and type(answer_three) is str
        ):
            string_str = string.lower()
            if string_str in [answer_one.lower()]:
                return answer_one.lower().lower()
            elif string_str in [answer_two.lower()]:
                return answer_two.lower()
            elif string_str in [answer_three.lower()]:
                return answer_three.lower()
            elif string_str in ["exit"]:
                break
            else:
                print(f"Статус операции {string} недоступен.\n")
        else:
            print("Введен неверный формат введите слово или число\n")
