import uuid
from datetime import datetime


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

    def travel_time(self, ):
        pass


class Gate:
    # Gate
    cost = 2500
    def __init__(self):
        pass

    def process_ticket(self, client, choosed_ticket_type):
        tickets = client.tickets
        if len(tickets) <= 0:
            return -1
        else:
            for ticket in tickets:
                if ticket.status:
                    if ticket.ticket_type == choosed_ticket_type:
                        use_ticket = ticket
                        # BankAccountManagement.__use_ticket(self, ticket)
                        print(ticket.ticket_amount)
                        print(Gate.__use_ticket(self, ticket))
                        print(ticket.ticket_amount)
                        break

    def __use_ticket(self, use_ticket):
        if isinstance(use_ticket, Ticket):
            if use_ticket.ticket_type == 1:
                if use_ticket.ticket_amount < 1500:
                    return -2
                else:
                    use_ticket.ticket_amount -= 1500
                    # return use_ticket.ticket_amount
                    return 0
            else:
                if use_ticket.status and use_ticket.ticket_type == 2:
                    use_ticket.status = False
    def __charge_ticket(self):
        pass

    def start(self, start):
        pass


class MetroTravelRegistration:
    def __init__(self):
        pass


class Management:
    pass


class Ticket:
    def __init__(self, ticket_type, ticket_amount=0):
        # P1 => one way ticket
        # P2 => chargable ticket
        # P3 => chargable and time zone ticket
        self.ticket_type = ticket_type
        self.ticket_amount = ticket_amount
        self.ticket_serial = str(uuid.uuid4())
        self.status = True

    def ticket_charge(self, amount):
        self.ticket_amount += amount
        return self.ticket_amount

    @classmethod
    def ticket_amount(cls, ticket_type, ticket_amount=0):
        if ticket_type == 1:
            return cls(ticket_type, ticket_amount + 200)


# زمان شروع و پایان