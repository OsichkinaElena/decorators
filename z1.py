import datetime


def make_logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        date = datetime.datetime.now()
        with open("log.txt", "a", encoding="utf-8") as output:
            print(f"Вызвана функция {old_function.__name__}", f"с аргументами {args} и {kwargs}",
                    f"дата и время вызова: {date}", f"результат: {result}", '*'*50, sep="\n", file=output)
        return result
    return new_function
@make_logger
def mini(a, b):
    return a-b

print(mini(9, 5))