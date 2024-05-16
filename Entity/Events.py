class Event:
    def __init__(
            self,
            event_name,
            event_date,
            event_time,
            venue_name,
            total_seats,
            available_seats,
            ticket_price,
            event_type
    ):
        self.event_name = event_name
        self.event_date = event_date 
        self.event_time = event_time
        self.venue_name= venue_name
        self.total_seats= total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type 