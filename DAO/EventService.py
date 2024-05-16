from Entity import Venues,Events
from Util.DBconnenction import DBConnection
from Entity import Booking


class event_Service_Provider(DBConnection):

    def create_event(self, Event):
        try:
            self.cursor.execute(
                """
                INSERT INTO Event (event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type, venue_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    Event.event_name,
                    Event.event_date,
                    Event.event_time,
                    Event.total_seats,
                    Event.available_seats,
                    Event.ticket_price,
                    Event.event_type,
                    Venues.venue_id,
                ),
            )
            self.conn.commit()
            print("event created successfully")
        except Exception as e:
            print(e)

    def getEventDetails(self):
        try:
            print("Select the type of event details you want to see:")
            print("1. Movie event details")
            print("2. Concert event details")
            print("3. Sports event details")
            choice = int(input("Enter your choice (1/2/3): "))

            if choice == 1:
                event_type = "Movie"
            elif choice == 2:
                event_type = "Concert"
            elif choice == 3:
                event_type = "Sports"
            else:
                print("Invalid choice. Please enter a valid option.")

            self.cursor.execute(
                "SELECT * FROM Event WHERE event_type = ?", (event_type,)
            )
            event = self.cursor.fetchall()
            for event in Events:
                print(event)

        except Exception as e:
            print(e)

    def getAvailableNoOfTickets(self):
        try:
            self.cursor.execute("SELECT SUM(available_seats) FROM Event")
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(e)