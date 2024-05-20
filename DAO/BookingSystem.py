from Exception.Exception import EventNotFoundException, InvalidBookingIDException
from Interface import IBooking_system_service_provider
from Util.DBconnenction import DBConnection
from Entity import Booking


class Booking_System_Provider(DBConnection, IBooking_system_service_provider):

    def calculate_booking_cost(self, num_tickets):
        try:
            while True:
                print("Select the type of ticket:")
                print("1. Diamond")
                print("2. Gold")
                print("3. Silver")
                choice = int(input("Enter your choice (1/2/3): "))

                if choice == 1:
                    ticket_price = 200
                    break
                elif choice == 2:
                    ticket_price = 150
                    break
                elif choice == 3:
                    ticket_price = 100
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

            total_cost = num_tickets * ticket_price
            return total_cost
        except Exception as e:
            print(e)

    def book_tickets(self, event_id, num_tickets, booking_date, list_of_customers):
        try:
            # Retrieve event details
            self.cursor.execute(
                "SELECT available_seats FROM Event WHERE event_id = ?", (event_id,)
            )
            event_details = self.cursor.fetchone()
            if not event_details:
                raise EventNotFoundException(event_id)

            available_seats = event_details[0]
            if available_seats < num_tickets:
                print("Not enough available seats!")
                return

            # Calculate total cost for booking
            total_cost = self.calculate_booking_cost(num_tickets)

            # Generate a new booking_id
            self.cursor.execute("SELECT MAX(booking_id) FROM Booking")
            max_booking_id = self.cursor.fetchone()[0]
            new_booking_id = max_booking_id + 1 if max_booking_id is not None else 1

            # Book tickets for each customer in the list
            for customer_id in list_of_customers:
                self.cursor.execute(
                    """
                    INSERT INTO Booking (booking_id, customer_id, event_id, num_tickets, total_cost, booking_date)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        new_booking_id,
                        customer_id,
                        event_id,
                        num_tickets,
                        total_cost,
                        booking_date,
                    ),
                )
                self.conn.commit()
                new_booking_id += 1  # Increment for the next customer

            # Update the available seats in the Event table
            new_available_seats = available_seats - num_tickets
            self.cursor.execute(
                "UPDATE Event SET available_seats = ? WHERE event_id = ?",
                (new_available_seats, event_id),
            )
            self.conn.commit()

            print("Tickets booked successfully!")
        except Exception as e:
            print(e)

    def cancel_booking(self, booking_id):
        try:
            # Retrieve booking details
            self.cursor.execute(
                "SELECT event_id, num_tickets FROM Booking WHERE booking_id = ?",
                (booking_id,),
            )
            booking_details = self.cursor.fetchone()

            if not booking_details:
                raise InvalidBookingIDException(booking_id)

            event_id, num_tickets = booking_details

            # Update the available seats in the Event table
            self.cursor.execute(
                """
                UPDATE Event
                SET available_seats = available_seats + ?
                WHERE event_id = ?
                """,
                (num_tickets, event_id),
            )
            self.conn.commit()

            # Delete the booking record
            self.cursor.execute(
                "DELETE FROM Booking WHERE booking_id = ?", (booking_id,)
            )
            self.conn.commit()

            print("Booking canceled successfully!")
        except Exception as e:
            print(e)

    def get_booking_details(self, booking_id):
        try:
            self.cursor.execute(
                "SELECT * FROM Booking WHERE booking_id = ?", (booking_id,)
            )
            booking_details = self.cursor.fetchone()
            if booking_details:
                booking = Booking(*booking_details)
                return booking
            else:
                raise InvalidBookingIDException(booking_id)
        except Exception as e:
            print(e)