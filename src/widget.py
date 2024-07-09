import datetime


def get_hello_message_from_time() -> str:
    """
    Функция для получения приветственного сообщения в зависимости от времени суток
    :return:
    """
    date = datetime.datetime.today()
    time = datetime.datetime.today().time().strftime("%H %M %S").split(" ")

    weekday = datetime.datetime.weekday(date)
    week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    if 6 <= int(time[0]) <= 11:
        return f"Доброе утро! Сегодня {week[weekday]}."
    elif 12 <= int(time[0]) <= 18:
        return f"Добрый день! Сегодня {week[weekday]}."
    elif 19 <= int(time[0]) <= 22:
        return f"Добрый вечер! Сегодня {week[weekday]}."
    else:
        return f"Доброй ночи! Сегодня {week[weekday]}."


if __name__ == '__main__':
    print(get_hello_message_from_time())
