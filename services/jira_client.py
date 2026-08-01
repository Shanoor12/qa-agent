import json

def load_ticket():
    with open("data/ticket.json", "r") as file:
        return json.load(file)


def load_tickets():
    with open("data/tickets.json", "r") as file:
        return json.load(file)    