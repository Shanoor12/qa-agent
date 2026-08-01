import json

def load_ticket():
    with open("data/ticket.json", "r") as file:
        return json.load(file)