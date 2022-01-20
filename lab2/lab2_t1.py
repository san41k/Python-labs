class Rectangle:

    def __init__(self, length = 1.0, width = 1.0):
        if not (isinstance(length, float) and isinstance(width, float)):
            raise TypeError
        elif not (0.0 < length <= 20.0 and 0.0 <  width <= 20.0):
            raise ValueError
        else:
            self.__length = length
            self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError
        elif not 0.0 < length <= 20.0:
            raise ValueError
        else:
            self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError
        elif not 0.0 < width <= 20.0:
            raise ValueError
        else:
            self.__width = width

    @property
    def area(self):
        return self.__width * self.__length

    @property
    def perimeter(self):
        return (self.__length + self.__width) * 2

if __name__ == "__main__":
    rect = Rectangle(12.0, 20.)
    print('Length: ', rect.length, '\tWidth: ', rect.width)
    print('Perimeter:', rect.pimeter)
    print('Area:', rect.area, '\n')
    rect.length = 2.2
    rect.width = 4.0
    print('Length: ', rect.length, '\tWidth: ', rect.width)
    print('Perimeter:', rect.perimeter)
    print('Area:', rect.area, '\n')