from Entity import Booking, Customers, Events, Venues
from DAO import EventService, BookingSystem


def main():
    event_service_provider = EventService()
    booking_service_provider = BookingSystem()

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
            event_id = int(input("Enter event ID: "))
            event_name = input("Enter event name: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM:SS): ")
            Venues.venue_id = int(input("Enter venue id:"))
            total_seats = int(input("Enter total number of seats: "))
            available_seats = int(input("Enter the available seats:"))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie/Sports/Concert): ")
            created_event = Events(
                event_id,
                event_name,
                event_date,
                event_time,
                Venues.venue_id,
                total_seats,
                available_seats,
                ticket_price,
                event_type,
            )
            event_service_provider.create_event(created_event)
        elif choice == "2":
            try:
                event_id = int(input("Enter event ID to book tickets: "))
                num_tickets = int(input("Enter the number of tickets to book: "))
                booking_date = input("Enter booking date (YYYY-MM-DD): ")
                list_of_customers = input(
                    "Enter customer IDs (comma-separated): "
                ).split(",")
                list_of_customers = [
                    int(customer_id) for customer_id in list_of_customers
                ]
                booking_service_provider.book_tickets(
                    event_id, num_tickets, booking_date, list_of_customers
                )
            except Exception as e:
                print("Error booking tickets:", e)
        elif choice == "3":
            try:
                booking_id = input("Enter booking ID to cancel: ")
                booking_service_provider.cancel_booking(booking_id)
            except Exception as e:
                print("Error canceling booking:", e)
        elif choice == "4":
            try:
                events, total_available_seats = (
                    EventService.event_service_provider.get_Available_No_Of_Tickets()
                )
                if events:
                    for event in events:
                        print(f"Event Name: {event[0]}, Available Seats: {event[1]}")
                    print(f"\nTotal Available Seats: {total_available_seats}")
                else:
                    print("No events found.")
            except Exception as e:
                print("Error fetching available seats:", e)
        elif choice == "5":
            try:
                event_service_provider.get_Event_Details()
            except Exception as e:
                print("Error fetching event details:", e)
        elif choice == "6":
            try:
                num_tickets = int(input("Enter the number of tickets: "))
                total_cost = booking_service_provider.calculate_booking_cost(
                    num_tickets
                )
                print(f"The total cost for {num_tickets} tickets is: {total_cost}")
            except Exception as e:
                print("Error calculating booking cost:", e)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()