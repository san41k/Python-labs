import re
import json


class Note:
    def __init__(self, name, surname=None, number=None, date=None):
        self.__name = name
        self.__number = number
        self.__surname = surname
        self.__date = date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, str) and number is not None:
            raise TypeError
        self.__number = number

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str) and surname is not None:
            raise TypeError
        self.__surname = surname

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if not isinstance(date, str) and date is not None:
            raise TypeError
        self.__date = date

    def to_dict(self):
        return {'Number': self.number, 'Name': self.name, 'Surname': self.surname, 'Date': self.date}

    def __str__(self):
        return f'Number: {self.number}, Name: {self.name}, Surname: {self.surname}, Date: {self.date}'


class Notebook:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    def __add__(self, other):
        if not isinstance(other, Note):
            return NotImplemented
        with open(f"{self.name}.json", 'r') as f:
            k = json.load(f)
            k.append(other.to_dict())
        with open(f"{self.name}.json", 'w') as f:
            json.dump(k, f)

    def __sub__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        with open(f"{self.name}.json", 'r') as f:
            t = json.load(f)
            for record in t:
                if record['Name'] == other:
                    t.remove(record)
        with open(f"{self.name}.json", 'w') as f:
            json.dump(t, f)

    def __mul__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        with open(f"{self.name}.json", 'r') as f:
            t = json.load(f)
            for record in t:
                if record['Name'] == other:
                    return str(record)
        return f'Anyone this name ' + other

    def __str__(self):
        with open(f"{self.name}.json", 'r') as f:
            t = json.load(f)
            if len(t):
                return "\n".join(map(str, t))
            return "\t\t (EMPTY)\n"


try:
    n = Notebook("notebook")
    n + Note("Serhiy")
    print(n * "Serhiy")

except TypeError as er:
    print(er)