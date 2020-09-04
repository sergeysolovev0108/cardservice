from datetime import datetime, date
from random import Random

import calendar


def generate_club_card_number():
    """Генерируем рандомный 16 значный номер карты"""
    card_number = ''
    while len(card_number) < 16:
        digit = Random().choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        card_number += digit
    return int(card_number)


def add_month(dat, times):
    """Функция обавляет месяца к указанной дате и возвращает дату"""
    month = dat.month - 1 + times
    year = dat.year + month // 12
    month = month % 12 + 1
    day = min(dat.day, calendar.monthrange(year, month)[1])
    end_date = date(year, month, day)
    return end_date


def add_time(activate_date, end_date):
    times = int(activate_date.value)  # Кол-во месяцев на которое продлевается абонемент

    """Приводим дату в формат для сравнения"""

    a = str(datetime.now()).replace(' ', '-', ).replace(':', '-').replace('.', '-').split('-')
    now = datetime(int(a[0]), int(a[1]), int(a[2]))
    """Проверяем поле окончания срока на наличие данных"""
    if end_date is not None:
        b = str(end_date).replace(' ', '-', ).replace(':', '-').replace('.', '-').split('-')
        end_date = datetime(int(b[0]), int(b[1]), int(b[2]))

    """добавляем время"""

    if end_date is None or now > end_date:
        end_date = add_month(now, times)
        return end_date
    else:
        end_date = add_month(end_date, times)
        return end_date


def add_balance(balance, active_date):
    """Добавляет стоимость продления в общей баланс"""
    price = int(active_date.price)
    balance += price
    return balance
