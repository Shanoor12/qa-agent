from services.jira_client import load_ticket
from services.jira_client import load_tickets


# Dicrionary
# print("Program Started")

# with open("data/ticket.json", "r") as file:
#     ticket = json.load(file)

# print("========== JIRA TICKET ==========")
# print("Ticket ID   :", ticket["key"])
# print("Summary     :", ticket["summary"])
# print("Priority    :", ticket["priority"])
# print("Status      :", ticket["status"])
# print("Description :", ticket["description"])
# print("assignee    :", ticket["assignee"])
# print("=================================")

# print(type(ticket))
# print(ticket.keys())
# print(ticket.items())
# print(ticket.values())

# print("=================================")

# for key, value in ticket.items():
#     print(f"{key}: {value}")

# print("=================================")


# Functions


def display_ticket(ticket):
    print("\n========== JIRA TICKET ==========")
    print("Ticket ID   :", ticket["key"])
    print("Summary     :", ticket["summary"])
    print("Priority    :", ticket["priority"])
    print("Status      :", ticket["status"])
    print("Description :", ticket["description"])
    print("=================================")
     


def display_tickets(tickets):

    for ticket in tickets:
        print("\n========== JIRA TICKET ==========")
        print("Ticket ID   :", ticket["key"])
        print("Summary     :", ticket["summary"])
        print("Priority    :", ticket["priority"])
        print("Status      :", ticket["status"])
        print("Description :", ticket["description"])
        print("=================================")

        

def search_ticket(tickets):
    ticket_id = input("Enter Ticket ID: ")
    found = False
    for ticket in tickets:
        if ticket["key"] == ticket_id:
            display_ticket(ticket)
            found = True
            break
    if not found:
        print("ticket not found. ");     
    


def main():
    ticket = load_ticket()
    tickets = load_tickets()
    display_ticket(ticket)
    display_tickets(tickets)
    search_ticket(tickets)


if __name__ == "__main__":
    main()