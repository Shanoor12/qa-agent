from services.jira_client import load_ticket


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


def main():
    ticket = load_ticket()
    display_ticket(ticket)


if __name__ == "__main__":
    main()