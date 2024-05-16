from Entity import Booking, Customers, Events, Venues
from DAO import EventService, BookingSystem
def main():
    

    while True:
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. Get Available Seats")
        print("5. Get Event Details")
        print("6. Calculate Booking cost")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event_name = input("Enter event name: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM:SS): ")
            total_seats = int(input("Enter total number of seats: "))
            available_seats = int(input("Enter the available seats:"))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie/Sports/Concert): ")
            Venues.venue_id = input("Enter venue id:")
            created_event = Events(
                event_name,
                event_date,
                event_time,
                total_seats,
                available_seats,
                ticket_price,
                event_type,
                Venues.Venue.venue_id,
            )
            EventService.create_event(created_event)
        elif choice == "2":
            try:
                event_name = input("Enter event name to book tickets: ")
                num_tickets = int(input("Enter the number of tickets to book: "))
                booking_date = input("Enter booking date (YYYY-MM-DD): ")
                list_of_customers = []
                # You need to define and populate this list with customer IDs
                BookingSystem.book_tickets(
                    event_name, num_tickets, booking_date, list_of_customers
                )
            except Exception as e:
                print("Error booking tickets:", e)
        elif choice == "3":
            try:
                booking_id = input("Enter booking ID to cancel: ")
                BookingSystem.cancel_booking(booking_id)
            except Exception as e:
                print("Error canceling booking:", e)
        elif choice == "4":
            try:
                available_seats = EventService.getAvailableNoOfTickets()
                if available_seats:
                    print("\nTotal Available Seats:", available_seats)
                else:
                    print("No available seats found.")
            except Exception as e:
                print("Error fetching available seats:", e)
        elif choice == "5":
            try:
                EventService.getEventDetails()
            except Exception as e:
                print("Error fetching event details:", e)
        elif choice == "6":
            print("Exiting...")
            break
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()