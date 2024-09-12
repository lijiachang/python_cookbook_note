class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)

data = {'year': 2023, 'month': 4, 'day': 30}
for key, value in data.items():
    setattr(d, key, value)

print(d.year)
