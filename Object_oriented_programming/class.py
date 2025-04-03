"""
This module demonstrates a simple iteration over a list of fruits using the for loop.

Author: Arnold Murphy
Date: 2025-04-02
"""
class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def display_attendee(self):
        """Display the attendee's name and ticket count."""
        print(f'Name : {self.name}, Tickets: {self.tickets}')

    def add_ticket(self):
        """Increase the ticket count by 1 and display the updated count."""
        self.tickets += 1
        print(f'{self.name} tickets increased to {self.tickets}')

attendee1 = Attendee('A. Murphy', 1)
attendee1.display_attendee()
attendee2 = Attendee('B. Johnson', 2)
attendee2.display_attendee()
attendee1.add_ticket()
attendee2.add_ticket()
attendee2.add_ticket()
attendee2.add_ticket()


# End-of-file (EOF)
