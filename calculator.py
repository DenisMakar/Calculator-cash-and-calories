import datetime as dt


date_format = '%d.%m.%Y'

class Record:
    def __init__(self, amount, comment, date=None):

        self.amount = amount
        self.comment = comment
        self.date = date

        if self.date == None:
            self.date = dt.datetime.now().date()

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self,record:Record):
        self.records.append(record)

    def get_today_stats(self):
        uses_today = 0
        today = dt.datetime.today().date()
        for day in self.records:
            if day.date == today:
                uses_today += day.amount

        return uses_today

    def get_week_stats(self):
        uses_week = 0
        today = dt.datetime.today().date()
        week =today - dt.timedelta(days=7)
        for day in self.records:
            if week <= day.data <=today:
                uses_week +=day.amount
        return uses_week

class CashCalculator(Calculator):
    def __init__(self, limit, currency):
        super().__init__(limit)
        self.currency = currency
        self.USD_RATE = 82

        self.EURO_RATE = 88
        self.RUB_RATE = 1




    def get_today_cash_remained(self,currency):
        money = {
            "rub": (self.RUB_RATE, "руб"),
            "usd": (self.USD_RATE, "USD"),
            "eur": (self.EURO_RATE, "euro")
        }

        if currency not in money:
            return "Неверный формат"

        if self.get_today_stats()<limit:
            return f"На сегодня осталось {limit - self.get_today_stats()} {currency}"
        elif self.get_today_stats() == self.limit:
            return "Денег нет, держись"
        else: return f"Денег нет, держись: твой долг - {self.limit - self.get_today_stats()} {currency}"

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {limit - self.get_today_stats()}"

        else:return "Хватит есть!"

if __name__ == "__main__":
    limit = 10000

    cash_calculator = CashCalculator(limit, "rub")
    calories_calculator = CaloriesCalculator(limit)

    # записи для денег
    r1 = Record(amount=145, comment='кофе')
    r2 = Record(amount=300, comment='Серёге за обед')
    r3 = Record(
        amount=3000,
        comment='Бар на Танин день рождения',
        date='08.11.2022')

    # записи для калорий
    r4 = Record(
        amount=118,
        comment='Кусок тортика. И ещё один.')
    r5 = Record(
        amount=84,
        comment='Йогурт.')
    r6 = Record(
        amount=1140,
        comment='Баночка чипсов.',
        date='24.02.2019')
    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

    # вывод результатов
    print(cash_calculator.get_today_cash_remained('rub'))
    print(calories_calculator.get_calories_remained())
