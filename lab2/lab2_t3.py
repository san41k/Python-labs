class Product:

    def __init__(self, name, price, ID, \
                 weight, topic):
        if not isinstance(name, str):
            raise TypeError
        elif not isinstance(price, int):
            raise TypeError
        elif not isinstance(topic, str):
            raise TypeError
        elif not isinstance(weight, int):
            raise TypeError
        elif not isinstance(ID, int):
            raise TypeError
        elif price < 0 or weight < 0 or ID < 0:
            raise ValueError
        else:
            self.__name = name
            self.__price = price
            self.__ID = ID
            self.__weight = weight
            self.__topic = topic

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def topic(self):
        return self.__topic

    @property
    def weight(self):
        return self.__weight

    @property
    def ID(self):
        return self.__ID

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        else:
            self.__name = name

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError
        elif price < 0:
            raise ValueError
        else:
            self.__price = price

    @topic.setter
    def description(self, topic):
        if not isinstance(topic, str):
            raise TypeError
        else:
            self.__topic = topic

    @weight.setter
    def height(self, weight):
        if not isinstance(weight, int):
            raise TypeError
        elif weight < 0:
            raise ValueError
        else:
            self.__weight = weight

    @ID.setter
    def width(self, ID):
        if not isinstance(ID, int):
            raise TypeError
        elif ID < 0:
            raise ValueError
        else:
            self.__ID = ID


class Customer:

    def __init__(self, name, surname, number, \
                 email):
        if not (isinstance(surname, str) and isinstance(name, str) and isinstance(number, str) \
                and isinstance(email, str)):
            raise TypeError
        else:
            self.__name = name
            self.__surname = surname
            self.__number = number
            self.__email = email

        @property
        def name(self):
            return self.__name

        @property
        def surname(self):
            return self.__name

        @property
        def number(self):
            return self.__patronymic

        @property
        def email(self):
            return self.__phone

        @surname.setter
        def surname(self, surname):
            if not isinstance(surname, str):
                raise TypeError
            else:
                self.__surname = surname

        @name.setter
        def name(self, name):
            if not isinstance(name, str):
                raise TypeError
            else:
                self.__name = name

        @number.setter
        def number(self, number):
            if not isinstance(number, str):
                raise TypeError
            else:
                self.__number = number

        @email.setter
        def email(self, email):
            if not isinstance(email, str):
                raise TypeError
            else:
                self.__email = email


class Order:

    def __init__(self, customer, *products):
        self.__products = products
        self.__customer = customer

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if not all(isinstance(item, Product) for item in Product):
            raise TypeError
        self.__products = products

    @property
    def f_total_price(self):
        total_price = 0
        for product in self.products:
            print(product.price)
            total_price += product.price
        return total_price


if __name__ == "__main__":
    laptop = Product('HP', 8800, 227, 2200, 'Electronics')
    phone = Product('Samsung', 7999, 152, 236, 'Electronics')
    wardrobe = Product('Arino', 14400, 11, 100000, 'Furniture')
    Illya = Customer('Illya', 'Petrenko', '0673652404', 'i.petrenko@gmail.com')
    Serhiy = Customer('Serhiy', 'Radchenko', '0961894523', 'radchenko24@mail.com')
    order_number_one = Order(Illya, phone, laptop, wardrobe)
    order_number_two = Order(Serhiy, phone, wardrobe)
    print("Total price: ", order_number_one.f_total_price)
    print("Total price: ", order_number_two.f_total_price)