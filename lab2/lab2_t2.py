import math

class Rational:

    def __init__(self, selected_numerator = 1, selected_denominator = 1):
        if not (isinstance(selected_numerator, int) or isinstance(selected_numerator, int)):
            raise TypeError
        if not selected_denominator:
            raise ZeroDivisionError
        else:
            divider = math.gcd(selected_numerator, selected_denominator)
            self.__numerator = selected_numerator // divider
            self.__denominator = selected_denominator // divider

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError
        else:
            self.__numerator = numerator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise TypeError
        else:
            self.__denominator = denominator

    @property
    def show_common_fraction(self):
        divider = math.gcd(self.__numerator, self.__denominator)
        self.__numerator // divider
        self.__denominator // divider
        return f' {self.__numerator} / {self.__denominator}'

    @property
    def show_decimal(self):
        return self.__numerator / self.__denominator

if __name__ == "__main__":
    number = Rational(2, 4)
    print('Rational number ', number.show_common_fraction)
    print('Equals ', number.show_decimal, '\n')
    number.numerator = 7
    number.denominator = 21
    print('Rational number ', number.show_common_fraction)
    print('Equals ', number.show_decimal, '\n')