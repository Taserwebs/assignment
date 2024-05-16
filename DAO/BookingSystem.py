from Util.DBconnenction import DBConnection
from Entity import Booking


class BookingSystemProvider(DBConnection):

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

    def book_tickets(self, event_name, num_tickets, booking_date, list_of_customers):
        try:
            self.cursor.execute(
                "SELECT event_id FROM Event WHERE event_name = ?", (event_name,)
            )
            event_id = self.cursor.fetchone()[0]
            for customer_id in list_of_customers:
                total_cost = self.calculate_booking_cost(num_tickets)
                self.cursor.execute(
                    """
                    INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost, booking_date)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (customer_id, event_id, num_tickets, total_cost, booking_date),
                )
                self.conn.commit()

            print("Tickets booked successfully!")
        except Exception as e:
            print(e)

    def cancel_booking(self, booking_id):
        try:
            self.cursor.execute(
                "SELECT * FROM Booking WHERE booking_id = ?", (booking_id,)
            )
            booking_details = self.cursor.fetchone()

            if not booking_details:
                print("Booking not found!")
                return
            self.cursor.execute(
                """
                UPDATE Event
                SET available_seats = available_seats + ?
                WHERE event_id = ?
                """,
                (booking_details[3], booking_details[2]),
            )
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
                print("Booking not found!")
        except Exception as e:
            print(e)