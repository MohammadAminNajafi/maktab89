import uuid


class Client:
    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.id = str(uuid.uuid4())
        self.tickets = []

    def buy_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.tickets.append(ticket)
        return self.tickets


class BankAccountManagement:
    # Gate
    def __init__(self):
        pass

    def process_ticket(self, client):


    def __use_ticket(self):
        pass

    def __charge_ticket(self):
        pass


class MetroTravelRegistration:
    pass


class Management:
    pass


class Ticket:
    def __init__(self, ticket_type, ticket_amount=0):
        # P1 => one way ticket
        # P2 => chargable ticket
        # P3 => chargable and time zone ticket
        self.ticketType = ticket_type
        self.ticket_amount = ticket_amount
        self.ticket_serial = str(uuid.uuid4())

    def ticket_charge(self, amount):
        self.ticket_amount += amount
        return self.ticket_amount

    @classmethod
    def ticket_amount(cls, ticket_type, ticket_amount=0):
        if ticket_type == 1:
            return cls(ticket_type, ticket_amount + 200)


