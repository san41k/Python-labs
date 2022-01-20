import json
import datetime


class Ticket:
    id_generator = 0

    def __init__(self):
        with open("event.json", 'r') as f:
            event = json.load(f)
        self.price = event['event']['price']
        Ticket.id_generator = event['event']['number_of_tickets']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value > Ticket.id_generator:
            raise ValueError
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__price = value

    def __str__(self):
        return f'{self.__class__.__name__} {self.price} {self.id}'


class AdvanceTicket(Ticket):

    def __init__(self):
        super().__init__()
        with open("event.json", 'r') as f:
            t = json.load(f)['event']['Advance']
            if not isinstance(t, float):
                raise TypeError
            self.price *= t



class LateTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("event.json", 'r') as f:
            t = json.load(f)['event']['Late']
            if not isinstance(t, float):
                raise TypeError
            self.price *= t


class StudentTicket(Ticket):
    def __init__(self):
        super().__init__()
        with open("event.json", 'r') as f:
            t = json.load(f)['event']['Student']
            if not isinstance(t, float):
                raise TypeError
            self.price *= t


class Event:
    def __init__(self):
        with open("event.json", 'r') as f:
            event = json.load(f)
        self.date = datetime.datetime(*list(event["event"]["date"]))
        self.regular = Ticket()
        self.student = StudentTicket()
        self.advanced = AdvanceTicket()
        self.late = LateTicket()

    def show_tickets(self):
        date_dif = (self.date - datetime.datetime.now()).days
        if date_dif < 0:
            return f"too late"
        with open("event.json", 'r') as f:
            event = json.load(f)
        if not event['event']['number_of_tickets']:
            return f"too late"
        if date_dif > 60:
            return f"Ticket price: {self.advanced.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"
        elif 0 <= date_dif < 10:
            return f"Ticket price: {self.late.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"
        else:
            return f"Ticket price: {self.regular.price}$\nFor students: " \
                   f"{self.student.price}$\n{event['event']['number_of_tickets']}" \
                   f" tickets left\n\n"

    def buy_ticket(self, is_student):
        date = datetime.datetime.now()
        with open("event.json", 'r') as f:
            event = json.load(f)
        if event["event"]["number_of_tickets"] <= 0:
            raise ValueError
        date_dif = (self.date - datetime.datetime.now()).days
        if date_dif < 0:
            raise TimeoutError
        event["event"]["number_of_tickets"] -= 1
        with open("event.json", 'w') as f:
            json.dump(event, f)
        if is_student:
            ticket = self.student
        elif date_dif > 60:
            ticket = self.advanced
        elif 0 <= date_dif < 10:
            ticket = self.late
        else:
            ticket = self.regular
        ticket.id = Ticket.id_generator
        Ticket.id_generator -= 1
        with open("tickets.json", 'r') as f:
            tickets = json.load(f)
        if 'event' not in tickets:
            tickets['event'] = {}
        if not str(ticket.id) in tickets['event']:
            tickets['event'][str(ticket.id)] = {}
            tickets['event'][str(ticket.id)]['price'] = ticket.price
            tickets['event'][str(ticket.id)]['purchase_date'] = str(date)
        with open("tickets.json", 'w') as f:
            json.dump(tickets, f)
        return f"You successfully bought your ticket!\n"\
               f"Id:{ticket.id}\n\n"

    @staticmethod
    def search_ticket(ticket_id):
        with open("tickets.json", 'r') as f:
            tickets = json.load(f)
        if "event" not in tickets:
            raise KeyError
        if ticket_id not in tickets["event"]:
            raise KeyError
        price = tickets["event"][ticket_id]["price"]
        date = tickets["event"][ticket_id]["purchase_date"]
        return f"YOUR TICKET:\nTicket id: {ticket_id}\n" \
               f"Price: {price}\nPurchase date: {date}"


responce = ""
event = Event()
print(event.show_tickets())
print(event.date)
while not responce.upper() == "Q":
    responce = input("Do you want to search or buy tickets? S/B\nq - to quit\n")
    try:
        if responce.upper() == "S":
            id = input("Enter id ")
            print(event.search_ticket(id))
        elif responce.upper() == "B":
            responce = input("Are you a student? Y/N\n")
            try:
                if responce.upper() == "Y":
                    st = True
                elif responce.upper() == "N":
                    st = False
                else:
                    raise TypeError
                print(event.buy_ticket(st))
            except TypeError:
                print
        else:
            raise TypeError
        print(event.show_tickets())
    except TypeError:
        print
    except KeyError as er:
        print(er)