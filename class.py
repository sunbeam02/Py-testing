from datetime import date

class person:
    def _init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.__salary = salary

    def capitalize(self):
        return self.name.capitalize()
    

def get_age(self):
    day, month, year = self.birthday.split('-')
    today = date.today()
    print(today)
    return ((today - date(int(year), int(month), int(day))) / 365)

#if __name__ == ""
